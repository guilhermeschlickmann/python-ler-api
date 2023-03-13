import csv
import json

import requests

import conecta_bd
import filme_banco
from config import params_api
from Filme import *

res = ''
url = ''

try:
    url = params_api['url']
    params = {'api_key': params_api['api_key']}
    res = requests.get(url,params=params)
except Exception as error:
    print(str(error))

jsonString = json.dumps(res.json())
filmes = json.loads(jsonString)

lista_filmes = []

#print(filmes['results'][0]['original_title'])

resultado = filmes['results'].copy()

#carrega apenas elementos desejados do dicionario 
for x in range(len(resultado)):   

    #print(filmes['results'][x]['original_title'])
    filme = Filme()
    filme.adult = resultado[x]['adult']
    filme.backdrop_path = resultado[x]['backdrop_path']
    filme.genre_ids = resultado[x]['genre_ids']
    filme.original_language = resultado[x]['original_language']
    filme.original_title = resultado[x]['original_title']
    filme.overview = resultado[x]['overview']
    filme.popularity = resultado[x]['popularity']
    filme.poster_path = resultado[x]['poster_path']
    filme.release_date = resultado[x]['release_date']
    filme.title = resultado[x]['title']
    filme.video = resultado[x]['video']
    filme.vote_average = resultado[x]['vote_average']
    filme.vote_count = resultado[x]['vote_count']

    lista_filmes.append(filme)

print(len(lista_filmes))

filme1 = lista_filmes[1]

print(filme1.original_title)

#salvar no banco de dados

conn = conecta_bd.conecta()

id = filme_banco.insere_filme(conn,filme1)


#busca filmes do banco de dados
dados = filme_banco.lista_filmes(conn)


#cria arquivo csv
cabecalho = ['id','adult','backdrop_path','original_language','original_title','overview,popularity',
          'poster_path','release_date','title,video','vote_average','vote_count']

with open('filmes.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(cabecalho)
    writer.writerows(dados)




print(f"id: {id}")

