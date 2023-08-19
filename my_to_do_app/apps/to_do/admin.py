from django.contrib import admin

# Register your models here.
from apps.to_do.models import Todo

admin.site.register(Todo)