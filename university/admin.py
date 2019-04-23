from django.contrib import admin
from university.models import University


class displayUni(admin.ModelAdmin):
    list_display = ('title', 'phone_number', 'website')


admin.site.register(University, displayUni)
