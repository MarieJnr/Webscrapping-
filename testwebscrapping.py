# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:57:49 2022

@author: 22541
"""

import requests
from bs4 import BeautifulSoup

url ='https://fentybeauty.com/' 
reponse = requests.get(url)
print (reponse ) #affiche <Response [200]> si tout s'est bien passé

# print (reponse.text) affiche le contenu html de la page 
if reponse.ok: 
      soup=BeautifulSoup(reponse.text,'lxml')
      titre=soup.find('title')
      lis=soup.findAll('li') #Trouve tte les balises LI de la page
      for li in lis :
          a=li.find('a')
          link = a['href'] #Manque un if pour gerer les balises a qui ne contiennent pas de href
          links=[]
          links.append('https://fentybeauty.com/'+ link)
          print (links)
         