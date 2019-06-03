import csv
from decimal import Decimal
from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Shoe
from .serializers import ShoeSerializer, FileSerializer


class ShoeView(ListCreateAPIView):
    queryset = Shoe.objects.get_queryset().order_by('id')
    serializer_class = ShoeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("brand", "color", "size", "price", "quantity")


class SingleShoeView(RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class FileUploadView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()

            with open('media/shoe.csv', 'r') as data:
                reader = csv.DictReader(data)

                for l in reader:
                    l['price'] = Decimal(l['cost']) + Decimal(l['profit'])
                    shoe = Shoe(
                        brand=l['brand'],
                        color=l['color'],
                        size=l['size'],
                        price=l['price'],
                        quantity=l['quantity'],
                    )
                    try:
                        shoe.save()
                    except:
                        print('there was a error with line ', l)
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
