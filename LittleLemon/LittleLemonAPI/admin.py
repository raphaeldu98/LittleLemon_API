from django.contrib import admin

# Register your models here.

from .models import Category, MenuItem, Cart, Order, OrderItem

models = [Category, MenuItem, Cart, Order, OrderItem]
for model in models:
    admin.site.register(model)