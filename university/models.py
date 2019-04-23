from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class University(models.Model):
    title = models.CharField(max_length=200, default='', null=False)
    address = models.CharField(max_length=200, default='', null=False)
    city = models.CharField(max_length=200, default='', null=False)
    state = models.CharField(max_length=50, default='', null=False)
    zipcode = models.IntegerField(default=0, null=False)
    phone_number = PhoneNumberField(default=0, null=False, unique=True)
    website = models.URLField(max_length=200, default='', null=False)
    photo_main = models.ImageField(upload_to='UniPhotos/main/', blank=True)
    photo_logo = models.ImageField(upload_to='UniPhotos/Logo/', blank=True)
    description = models.TextField(default='', null=True)

    def __str__(self):
        return self.title
