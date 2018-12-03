#Prueba de scraping con Python v0.000000000000000000000000001
#Creditos a Brian (por si es ilegal esto)
#Solo para fines académicos

from bs4 import BeautifulSoup
import urllib.request
from requests import get
import re

urlcate = 'https://www.ricardorodriguez.cl/'  #url base
htmlcate = urllib.request.urlopen(urlcate) 

soupcate = BeautifulSoup(htmlcate)
categoria = soupcate.findAll('li', {'class':'lx'}) #busca las categorias
descarga = []

for id in categoria:
    idcat = id.find('a').get('href').replace('/categoria.aspx?cat=','') #extrae la id de la categoría
    cate = id.find('a').text
    urlarti = 'https://www.ricardorodriguez.cl/categoria.aspx?cat=' + idcat #genera la dirección con cada id encontrada
    htmlarti = urllib.request.urlopen(urlarti)
    souparti = BeautifulSoup(htmlarti)
    articulo = souparti.findAll('div', {'class':'calloutContent'}) #busca los articulos de una categoría
    print('descargando categoría ... ' + cate )
    
    for art in articulo:
        arti = art.find('span').text.split('Codigo: #')[0]
        codigo = art.find('span').text.split('Codigo: #')[1].strip()
        precio = art.find('span', {'class':'productItemPrice'}).text.replace('$','').replace('.','')
        imagen = 'https://www.ricardorodriguez.cl' + art.find('a').contents[0].get('src')
        descarga.append([idcat, cate, codigo, arti, precio, imagen])
        
with open("detalle1.csv", 'w', newline='', encoding='utf-8') as carga: #crea archivo con cabeceras y datos descargados
    writer = csv.writer(carga)
    writer.writerow(['id categoría', 'categoría', 'código artículo', 'descripción artículo', 'precio', 'imagen'])
    writer.writerows(descarga)
    print('Archivo creado !')
