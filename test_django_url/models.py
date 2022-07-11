from django.db import models
from django.contrib.auth.models import User


class ShortUrl(models.Model):
    url = models.CharField(max_length=50, verbose_name='Сокращенный url')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Пользователи')

    class Meta:
        verbose_name_plural = 'Сокращенный url'
        verbose_name = 'Сокращенный url'