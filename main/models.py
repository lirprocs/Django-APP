from django.db import models


class DANPOLZ(models.Model):
    Nickname = models.CharField('Nickname', max_length=50)

    def __str__(self):
        return self.Nickname

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

