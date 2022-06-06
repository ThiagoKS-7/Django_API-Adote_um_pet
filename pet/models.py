from django.db import models

# MODELS SÃO AS CLASSES QUE VÃO REPRESENTAR O DB

# herança sempre da Model
class Pet(models.Model):
    nome = models.CharField(blank=False,null=False, max_length=255) # sem branco sem nulo máximo de 255 char (mesmo q VARCHAR)
    historia = models.TextField(blank=False,null=False) # TextField não tem tamanho máximo
    foto = models.URLField(blank=False,null=False) # valida a url
    '''
        CRIAR MIGRATION DA TABELA (versão do db)
        python manage.py makemigrations
    '''