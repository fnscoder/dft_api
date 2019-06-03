from django.contrib import admin
from .models import Shoe


class ShoeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'color', 'size', 'price', 'quantity', 'created_at', 'updated_at')


admin.site.register(Shoe, ShoeAdmin)
