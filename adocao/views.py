from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import AdocaoSerializer
from .models import Adocao
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST,HTTP_200_OK

class AdocaoList(APIView):
    # atributos padrão
    def get(self, request, format=None):
        # Passo 1 - ir no banco e pegar todos os Adocaos
        Adocoes = Adocao.objects.all()
        # Passo 2 - instanciar serializer
        serializer = AdocaoSerializer(Adocoes, many=True) # o many é True qnd for lista
        return Response(serializer.data, status=HTTP_200_OK)

class AdocaoDetail(APIView):
    # atributos padrão
    #TODO: fazer uma validação de email decente
    def post(self, request, format=None):
        # Passo 1 - pegar a request
        serializer = AdocaoSerializer(data=request.data)
        # Passo 2 - validar body
        if serializer.is_valid():
            # Passo 2 - salvar no banco
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message": "Houverar erros de validação - formato de email inválido"
            }, status=HTTP_400_BAD_REQUEST)

