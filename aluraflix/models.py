from django.db import models

class Video(models.Model):
    titulo = models.CharField(max_length = 30, blank=False)
    descricao = models.CharField(max_length = 300, blank=False)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.titulo