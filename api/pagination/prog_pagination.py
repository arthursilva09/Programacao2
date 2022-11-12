from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class VendasPagination(PageNumberPagination):
    page_size = 19

    def get_paginated_response(self, data):
        return Response({
            'vendas': data,
        })

class ProdutosPagination(PageNumberPagination):
    page_size = 5

    def get_paginated_response(self, data):
        return Response({
            'produtos': data,
        })
