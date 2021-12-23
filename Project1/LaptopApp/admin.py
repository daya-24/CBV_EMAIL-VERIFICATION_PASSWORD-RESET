from django.contrib import admin
from .models import Laptop


# Register your models here.

class LaptopModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'model_name', 'ram', 'rom', 'processor', 'price', 'weight']


admin.site.register(Laptop, LaptopModelAdmin)