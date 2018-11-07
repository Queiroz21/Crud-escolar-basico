from django.db import models
from django import forms

# Create your models here.

class InscricaoAluno(models.Model):
        nome = models.CharField(max_length=100) 
        email = models.EmailField()
        dtnasc = models.DateField()
        celular = models.IntegerField()
        ra = models.IntegerField()
        foto = models.CharField(max_length=800)

        class Meta:
        	#Então, descrever pra que serve isso~~
                ordering = ['nome']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome

class InscricaoProf(models.Model):
        nome = models.CharField(max_length=100) 
        email = models.EmailField()
        hab = models.CharField(max_length=500)
        celular = models.IntegerField()
        cpf = models.CharField(max_length=14)
        #Existe campo numero/salario?
        salario = models.CharField(max_length=9)

        class Meta:
                #Então, descrever pra que serve isso~~
                ordering = ['nome']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome

class InscricaoDisc(models.Model):
        
        nome = models.CharField(max_length=100) 
        cargaH = models.IntegerField()
        PctTeo = models.IntegerField()
        PctPrat = models.IntegerField()
        CoordCurso = models.IntegerField()
        PlanoEns = models.CharField(max_length=1000)

        class Meta:
                #Então, descrever pra que serve isso~~
                ordering = ['nome']
                verbose_name = (u'nome')
                verbose_name_plural = (u'nomes')

        def __unicode__(self):
                return self.nome

        
