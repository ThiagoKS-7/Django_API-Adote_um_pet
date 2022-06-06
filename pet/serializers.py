"""
    SERIALIZAÇÃO = CONVERSÃO JSON/PYTHON
    SERVIRÁ PRA TRATAR AS REQUESTS E AS RESPONSES
"""
from rest_framework import serializers
from .models import Pet

class PetSerializer(serializers.ModelSerializer):
    #configurações iniciais com uma metaclass
    class Meta:
       model = Pet # validações vão se basear no modelo
       fields = ('id', 'nome', 'historia', 'foto') # tupla doq vai retornar na response