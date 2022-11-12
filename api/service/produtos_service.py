from webform.models import Produto
from django.db.models.query_utils import Q


def listar_produtos_api(param):
  if param == 'None':
    produtos = Produto.objects.all()
  else:
    try:
      produtos = Produto.objects.filter(barras=param).order_by('id')
    except Produto.DoesNotExist:
      return []
  
  return produtos
