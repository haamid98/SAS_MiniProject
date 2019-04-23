from django.contrib import admin
from Programs.models import Program


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'university', 'department')

admin.site.register(Program)
