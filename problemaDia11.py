import bs4
import requests

#CRear la url sin numero
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos ok
titulos_ranking_alto = []

#iterar paginas
for pagina in range(1,51):

    # crear sopa en cada pagina
    base = url_base.format(pagina)
    resultado = requests.get(base)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')
    print(f'pagina numrero {pagina} -- {base}')

    #seleccionar datos de los libros revisando la clase product pod
    libros = sopa.select('.product_pod')
    for libro in libros:

        #chequear que tenga 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:


            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            # Agregar libro a la lista
            titulos_ranking_alto.append(titulo_libro)

for r in titulos_ranking_alto:
    print(r)