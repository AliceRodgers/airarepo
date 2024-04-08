from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group, Permission

class AiraUser(AbstractUser):
    # Your custom fields
    def save(self, *args, **kwargs):
        # Your custom logic here (if any)
        super().save(*args, **kwargs)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null = True)
    class Meta:
        permissions = (("can_access_dashboard", "Can access dashboard"),)

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, verbose_name=_('user permissions'), blank=True, related_name='custom_user_permissions')

    def _str_(self):
     return self.username
    
class Product(models.Model):
        category = models.CharField(max_length=100, null=True)
        # Add more types as needed
        image = models.ImageField(upload_to='images/', null=True)
        name = models.CharField(max_length=100)
        brand = models.CharField(max_length=100,null=True)
        price = models.PositiveIntegerField(null=True)
        cart = models.ManyToManyField(AiraUser, related_name="addtocart",blank=True)
def _str_(self):
    return self.name