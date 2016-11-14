from rest_framework import serializers
import models

class UrlSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = models.Url
        fields = ('id','originalUrl','shortUrl')
