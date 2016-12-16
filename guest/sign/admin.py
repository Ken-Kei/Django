from django.contrib import admin
from sign.models import Event, Guest


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'limit', 'status', 'address', 'start_time', 'create_time']
    search_fields = ['name']
    list_filter = ['status']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'event', 'phone', 'email', 'sign', 'create_time']
    search_fields = ['real_name', 'event__name', 'phone', 'email']
    list_filter = ['sign']

# Register your models here.
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)
