from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(student)
class studentadmin(admin.ModelAdmin):
    list_display = ['id','name','city','age']