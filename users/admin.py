from django.contrib import admin
from users.models import NewUser
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

# Register your models here.

class UserAdminConfig(UserAdmin):
    search_fields = ('email', 'username', 'first_name',)
    filter = ('email', 'user_name', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    # To eliminate field error
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
        ('Personal', {'fields': ('about',)}),
    )

    formfield_overrides = {
        NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 40})},
    }

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')
        }),
    )


admin.site.register(NewUser, UserAdminConfig)

