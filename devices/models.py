"""Модуль для определения используемых моделей."""
from django.db import models


class Device(models.Model):
    """Модель устройства оповещения.

    1. Название
    2. Тип устройства(Сирена или Мегафон)
    3. Адрес размещения
    4. Широта
    5. Долгота
    6. Радиус зоны звукопокрытия (в метрах)
    """

    SIREN = "SR"
    MEGAPHONE = "MG"
    TYPE_CHOICES = [(SIREN, 'Сирена'),
                    (MEGAPHONE, 'Громкоговоритель')]

    class Meta:
        """Дополнительная информация о модели - название модели для вывода."""

        verbose_name_plural = "устройства оповещения"
        verbose_name = "устройство"

    name = models.CharField(
        verbose_name='Название',
        max_length=200
    )
    type = models.CharField(
        verbose_name='Тип устройства',
        max_length=2,
        choices=TYPE_CHOICES,
        default=SIREN
    )
    address = models.CharField(
        verbose_name='Адрес размещения',
        max_length=200
    )
    # или DecimalField для указания шести знаков после запятой?
    latitude = models.FloatField(
        verbose_name='Широта'
    )
    longitude = models.FloatField(
        verbose_name='Долгота'
    )
    sound_reaching_radius = models.PositiveIntegerField(
        verbose_name='Радиус зоны звукопокрытия (в метрах)'
    )

    def __str__(self):
        """Метод для отображения информации об экземпляре.

        Возвращает название устройства оповещения.
        """
        return str(self.name)
