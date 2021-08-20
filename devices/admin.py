"""Модуль для управления панелью администратора."""
from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Device


class RadiusListFilter(admin.SimpleListFilter):
    """Класс для обеспечения фильтрации по радиусу оповещения с шагом 100."""

    title = 'Радиус зоны звукопокрытия'
    parameter_name = 'radius'

    def lookups(self, request, model_admin):
        """Метод для выбора значений фильтрации."""
        return ((100, ">100"),
                (200, ">200"),
                (300, ">300"),
                (400, ">400"),
                (500, ">500"),)

    def queryset(self, request, queryset):
        """Метод для вывода данных в зависимости от фильтра."""
        if self.value():
            return queryset.filter(sound_reaching_radius__gte=self.value())


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """Класс для кастомизации управления устройствами оповещения."""

    list_display = ('name', 'type', 'sound_reaching_radius', 'address')
    list_filter = ('type', RadiusListFilter,)
    search_fields = ('name', 'address')


admin.site.site_header = 'Справочник устройств оповещения'
admin.site.site_title = "Устройства оповещения"
admin.site.index_title = "Тестовое задание"

# Register your models here.
admin.site.unregister(Group)
admin.site.unregister(User)
