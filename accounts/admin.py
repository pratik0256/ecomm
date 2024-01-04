from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(CartItems)


# class CartItems(admin.ModelAdmin):
#     list_display = ['size_variant' , 'color_cariant']
#     model = Cart
    