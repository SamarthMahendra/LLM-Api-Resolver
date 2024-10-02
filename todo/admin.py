from django.contrib import admin

# Register your models here.

# todo app table

from .models import Todo

admin.site.register(Todo)

