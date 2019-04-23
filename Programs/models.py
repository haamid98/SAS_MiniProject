from django.db import models
from university.models import University


class Program(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='', null=False)
    department = models.CharField(max_length=200, default='', null=False)
    level = models.CharField(max_length=200, default='', null=False)
    requirements = models.TextField(default='', null=False)
    duration = models.FloatField(default=0, null=False)
    campus = models.CharField(max_length=200, default='', null=False)
    description = models.TextField(default='', null=False)

    def __str__(self):
        return self.title
