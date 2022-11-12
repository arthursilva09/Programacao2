from django.urls import path

from api.views import ProdutosList, VendasList


urlpatterns = [
    path('produtos/', ProdutosList.as_view(), name='api-produtos'),
    path('vendas/', VendasList.as_view(), name='api-vendas'),
]
