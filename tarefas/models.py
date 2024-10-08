from django.db import models

class Tarefas(models.Model):
    nome = models.CharField(max_length=255)
    pronta = models.BooleanField(default=False)

    def __str__(self):
        return self.nome