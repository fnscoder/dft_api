from django.db import models
from django.contrib.auth.models import User


class Shoe(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    size = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = 'calçados'
        verbose_name = 'calçado'

    def __str__(self):
        return self.brand
