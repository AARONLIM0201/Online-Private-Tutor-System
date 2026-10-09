from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from account.models import Account

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'role', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username','role')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal=()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin) #this will make the Account model visible on the admin page