from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from datetime import date


def user_path(instance, filename):
    return '{}_uploads/{}'.format(instance.user.username, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # for university Staff only!
    userType = models.CharField(max_length=20, default='', null=True, blank=True)
    university = models.CharField(max_length=50, default='', blank=True)
    profilePic = models.ImageField(upload_to=user_path, blank=True)


class StudentInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nationality = models.CharField(max_length=200, default='', blank=True)
    nationalID = models.CharField(max_length=200, default='', blank=True)
    DateOfBirth = models.DateField(default=date.today(), blank=True)
    gender = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    city = models.CharField(max_length=200, default='', blank=True)
    state = models.CharField(max_length=50, default='', blank=True)
    zipcode = models.IntegerField(default=0, blank=True)
    phone_number = PhoneNumberField(default='', blank=True, unique=True)
    previousSchool = models.CharField(max_length=200, default='', blank=True)
    highest_level_of_study = models.CharField(max_length=200, default='', blank=True)
    year_of_completion = models.DateField(default=date.today(), blank=True)
    certificate_of_study = models.FileField(upload_to=user_path, blank=True)
    transcript = models.FileField(upload_to=user_path, blank=True)
