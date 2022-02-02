from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# модель Event
class Event(models.Model):
    title = models.CharField(max_length=200, default='',
                             verbose_name='Название')
    description = models.TextField(default='',
                                   verbose_name='Описание')
    date_start = models.DateTimeField(verbose_name='Дата начала')
    participants_number = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1), MaxValueValidator(10000)],
        verbose_name='Количество участников')
    is_private = models.BooleanField(default=False, verbose_name='Частное')

    class Meta:
        verbose_name_plural = 'События'  # форма единственного числа
        verbose_name = 'Событие'  # форма множественного числа

    def __str__(self):
        return self.title


# модель Category
class Category(models.Model):
    title = models.CharField(max_length=90, default='',
                             verbose_name='Категория')

    class Meta:
        verbose_name_plural = 'Категории'  # форма единственного числа
        verbose_name = 'Категория'  # форма множественного числа

    def __str__(self):
        return self.title