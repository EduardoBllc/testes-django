from django.db import models


# Create your models here.
class Ingresso(models.Model):
    id = models.AutoField(primary_key=True)
    validado = models.BooleanField(default=False)
    data_sessao = models.DateTimeField()

    def __str__(self):
        return self.id.__str__()

