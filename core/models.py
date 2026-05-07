from django.db import models

# Create your models here.
from django.db import models

class Certificate(models.Model):
    certificate_number = models.CharField(max_length=100, unique=True)
    company_name = models.CharField(max_length=255)
    standard = models.CharField(max_length=255)
    scope = models.TextField()
    issue_date = models.DateField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    validity = models.CharField(max_length=50)

    def __str__(self):
        return self.certificate_number

