# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:57:49 2022

@author: 22541
"""
import time 
import requests
from bs4 import BeautifulSoup


links=[]
url ='https://fentybeauty.com/' 
reponse = requests.get(url)
print (reponse ) #affiche <Response [200]> si tout s'est bien passé

# print (reponse.text) affiche le contenu html de la page 
if reponse.ok: 
      soup=BeautifulSoup(reponse.text,'lxml')
      titre=soup.find('title')
      lis=soup.findAll('li') #Trouve tte les balises LI de la page
      for li in lis :
          try: # Pour gerer les balises a n'ayant pas de href 
            a=li.find('a')
            link = a['href'] #Manque un if pour gerer les balises a qui ne contiennent pas de href
            links.append('https://fentybeauty.com/'+ link)
            print (links) 
          except:
             pass  
      time.sleep(3) #Enfin, nous devrions inclure cette ligne de code afin de pouvoir suspendre notre code pendant une seconde afin de ne pas envoyer de requêtes au site Web. Cela nous aide à ne pas être signalé comme spam.
print (len(links))# voir le nombre de href obtenu

with open ('urls.txt','w') as file : #Creer un fichier texte contenant tout les liens.
   for link in links :
    file.write( link + '\n')
    
with open ('urls.txt','r') as file : #Lire le fichier contenant ttles liens
   for row in file :
    print (row)
    """
    a terminer https://youtu.be/KdLkwBNtGsY
    """
       