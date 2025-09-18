import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

url = 'http://books.toscrape.com/'

lista_de_livros = []

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    livros = soup.find_all('article', class_='product_pod')

    print(f"Foram encontrados {len(livros)} livros na página.")
    print("-" * 30)

    # Extração de Dados dos Livros
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').text
        nota = livro.find('p', class_='star-rating')['class'][1]

        dados_do_livro = {
            'Title': titulo,
            'Price': preco,
            'Reputation': nota
        }

        lista_de_livros.append(dados_do_livro)

    proxima_pagina = soup.find('li', class_='next')

    if proxima_pagina:
        link_proxima_pagina = proxima_pagina.a['href']
        url = urljoin(url, link_proxima_pagina)
    else:
        break

df = pd.DataFrame(lista_de_livros)
df.to_csv('livros_raspados.csv', index=False, encoding='utf-8')

print("Extração de dados concluída!")
print(f"Os dados foram salvos em um arquivo chamado 'livros_raspados.csv'")
#Codigo Finalizado
