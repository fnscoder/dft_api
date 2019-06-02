from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Shoe


class ShoeSerializer(ModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'brand',
            'color',
            'size',
            'price',
            'quantity',
            'created_at',
            'updated_at'
        )
