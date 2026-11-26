from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from urllib.parse import urlsplit
from types import SimpleNamespace
from .seo import PAGE_LABELS


class StaticViewSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return [name for name in PAGE_LABELS if name != "iso_27001"]

    def location(self, item):
        return reverse(item)

    def get_urls(self, page=1, site=None, protocol=None):
        origin = urlsplit(settings.SITE_URL)
        return super().get_urls(page=page, site=SimpleNamespace(domain=origin.netloc), protocol=origin.scheme)
