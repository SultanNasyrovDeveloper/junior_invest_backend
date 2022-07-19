from django.contrib import admin

from junior_invest.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
