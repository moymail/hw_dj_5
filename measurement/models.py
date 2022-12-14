from datetime import date

from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=55, verbose_name='Название')
    description = models.CharField(max_length=200, verbose_name='Описание', blank=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateField(default=date.today, verbose_name='Дата измерения')

