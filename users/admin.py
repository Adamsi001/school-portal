from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import BaseUser


class UserAdmin(BaseUserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = BaseUser
    list_display = ('email', 'is_active', "user_type",)
    list_filter = ('is_active', "user_type", "staff_type",)
    fieldsets = (
        ('Basic', {'fields': ('email', 'password',)}),
        ('User Information', {
         'fields': ( 'first_name', 'middle_name', 'last_name', 'gender',)}),
        ('User Type', {
            'fields': ('user_type', 'staff_type',)}
        ),
        ('Permissions', {'fields': ('is_staff',
         'is_active', 'is_superuser', 'user_permissions',)}),
        ('Groups', {'fields': ('groups',)}),
    )
    add_fieldsets = (
        ('Basic', {
            'fields': ('email', 'first_name', 'middle_name', 'last_name', 'gender',)}
         ),
        ('User Type', {
            'fields': ('user_type', 'staff_type',)}
         ),
        (None, {
            'fields': ('faculty', 'department', 'level',)}
         ),
        ('Authentication', {
            'fields': ('password1', 'password2',)}
         ),
        (None, {
            'fields': ( 'is_active',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(BaseUser, UserAdmin)
