from django.shortcuts import render
from django.views.generic import CreateView
from .models import addmission,payment
# Create your views here.

class NewAddmission(CreateView):
    model = addmission
    fields = '__all__'
    success_url = '/home/'

#    def __init__(self, *args, **kwargs):
#       super('MyForm', self).__init__(*args, **kwargs)
#      self.fields['student'].widget.attrs.update

class new_payment(CreateView):
    model = payment
    fields = '__all__'
    success_url = '/admin/'