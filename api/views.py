from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Shoe
from .serializers import ShoeSerializer


class ShoeView(ListCreateAPIView):
    queryset = Shoe.objects.get_queryset().order_by('id')
    serializer_class = ShoeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("brand", "color", "size", "price", "quantity")


class SingleShoeView(RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
