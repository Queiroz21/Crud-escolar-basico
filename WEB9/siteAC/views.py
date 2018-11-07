from django.shortcuts import render
# Create your views here.
# Create your views here.
# -*- coding: utf-8 -*-
from django.views.generic import CreateView, ListView
from django.template import Template, Context
from siteAC.models import InscricaoAluno, InscricaoProf, InscricaoDisc
from siteAC.forms import InscricaoFormAluno, InscricaoFormProf, InscricaoFormDisc

def home(request):
        return render(request,'index.html')

class Prof(CreateView):
        template_name = 'crud_prof.html'
        model = InscricaoProf
        fields = "__all__"

class Aluno(CreateView):
        template_name = 'crud_aluno.html'
        model = InscricaoAluno
        fields = "__all__" 

#BEA É CLASS NÃO DEF
class Disc(CreateView):
        template_name = 'crud_disc.html'
        model = InscricaoDisc
        #Porque fields tem que ser ALL???
        fields = "__all__"