from django.contrib import admin
from accounts.models import UserProfile
from accounts.models import StudentInformation


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'userType', 'university')
    list_display_links = ('id', 'user_id')
    list_per_page = 20


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(StudentInformation)
