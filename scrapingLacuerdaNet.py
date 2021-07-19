from bs4 import BeautifulSoup
import requests
import pandas as pd 

print("Nombre de la banda : ")
band = input()
print("Nombre de la canción : ")
song = input()

band = band.replace(' ','_')
song = song.replace(' ','_')

url = 'https://acordes.lacuerda.net/'+band+'/'+song+'.shtml'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

le = soup.find_all('div', id= 't_body')

letra = list()
for i in le:
    letra.append(i.text)
    
letra  = "".join(letra)
print(letra)