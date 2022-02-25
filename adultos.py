from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

nomes_revistas = []
precos_revistas = []
dados = []

url = str(input('URL:'))

response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
cards_precos = soup.findAll('input', {'name': 'valor[]'})

for produto in cards_produtos:
    nomes_revistas.append(produto.find('label').getText())

for preco in cards_precos:
    precos_revistas.append(preco.get('value'))
    
#print(nomes_revistas)
#print(precos_revistas)

for n, p in zip(nomes_revistas, precos_revistas):
    #print(f'{n}: R${p}')
    dd = {}
    dd[n] = p
    dados.append(dd)

with open('adultos.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4 ,ensure_ascii=False)
