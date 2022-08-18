from django.contrib import admin

# from .models import SimpleUser
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth import get_user_model as user_model
# from django.contrib.auth.admin import UserAdmin
# User = user_model()
# admin.site.register(SimpleUser)

# admin.site.register(User, UserAdmin)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('User Profile', {'fields': (
            'first_name',
            'last_name',
            'email',
            'date_de_naissance',
            'adresse',
            'ville',
            'code_postal',  
            'num_tel',
            'presentation',
            'profile_image',
            'resume',
            'avancement',
            
        )}),

        ('Permissions', {'fields': (
            'is_active', 
            'is_staff', 
            'is_superuser',
            # 'groups', 
            # 'user_permissions',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('username', 'password1', 'password2')
            }
        ),
    )

    list_display = ('username','email', 'is_staff', 'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


admin.site.register(User, UserAdmin)