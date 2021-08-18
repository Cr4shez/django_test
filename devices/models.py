from django.db import models



class Device(models.Model):
    """Generic warning device - Siren or a Megaphone"""

    SIREN = "SR"
    MEGAPHONE = "MG"
    TYPE_CHOICES = [(SIREN, "Сирена"),
                    MEGAPHONE, "Громкоговоритель"]

    name = models.CharField(
        verbose_name='Название', max_length=200)
    type = models.CharField(
        verbose_name='Тип устройства',
        max_length=2,
        choices=TYPE_CHOICES,
        default=SIREN)
    address = models.CharField(
        verbose_name='Адрес размещения', max_length=200)
    latitude = models.FloatField(
        verbose_name='Широта')
    # DecimalField для указания шести знаков после запятой?
    longitude = models.FloatField(
        verbose_name='Долгота')
    sound_reaching_radius = models.PositiveIntegerField(
        verbose_name="Радиус зоны звукопокрытия (в метрах)")
