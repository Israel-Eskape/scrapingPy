from bs4 import BeautifulSoup
import requests
import pandas as pd 

#prueba1  url = 'https://resultados.as.com/resultados/futbol/primera/'
url = 'https://acordes.lacuerda.net/en_espiritu_y_en_verdad/rey_humilde-2.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#letra
#prueba1 le = soup.find_all('span', class_= 'nombre-equipo')
le = soup.find_all('div', id= 't_body')

#print (le)

letra = list()

for i in le:
    letra.append(i.text)
    
letra  = "".join(letra)
print(letra)