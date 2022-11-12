from django.db import models

# Create your models here.

class Cliente(models.Model):
  nome = models.CharField(max_length=80, null=False, blank=False)
  cnpj = models.CharField(max_length=14, null=True, blank=False)
  cpf = models.CharField(max_length=11, null=True, blank=False)
  cnpj = models.CharField(max_length=11, null=False, blank=False)
  logradouro = models.CharField(max_length=120, null=False, blank=False)
  estado = models.CharField(max_length=80, null=False, blank=False)
  fone = models.CharField(max_length=80, null=False, blank=False)

  def __str__(self):
    return self.nome

class Funcionario(models.Model):
  nome = models.CharField(max_length=80, null=False, blank=False)
  cpf = models.CharField(max_length=11, null=True, blank=False)
  cnpj = models.CharField(max_length=11, null=False, blank=False)
  logradouro = models.CharField(max_length=120, null=False, blank=False)
  estado = models.CharField(max_length=80, null=False, blank=False)
  fone = models.CharField(max_length=80, null=False, blank=False)

  def __str__(self):
    return self.nome

class Venda(models.Model):
  FORMAS_PAGAMENTOS = [
    ('Especie', 'Especie'),
    ('Cartão Crédito', 'Cartão Crédito'),
    ('Cartão Débito', 'Cartão Débito'),
  ]

  data_venda = models.DateTimeField(null=True, blank=False, auto_now_add=True)
  cliente = models.CharField(null=False, blank=False, max_length=80)
  forma_pagamento = models.CharField(max_length=80, null=False, blank=False, choices=FORMAS_PAGAMENTOS)
  valor_total = models.FloatField(null=False, blank=False)
  valor_pago = models.FloatField(null=False, blank=False)
  def __str__(self):
    return self.cliente

class Produto(models.Model):
  nome = models.CharField(max_length=80, null=False, blank=False)
  barras = models.CharField(max_length=11, null=True, blank=False)
  preco = models.FloatField(null=False, blank=False)

  def __str__(self):
    return self.nome
