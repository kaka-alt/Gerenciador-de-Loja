from django.db import models

class register(models.Model):
    nome = models.CharField(max_length = 50)
    email = models.CharField(max_length = 100)
    
    

    def __str__(self) -> str:
        return self.nome
