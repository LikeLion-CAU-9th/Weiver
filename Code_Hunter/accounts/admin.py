from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# UserAdmin > helper class for making admin screen
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    # override some attributes
    list_display = ('email', 'nickname', 'joined_on', 'is_admin', 'is_staff')
    # admin console에 보여줄 것들
    search_fields = ('email', 'nickname', )
    ordering = ("nickname", )
    # admin console에 search 가능한 attrib
    readonly_fields = ('joined_on', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    # required stuff but don't wanna use


admin.site.register(CustomUser, CustomUserAdmin)
