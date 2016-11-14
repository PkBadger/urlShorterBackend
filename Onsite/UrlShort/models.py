from __future__ import unicode_literals

from django.db import models

class Url(models.Model):
    originalUrl = models.URLField(null= False)
    shortUrl = models.SlugField(max_length=6,null=True)

#class PersonalizedUrl(models.Model):
#    Url = models.OneToOneField(Url)
# Create your models here.
