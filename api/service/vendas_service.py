from webform.models import Venda
from django.db.models.query_utils import Q


def listar_vendas_api(param):
  vendas = Venda.objects.all()

  return vendas
