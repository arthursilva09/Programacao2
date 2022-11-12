from django.contrib import admin
from webform.models import Cliente, Funcionario, Venda, Produto
import csv
from django.http import HttpResponse
import codecs
from django.contrib import messages
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Venda)
admin.site.register(Produto)

# class ExportCsvMixin:
#     def export_as_csv(self, request, queryset):

#         meta = self.model._meta
#         field_names = [field.name for field in meta.fields]

#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
#         writer = csv.writer(response)

#         writer.writerow(field_names)
#         for obj in queryset:
#             row = writer.writerow([getattr(obj, field) for field in field_names])

#         return response

#     export_as_csv.short_description = "Exportar csv selecionados"

# class AgendamentoAdmin(admin.ModelAdmin,ExportCsvMixin):
#   list_display=('cnpj', 'unidade', 'curso','dia_curso','horario_curso', 'vagas_solicitadas', 'vagas_aceitas', 'vagas_restantes')
#   readonly_fields=('vagas_solicitadas', 'data_agendamento', 'data_atualizacao', 'razao_social', 'nome_fantasia',
#               'cnpj', 'estado', 'cidade', 'bairro', 'logradouro', 'complemento',
#               'numero', 'telefone_fixo', 'telefone_celular', 'whatsapp',
#               'ramo_atividade', 'fpas', 'unidade', 'cidade_curso', 'curso', 'dias', 'horario', 
#               'uuid_curso', 'termos_privacidade')
#   list_filter = ('unidade', 'curso', 'dias')
#   search_fields=('nome_fantasia',)
#   date_hierarchy='data_agendamento'
#   actions = ['export_as_csv']
  
#   def vagas_restantes(self,obj):
#     return obj.curso.vagas_ofertadas
  
#   def dia_curso(self,obj):
#     return obj.curso.dias
  
#   def horario_curso(self,obj):
#     return obj.curso.horario

#   def save_model(self, request, obj, form, change):
#     if change:
#       curso = Curso.objects.get(uuid=obj.uuid_curso)
#       agendamento = Agendamento.objects.get(id=obj.id)
#       diferenca = int(agendamento.vagas_aceitas) - int(obj.vagas_aceitas)
#       if diferenca < 0:
#         if curso.vagas_ofertadas >= abs(diferenca):
#           curso.vagas_ofertadas += diferenca
#           curso.save()
#         else:
#           obj.vagas_aceitas = agendamento.vagas_aceitas
#           obj.save()
#           messages.error(request, 'Não há vagas suficientes para essa demanda.')
#       else:
#         curso.vagas_ofertadas += diferenca
#         curso.save()
#       super(AgendamentoAdmin, self).save_model(request, obj, form, change)
        
# admin.site.register(Agendamento, AgendamentoAdmin)


# class CursoAdmin(admin.ModelAdmin):
#   list_filter = ('unidade', 'nome')
#   list_display=('id' ,'nome', 'unidade', 'vagas_ofertadas', 'dias', 'horario', 'disp')
#   def save_model(self, request, obj, form, change):
#     if change:
#       if obj.vagas_ofertadas == 0:
#         obj.disp = False
#     super(CursoAdmin, self).save_model(request, obj, form, change)

# admin.site.register(Curso, CursoAdmin)


# class UnidadeAdmin(admin.ModelAdmin):
#   list_filter = ('nome', 'cidade')
#   list_display=('nome', 'cidade')

# admin.site.register(Unidade, UnidadeAdmin)

# admin.site.register(Cidade)
