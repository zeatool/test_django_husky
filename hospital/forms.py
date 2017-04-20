from datetime import datetime

from django import forms
from django.forms import ModelForm
from hospital.models import Reception


class ReceptionForm(ModelForm):
    def clean(self):
        cleaned_data = super(ReceptionForm, self).clean()

        date = cleaned_data.get('date')
        time = cleaned_data.get('time')
        doctor = cleaned_data.get('doctor')

        if not date.weekday() in [i for i in range(5)]:
            raise forms.ValidationError("Не возможно записаться, мы работаем с пн. по пт.")
        if not time.hour in [i for i in range(9, 19)]:
            raise forms.ValidationError("Не возможно записаться, мы работаем с 9:00 до 18:00")
        if Reception.objects.filter(date=date,time=time,doctor=doctor).count()>0:
            raise forms.ValidationError("На данную дату уже есть запись")

    class Meta:
        model = Reception
        fields = ('fio','doctor', 'date', 'time' )
        widgets = {
            'fio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ф.И.О.'
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Имя врача',
            }),
            'date': forms.TextInput(attrs={
                'class': 'form-control js-date',
            }),
            'time': forms.Select(attrs={
                'class': 'form-control',
            },choices=[(str(i)+":00", str(i)+":00") for i in range(9,19)])
        }