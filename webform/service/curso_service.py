import requests
import json


def buscar_curso(unidade):
  response = requests.get(
    f"http://127.0.0.1:8000/api/cursos/?unidade={unidade}"
  )
  return response.json()

def validar_cnpj(cnpj):
  digitos = ''
  aux_st = [5,4,3,2,9,8,7,6,5,4,3,2]
  aux_nd = [6,5,4,3,2,9,8,7,6,5,4,3,2]
  result = 0
  for i in range(len(aux_st)):
    result += (int(cnpj[i]) * aux_st[i])

  resto_st = result%11
  
  if resto_st<2:
    resto_st = 0
  else:
    resto_st = 11-resto_st

  result = 0
  for j in range(len(aux_nd)):
    result += int(cnpj[j]) * aux_nd[j]

  resto_nd = result%11
  if resto_nd < 2:
    resto_nd = 0
  else:
    resto_nd = 11-resto_nd

  digitos+=(f'{resto_st}{resto_nd}')

  if cnpj[12] == digitos[0] and cnpj[13] == digitos[1]:
    return True
  else:
    return False
