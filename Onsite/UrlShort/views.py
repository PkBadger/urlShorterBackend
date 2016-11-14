from django.shortcuts import render
import serializers
import models
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
# Create your views here.
class UrlViewSet(viewsets.ModelViewSet):
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerizalizer

    def get_queryset(self):
        short = self.request.query_params.get('short',None)

        query = models.Url.objects.all()
        if(short is not None):
            query = query.filter(shortUrl = short)
        return query

    def create(self, request, *args, **kwargs):
        request = request.data.copy()
        serializer = self.get_serializer(data=request)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        UrlId = serializer.data['id']
        instance = models.Url.objects.get(id=UrlId)
        request['shortUrl'] = self.encode(UrlId,"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        serializer = self.get_serializer(instance, data=request, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def encode(self,num, alphabet):
        """Encode a positive number in Base X

        Arguments:
        - `num`: The number to encode
        - `alphabet`: The alphabet to use for encoding
        """
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)
