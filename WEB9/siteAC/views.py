from django.shortcuts import render
# Create your views here.
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.template import Template, Context

def home(request):
        return render(request,'index.html')

def prof(request):
        return render(request,'crud_prof.html')

def aluno(request):
        return render(request,'crud_aluno.html')

def disci(request):
        return render(request,'crud_disc.html')