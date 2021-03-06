from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import addmission,payment,courses_master
# Create your views here.


class NewCourse(CreateView):
    model = courses_master
    fields = '__all__'
    extra_context = {'page_title':'New Course'}



class ViewCourse(ListView):
    model = courses_master
    context_object_name = "Courses"
    ordering = ['-name']

class updatecourse(UpdateView):
    model = courses_master
    fields = '__all__'

class deletecourse(DeleteView):
    model = courses_master
    success_url = '/course/view'

