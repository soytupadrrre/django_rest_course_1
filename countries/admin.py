from django.contrib import admin
from countries.models import Countries

# Register your models here.

class Admin_Countries(admin.ModelAdmin):
    """
    Admin Model for manage Model Countries

    :param admin: super class admin.ModelAdmin
    :type admin: class
    """
    list_display = ("id", "name", "capital")
    search_fields = ("id", "name", "capital")

admin.site.register(Countries, Admin_Countries)