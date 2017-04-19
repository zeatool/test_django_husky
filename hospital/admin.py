from django.contrib import admin
from hospital.models import Doctor,Reception

class ReceptionInline(admin.TabularInline):
    model = Reception
    ordering = ('date', 'time')

class DoctorAdmin(admin.ModelAdmin):
    inlines = [ReceptionInline, ]

class ReceptionAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'date', 'time')
    date_hierarchy = 'date'
    list_filter = ('doctor', 'date', 'time')

# Register your models here.
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Reception,ReceptionAdmin)