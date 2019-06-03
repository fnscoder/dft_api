from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import File, Shoe
from .validators import (
    validate_brand,
    validate_color,
    validate_price,
    validate_number
)


class ShoeSerializer(ModelSerializer):
    brand = serializers.CharField(validators=[validate_brand])
    color = serializers.CharField(validators=[validate_color])
    size = serializers.IntegerField(validators=[validate_number])
    price = serializers.DecimalField(
        validators=[validate_price], decimal_places=2, max_digits=6)
    quantity = serializers.IntegerField(validators=[validate_number])

    class Meta:
        model = Shoe
        fields = (
            'id',
            'brand',
            'color',
            'size',
            'price',
            'quantity',
            'created_at',
            'updated_at'
        )


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
