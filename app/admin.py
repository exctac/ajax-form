from django.contrib import admin
from app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

