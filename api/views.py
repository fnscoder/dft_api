from django.shortcuts import get_object_or_404

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Shoe
from .serializers import ShoeSerializer


class ShoeView(ListCreateAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer


class SingleShoeView(RetrieveUpdateDestroyAPIView):
    queryset = Shoe.objects.all()
    serializer_class = ShoeSerializer
