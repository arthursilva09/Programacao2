from pickletools import read_uint1
from django.shortcuts import render
from rest_framework.views import APIView
from api.service.produtos_service import listar_produtos_api
from api.service.vendas_service import listar_vendas_api
from api.serializer.prog_serializer import ProdutosSerializer, VendasSerializer
from api.pagination.prog_pagination import ProdutosPagination, VendasPagination
from rest_framework import permissions
from django.contrib.auth import login
# Create your views here.

class ProdutosList(APIView, ProdutosPagination):
  # permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, format=None):
    param_busca = self.request.query_params.get('barras', None)
    cursos = listar_produtos_api(param_busca)

    resultado = self.paginate_queryset(cursos, request)
    serializer = ProdutosSerializer(resultado, many=True, context={'request': request})
  
    return self.get_paginated_response(serializer.data)

class VendasList(APIView, VendasPagination):
  # permission_classes = (permissions.IsAuthenticated,)

  def get(self, request, format=None):
    param_busca = self.request.query_params.get('cliente', None)
    unidades = listar_vendas_api(param_busca)

    resultado = self.paginate_queryset(unidades, request)
    serializer = VendasSerializer(resultado, many=True, context={'request': request})
    
    return self.get_paginated_response(serializer.data)
    