from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Shoe
from .validators import (
    validate_brand,
    validate_color,
    validate_price,
    validate_quantity,
    validate_size
)


class ShoeSerializer(ModelSerializer):
    brand = serializers.CharField(validators=[validate_brand])
    color = serializers.CharField(validators=[validate_color])
    size = serializers.IntegerField(validators=[validate_size])
    price = serializers.DecimalField(validators=[validate_price], decimal_places=2, max_digits=6)
    quantity = serializers.IntegerField(validators=[validate_quantity])

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
