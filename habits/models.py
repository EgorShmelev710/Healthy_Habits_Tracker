from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    FREQUENCY_UNITS = [
        ("minutes", "минуты"),
        ("hours", "часы"),
        ("days", "дни"),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='создатель привычки',
                             **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='место привычки')
    time = models.DateTimeField(verbose_name='время привычки')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='приятная')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE, verbose_name='связанная привычка')
    frequency_number = models.PositiveIntegerField(verbose_name='количество раз')
    frequency_unit = models.CharField(max_length=10, choices=FREQUENCY_UNITS, default='days',
                                      verbose_name='единицы измерения')
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.DurationField(verbose_name='длительность действия')
    is_public = models.BooleanField(verbose_name='публичная')

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
