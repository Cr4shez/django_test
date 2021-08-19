"""Модуль для настройки конфигурации приложения."""
from django.apps import AppConfig


class DevicesConfig(AppConfig):
    """Класс конфигурации приложения."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'devices'
    verbose_name = "Устройства"
