from bs4 import BeautifulSoup
from urllib.request import urlopen
from json import dump

nomes_revistas = []
precos_revistas = []
dados = []


class Livia:
    def __init__(self):
        self.url = None

    @staticmethod
    def registrar(caminho):
        with open(f'dados/{caminho}.json', 'w') as json_file:
            dump(dados, json_file, indent=4, ensure_ascii=False)
    
    def infantil(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for n, p in zip(nomes_revistas, precos_revistas):
            dd = {n: p}
            dados.append(dd)

        Livia.registrar('infantil')
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
        
    def adolescente(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for n, p in zip(nomes_revistas, precos_revistas):
            
            dd = {n: p}
            dados.append(dd)

        with open('dados/adolescente.json', 'w') as json_file:
            dump(dados, json_file, indent=4, ensure_ascii=False)
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
    
    def jovens(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for n, p in zip(nomes_revistas, precos_revistas):
            
            dd = {n: p}
            dados.append(dd)

        with open('dados/jovem.json', 'w') as json_file:
            dump(dados, json_file, indent=4, ensure_ascii=False)
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
    
    def adultos(self, url):
        self.url = url
        url = url

        response = urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')

        cards_produtos = soup.findAll('tr', {'class': 'GrupoxProduto'})
        cards_precos = soup.findAll('input', {'name': 'valor[]'})

        for produto in cards_produtos:
            nomes_revistas.append(produto.find('label').getText())

        for preco in cards_precos:
            precos_revistas.append(preco.get('value'))

        for n, p in zip(nomes_revistas, precos_revistas):
            
            dd = {n: p}
            dados.append(dd)

        with open('dados/adulto.json', 'w') as json_file:
            dump(dados, json_file, indent=4, ensure_ascii=False)
        
        print("Arquivo Criado!")
        
        nomes_revistas.clear()
        precos_revistas.clear()
        dados.clear()
