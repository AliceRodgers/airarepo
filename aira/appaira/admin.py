"""module containing admin registrations"""
from django.contrib import admin
from .models import AiraUser, Product
# Import the CustomUser model after Django's apps are ready

# Import the CustomUser model and register it with the admin site.
admin.site.register(AiraUser)
admin.site.register(Product)
