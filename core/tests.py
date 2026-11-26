from xml.etree import ElementTree

from django.test import SimpleTestCase
from django.urls import reverse

from .seo import PAGE_LABELS


class PublicPageSEOTests(SimpleTestCase):
    def test_public_pages_have_distinct_metadata_and_canonical_urls(self):
        titles = set()
        for name in PAGE_LABELS:
            if name == 'iso_27001':
                continue
            with self.subTest(page=name):
                path = reverse(name)
                response = self.client.get(path, HTTP_HOST='localhost')
                self.assertEqual(response.status_code, 200)
                self.assertContains(response, f'https://www.tiscertification.com{path}')
                self.assertNotContains(response, 'pythonanywhere.com')
                title = response.context['seo_title']
                self.assertNotIn(title, titles)
                titles.add(title)

    def test_sitemap_uses_public_origin_even_on_local_requests(self):
        response = self.client.get('/sitemap.xml', HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)
        urls = [node.text for node in ElementTree.fromstring(response.content).iter(
            '{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
        self.assertEqual(len(urls), len(PAGE_LABELS) - 1)
        self.assertTrue(all(url.startswith('https://www.tiscertification.com/') for url in urls))
        self.assertNotIn('https://www.tiscertification.com/certifications/iso-27001/', urls)

    def test_old_iso_27001_url_redirects_to_the_existing_page(self):
        self.assertRedirects(self.client.get(reverse('iso_27001'), HTTP_HOST='localhost'),
                             reverse('iso_iec_27001'), status_code=301)

    def test_home_images_defer_gallery_but_prioritize_hero(self):
        response = self.client.get('/', HTTP_HOST='localhost')
        self.assertContains(response, 'fetchpriority="high"')
        self.assertContains(response, 'loading="lazy"')
        self.assertContains(response, 'images/hero-certification.webp')
