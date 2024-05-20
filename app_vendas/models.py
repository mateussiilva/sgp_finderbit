from django.db import models

# Create your models here.
class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.TextField(max_length=255)
    value = models.FloatField()

