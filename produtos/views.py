from django.shortcuts import render

#Importando módulos REST
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#importando modelos
from .models import Produto
from .serializers import ProdutoSerializer
#Importando serializers 
# Create your views here

class ProdutosAPIView(APIView):
    """
    API de Produtos
    """

    def get(self, request):
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({"msg": "Criou com sucesso!"},serializer.data, status=status.HTTP_201_CREATED)


