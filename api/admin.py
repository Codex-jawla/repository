from django.contrib import admin

from api.models import *

# Register your models here.
class collageadmin(admin.ModelAdmin):
    list_display = ['cname','cAddress']

class studentadmin(admin.ModelAdmin):
    list_display = ['sName','sEmail']


admin.site.register(Collage,collageadmin)
admin.site.register(Student,studentadmin)