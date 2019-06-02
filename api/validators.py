import decimal
from django.core.exceptions import ValidationError


def validate_brand(brand):
    if type(brand) != str or len(brand) > 20:
        raise ValidationError("Brand has to be a string with maximum 20 characters.")


def validate_color(color):
    if type(color) != str or len(color) > 20:
        raise ValidationError("Color has to be a string with maximum 20 characters.")


def validate_size(size):
    if size <= 0 or type(size) != int:
        raise ValidationError("Size has to be a positive integer number.")


def validate_price(price):
    if price <= 0 or type(price) != decimal.Decimal:
        raise ValidationError("Price has to be a positive decimal number.")


def validate_quantity(quantity):
    if quantity <= 0 or type(quantity) != int:
        raise ValidationError("Quantity has to be a positive integer number.")
