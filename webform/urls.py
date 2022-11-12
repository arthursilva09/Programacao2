from django.urls import path
from .views import login, home, consultar_produtos, cadastrar_produtos, editar_produto, deletar_produto, consultar_vendas, cadastrar_vendas, forma_pagamento
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", login, name="login"),
    path("home/", home, name="home"),
    path("produtos/", consultar_produtos, name="produtos"),
    path("produtos/cadastrar/", cadastrar_produtos, name="cadastrar-produtos"),
    path("produtos/editar/<int:id>", editar_produto, name="editar-produto"),
    path("produtos/deletar/<int:id>", deletar_produto, name="deletar-produto"),
    path("vendas/", consultar_vendas, name="consultar-vendas"),
    path("vendas/cadastrar/", cadastrar_vendas, name="cadastrar-venda"),
    path("vendas/forma_pagamento/<str:valor>", forma_pagamento, name="forma-pagamento-vendas"),
    path("api-token-auth/", obtain_auth_token, name="api_token_auth")
]


