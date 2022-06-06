"""
API VIEWS
retorna muitas coisa - __List
retorna só um - __Detail
VIEWS BASEADAS EM FUNÇÃO
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Pet
from .serializers import PetSerializer
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class PetList(APIView):
    # atributos padrão
    def get(self, request, format=None):
        # Passo 1 - ir no banco e pegar todos os pets
        pets = Pet.objects.all()
        # Passo 2 - instanciar serializer
        serializer = PetSerializer(pets, many=True) # o many é True qnd for lista
        return Response(serializer.data, status=HTTP_200_OK)

class PetDetail(APIView):
    # atributos padrão
    def post(self, request, format=None):
        # Passo 1 - pegar a request
        serializer = PetSerializer(data=request.data)
        # Passo 2 - validar body
        if serializer.is_valid():
            # Passo 2 - salvar no banco
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houverar erros de validação"
            },
            status=HTTP_400_BAD_REQUEST)