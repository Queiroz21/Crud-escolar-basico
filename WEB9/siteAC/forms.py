#Criando o arquivo forms.py

from django import forms
from .import models

class InscricaoFormAluno(forms.ModelForm):      

    class Meta:
        model = models.InscricaoAluno
        #Declarando que todos os campos fazem parte deste formulário
        fields = "__all__" 

class InscricaoFormProf(forms.ModelForm):      

    class Meta:
        model = models.InscricaoProf
        #Declarando que todos os campos fazem parte deste formulário
        fields = "__all__" 

class InscricaoFormDisc(forms.ModelForm):      

    class Meta:
        model = models.InscricaoDisc
        #Declarando que todos os campos fazem parte deste formulário
        fields = "__all__" 