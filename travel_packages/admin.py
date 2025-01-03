from django.contrib import admin
from .models import TravelPackage
from tinymce.widgets import TinyMCE
from django.db import models

@admin.register(TravelPackage)
class TravelPackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'original_price', 'discounted_price')

    formfield_overrides = {models.TextField: {'widget': TinyMCE()}}