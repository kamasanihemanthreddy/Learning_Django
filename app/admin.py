from django.contrib import admin
from .models import Document,SalesData, EasycomData
# Register your models here.
admin.site.register(Document)
admin.site.register(SalesData)
admin.site.register(EasycomData)