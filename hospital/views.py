import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from hospital.forms import ReceptionForm
from .models import Doctor,Reception

# Create your views here.
def index(request):
    doctors = Doctor.objects.all()
    initial = {
        'date' : datetime.datetime.now().strftime("%d.%m.%Y"),
    }
    form = ReceptionForm(initial=initial)

    context = {
        'doctors':doctors,
        'form':form
    }
    return render(request,'index.html',context)

def add_reception(request):
    form = ReceptionForm(request.POST)

    data = {
        'RESULT': True,
        'MESSAGE': ''
    }

    if not form.is_valid():
        data['RESULT']=False
        for msg in form.errors["__all__"]:
            data['MESSAGE'] += msg
    else:
        data['MESSAGE'] = 'Вы успешно записаны'
        form.save()

    return JsonResponse(data)