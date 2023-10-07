from typing import Any
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse
from app.forms import *

class temp(TemplateView):
    template_name='temp.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        #ECDO['name']='supraja'
        SFO=StudentForm()
        ECDO['SFO']=SFO
        return ECDO
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data is inerted')