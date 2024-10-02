from django.contrib import admin

# Register your models here.

# API app table

from .models import Api

admin.site.register(Api)
