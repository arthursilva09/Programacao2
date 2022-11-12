from django import forms
from webform.models import Produto, Venda


class ProdutoForm(forms.ModelForm):
  class Meta:
    model = Produto
    fields = "__all__"

class VendaForm(forms.ModelForm):
  class Meta:
    model = Venda
    exclude = ('valor_total',)


# class AprendizagemForm(forms.ModelForm):
#   cnpj = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00.000.000/0000-00'}))
#   telefone_fixo = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 0000-0000'}))
#   telefone_celular = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))
#   whatsapp = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00) 00000-0000'}))
#   fpas = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000'}))
  
#   class Meta:
#     model = Agendamento
#     exclude = ('uuid_curso', 'vagas_aceitas')

#   def clean_cnpj(self):
#     cnpj = self.cleaned_data['cnpj']
#     return cnpj.replace('.', '').replace('/', '').replace('-', '')

#   def clean_telefone_fixo(self):
#     if self.cleaned_data['telefone_fixo']:
#       telefone_fixo = self.cleaned_data['telefone_fixo']
#       return telefone_fixo.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
  
#   def clean_telefone_celular(self):
#     telefone_celular = self.cleaned_data['telefone_celular']
#     return telefone_celular.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

#   def clean_whatsapp(self):
#     whatsapp = self.cleaned_data['whatsapp']
#     return whatsapp.replace('(', '').replace(')', '').replace(' ', '').replace('-', '')

#   def save(self, commit=True):
#     instance = super(AprendizagemForm, self).save(commit=False)
#     # Colocando os dados em uppercase
#     instance.razao_social = instance.razao_social.upper()
#     instance.nome_fantasia = instance.nome_fantasia.upper()
#     instance.cidade = instance.cidade.upper()
#     instance.bairro = instance.bairro.upper()
#     instance.logradouro = instance.logradouro.upper()
#     instance.ramo_atividade = instance.ramo_atividade.upper()


#     unidade = Unidade.objects.get(nome=instance.unidade)
#     curso = Curso.objects.get(nome=instance.curso, unidade=unidade, dias=instance.dias, horario=instance.horario)
#     instance.curso = curso
#     instance.uuid_curso = curso.uuid
#     instance.save()
  