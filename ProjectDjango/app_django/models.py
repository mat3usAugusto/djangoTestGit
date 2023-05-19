from django.db import models

class Test(models.Model):
    nome = models.CharField(
        max_length=100
    )
