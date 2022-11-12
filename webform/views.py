import uuid
from django.shortcuts import render, redirect
from webform.forms.produtos_form import ProdutoForm, VendaForm
from webform.models import Produto, Venda

from django.contrib import messages
from .service import curso_service

from django.conf import settings
import requests

# Create your views here.

def login(request):
  return render(request, 'webform/login.html')

def home(request):
  return render(request, 'webform/home.html')

def consultar_produtos(request):
  return render(request, 'webform/consultar_prod.html')

def cadastrar_produtos(request):
  if request.method == "POST":
    form = ProdutoForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Puroduto salvo com scesso!')
  else:
    form = ProdutoForm()
  return render(request, 'webform/form.html', {'form': form})

def editar_produto(request, id):
  produto = Produto.objects.get(id=id)
  if request.method == "POST":
    form = ProdutoForm(request.POST, instance=produto)
    if form.is_valid():
      form.save()
      messages.success(request, 'Produto editado com sucesso!')
  else:
    form = ProdutoForm(instance=produto)
  return render(request, 'webform/form.html', {'form': form})

def deletar_produto(request, id):
  produto = Produto.objects.get(id=id)
  produto.delete()
  return redirect('produtos')

def consultar_vendas(request):
  vendas = Venda.objects.all()
  return render(request, 'webform/consultar_vendas.html', {'vendas': vendas})

def cadastrar_vendas(request):
  return render(request, 'webform/vender.html')

def forma_pagamento(request, valor):
  valor = float(valor)
  if request.method == "POST":
    form = VendaForm(request.POST)
    if form.is_valid():
      post = form.save(commit=False)
      post.valor_total = valor
      post.save()
      messages.success(request, 'Venda salva com sucesso!')
      return redirect('consultar-vendas')
  else:
    form = VendaForm()
  return render(request, 'webform/form.html', {'form': form, 'valor': valor})

