import datetime

from django.db import models

# Create your models here.
class Doctor(models.Model):
    fio = models.CharField(verbose_name='Ф.И.О.',max_length=150)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return self.fio



class Reception(models.Model):
    doctor = models.ForeignKey(Doctor,verbose_name='Врач')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    fio = models.CharField(verbose_name='Ф.И.О. пациента', max_length=150)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return 'Запись №{0} от {1} {2}'.format(self.id,self.date,self.time)