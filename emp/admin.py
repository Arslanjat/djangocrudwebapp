from django.contrib import admin 
from .models import Emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=('name', 'working', 'emp_id', 'phone')
    list_editable=('working', 'emp_id')
    search_fields=('working', 'emp_id')
    list_filter=('working', 'emp_id')

admin.site.register(Emp, EmpAdmin)