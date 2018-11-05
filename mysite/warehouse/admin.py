from django.contrib import admin
from django.db import models
# Register your models here.

from .models import Category,Product,Magazyn,Product_Change_log


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Magazyn)
admin.site.register(Product_Change_log)

