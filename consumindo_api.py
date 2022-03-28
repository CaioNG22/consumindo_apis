import requests
import io

"""""""""""
url = 'https://viacep.com.br/ws/'
cep = '30140071'
formato = '/xml/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print('XML : ', r.text)
    print()
else:
    print('Nao houve sucesso na requisicao.')
""""""
""""""
for cep in range(1,6):
    url = 'https://viacep.com.br/ws/'
    ceps = (f'3014007{cep}')
    formato ='/json/'

    r = requests.get(url+ceps+formato)

    r = r.json()

    lugar = r['localidade'], r['bairro']
   
    print(lugar)

"""
"""'

url = 'https://viacep.com.br/ws/'
estado = 'MG/'
cidade = 'Belo Horizonte/'
rua = 'Rua dos Aimores'
formato ='/json/'

r = requests.get(url+estado+cidade+rua+formato)

r = r.json()

   
print(r)

"""

""""
import requests
url = 'https://viacep.com.br/abc/'
cep = '30140071'
formato = '/json/'
r = requests.get(url + cep + formato)
if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print(r.status_code)
    print('Nao houve sucesso na requisicao.')

"""

"""""

5)

r = requests.get('http://www.google.com/search', params={'q':
'Protocolo HTTP'})
if (r.status_code == 200):
    print()
    print('Retorno : ', r.text)    
   
else:
    print('Nao houve sucesso na requisicao.')

with io.open('arquivo.txt', "w", encoding="utf-8") as file:
    file.write(str(r.text))
    
"""
