from django.contrib import admin

from .models import Bookie, SubProfile


@admin.register(Bookie)
class BookieAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'email', 'phone_number')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(SubProfile)
class SubProfileAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'bookie', 'user', 'balance', 'exposure_limit', 'is_active', 'is_suspended', 'is_locked')
    list_filter = ('bookie', 'is_active', 'is_suspended', 'is_locked', 'created_at', 'updated_at')
    search_fields = ('nickname', 'bookie__name', 'user__username')
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
