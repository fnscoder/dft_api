import decimal
from django.core.exceptions import ValidationError


def validate_brand(brand):
    if len(brand) > 20:
        raise ValidationError(
            "Brand has to be a string with maximum 20 characters.")


def validate_color(color):
    if len(color) > 20:
        raise ValidationError(
            "Color has to be a string with maximum 20 characters.")


def validate_number(number):
    if number <= 0 or type(number) != int:
        raise ValidationError("Has to be a positive integer number.")


def validate_price(price):
    if price <= 0 or type(price) != decimal.Decimal:
        raise ValidationError("Price has to be a positive decimal number.")
