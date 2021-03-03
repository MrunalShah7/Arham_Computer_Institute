from django.contrib import admin
from .models import courses_master,student,addmission,payment,attendance,timetable
# Register your models here.
admin.site.register(courses_master)
admin.site.register(student)
admin.site.register(addmission)
admin.site.register(payment)
admin.site.register(attendance)
admin.site.register(timetable)