from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomPermissions:
    SUPERVISOR = 'supervisor'

class CustomUser(AbstractUser):
    class Meta:
        permissions = [
            (CustomPermissions.SUPERVISOR, 'Supervisor de classe'),
        ]

class Classe (models.Model):
    nome = models.CharField(max_length=20)
    qtd_membros = models.IntegerField(default=0)

    def __str__(self):
        return f'${self.nome} | ${self.qtd_membros} alunos'
    
class Requisito (models.Model):
    descricao = models.CharField(max_length=500)