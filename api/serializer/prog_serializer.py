from rest_framework import serializers
from webform.models import Produto, Venda


class ProdutosSerializer(serializers.ModelSerializer):
  class Meta:
    model = Produto
    fields = ('id','nome', 'barras', 'preco')

class VendasSerializer(serializers.ModelSerializer):
  class Meta:
    model = Venda
    fields = ('id','forma_pagamento', 'valor_total', 'valor_pago', 'cliente', 'data_venda')
