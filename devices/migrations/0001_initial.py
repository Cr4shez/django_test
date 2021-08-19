# Generated by Django 3.2.6 on 2021-08-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('type', models.CharField(choices=[('SR', 'Сирена'), ('MG', 'Громкоговоритель')], default='SR', max_length=2, verbose_name='Тип устройства')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес размещения')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('sound_reaching_radius', models.PositiveIntegerField(verbose_name='Радиус зоны звукопокрытия (в метрах)')),
            ],
        ),
    ]