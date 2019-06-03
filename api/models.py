from django.db import models
from django.contrib.auth.models import User


class Shoe(models.Model):
    brand = models.CharField('Marca', max_length=20)
    color = models.CharField('Cor', max_length=20)
    size = models.IntegerField('Tamanho')
    price = models.DecimalField('Preço', decimal_places=2, max_digits=6)
    quantity = models.IntegerField('Quantidade')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'calçado'
        verbose_name_plural = 'calçados'

    def __str__(self):
        return self.brand


class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
