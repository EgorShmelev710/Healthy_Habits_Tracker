from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Habit(models.Model):
    FREQUENCY_UNITS = [
        ("minutes", "минуты"),
        ("hours", "часы"),
        ("days", "дни"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='создатель привычки')
    place = models.CharField(max_length=200, verbose_name='место привычки')
    time = models.DateTimeField(verbose_name='время привычки')
    action = models.CharField(max_length=200, verbose_name='действие')
    is_pleasant = models.BooleanField(verbose_name='приятная')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, **NULLABLE)
    frequency_number = models.PositiveIntegerField()
    frequency_unit = models.CharField(max_length=10, choices=FREQUENCY_UNITS, default='days')
    reward = models.CharField(max_length=200, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.DurationField()
    is_public = models.BooleanField()

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
