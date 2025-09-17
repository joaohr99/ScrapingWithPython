import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'

# Faz a requisição HTTP e obtém o conteúdo da página que eu precisar
response = requests.get(url)

# Código que cria um objeto BeautifulSoup para analisar o HTML
soup = BeautifulSoup(response.text, 'html.parser')

titulos = soup.find_all('h3')

for titulo in titulos:
    nome_livro = titulo.find('a')['title']
    print(nome_livro)
