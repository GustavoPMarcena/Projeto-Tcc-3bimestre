from email.policy import default
from django.db import models
from django.contrib.postgres.fields import *

# Create your models here.
class Tcc(models.Model):

    autor = models.CharField(max_length=150, default=None)
    titulo = models.CharField(max_length=150, default=None)
    orientador = models.CharField(max_length=150, default=None)
    ano_documento = models.IntegerField(verbose_name = "Ano do Tcc", default=None)
    resumo = models.TextField(max_length=150, default=None)
    arquivo = models.FileField(default=None, blank=True)
   # achar o caminho correto do arquivo dps

    def __str__(self) -> str:
        return self.titulo
    
    
  