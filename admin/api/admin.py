from django.contrib import admin

from .models import Breed, Dog

# Register your models here.
admin.site.register(Dog)
admin.site.register(Breed)