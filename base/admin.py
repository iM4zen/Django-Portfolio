# in your_app/admin.py

from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'web_developer', 'email')

    actions = ['make_web_developer']

    def make_web_developer(self, request, queryset):
        queryset.update(web_developer=True)
    make_web_developer.short_description = "Mark selected profiles as Web Developers"
