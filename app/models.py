from django.db import models


class Profile (models.Model):
    first_name = models.CharField('Имя', max_length=255)
    last_name = models.CharField('Фамилия', max_length=255)
    phone = models.CharField('Моб. телефон', max_length=250)
    email = models.CharField('Email', max_length=250)
    birthday = models.DateField('Дата рождения')

    def __str__(self):  # __unicode__ on Python 2
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
