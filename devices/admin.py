from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Device


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'sound_reaching_radius')
    list_filter = ('type', 'sound_reaching_radius')


admin.site.site_header = 'Справочник устройств оповещения'
admin.site.site_title = "Устройства оповещения"
admin.site.index_title = "Тестовое задание"

# Register your models here.
admin.site.register(Device, DeviceAdmin)




