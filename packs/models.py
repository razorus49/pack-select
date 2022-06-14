from django.db import models


class Packs(models.Model):
    name = models.CharField(max_length=255)
    rating = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    download_link = models.CharField(max_length=2083)
    description = models.CharField(max_length=2100)


