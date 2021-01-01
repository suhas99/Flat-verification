from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as u
import datetime
# # Register your models here.
from .models import User, Alerts, Projects, Floors, Blob


class UserAdmin(u):
    model = User
    fieldsets = u.fieldsets + (
        (None, {'fields': ('name', 'profile_image', 'extra', 'type', 'preferences', 'status', 'tel')}),
    )


class AlertsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'title', 'detail', 'status', 'app_redirect',
                    'created_at', 'created_by', 'modified_at', 'modified_by', 'is_deleted')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'name', 'location', 'status', 'type',
                    'created_at', 'created_by', 'modified_at', 'modified_by', 'is_deleted')


class FloorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'house_id', 'type', 'name', 'nm_meta', 'extra'
                    , 'created_by', 'modified_at','modified_by', 'is_deleted')


class BlobAdmin(admin.ModelAdmin):
    list_display = ('id', 'floor_id', 'data','nm_meta',
                    'created_at', 'created_by', 'modified_at', 'modified_by', 'is_deleted')


admin.site.register(User, UserAdmin)
admin.site.register(Alerts, AlertsAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(Floors, FloorsAdmin)
admin.site.register(Blob, BlobAdmin)
