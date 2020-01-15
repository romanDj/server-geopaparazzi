import datetime
from django.db import models
from geopaparazzi.users.models import User
from django.urls import reverse

# Модель подразделений
class Subdivision(models.Model):
    title = models.CharField("название подразделения", max_length=70)
    description = models.CharField("краткое описание", max_length=300)
    participants = models.ManyToManyField(User, verbose_name='участники')
    created_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата создания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('subdivision_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

#Модель проектов
class Project(models.Model):
    title = models.CharField("название проекта", max_length=70)
    description = models.CharField("краткое описание", max_length=300)
    owner = models.ForeignKey(Subdivision, on_delete=models.CASCADE, verbose_name='подразделение')
    created_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Дата создания')
    edit_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
