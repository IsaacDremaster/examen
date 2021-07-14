from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=50)


class Team(models.Model):
    name_avanger = models.ForeignKey(Name, models.SET_NULL, 'Avanger', null=True)
    name = models.CharField('Имя героя', max_length=50)
    gender = models.CharField('Пол', max_length=50)
    ability = models.CharField('Способность', max_length=50)