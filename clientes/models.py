from django.db import models


class Cliente(models.Model):
    id_client = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    # address = models.TextField(max_length=255)