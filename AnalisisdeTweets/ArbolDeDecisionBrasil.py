import couchdb
import sys
import urllib2
import re
import json
from textblob import TextBlob
import os
import threading
import csv

regex = re.compile(r'[A-za-z0-9]+')
tweets = 0
desechados = 0
from couchdb import view


URL = 'localhost'
db_name = 'croacia'


'''========couchdb'=========='''
server = couchdb.Server('http://localhost:5984/')  #('http://245.106.43.184:5984/') poner la url de su base de datos
try:
    #print db_name
    db = server[db_name]
    print 'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()



url = 'http://127.0.0.1:5984/brasil/_design/coordenadas/_view/brasil'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []
fieldnames = ['lat', 'lon']
conc = 0 
sinc = 0 
f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\coordenadasporPais.txt","w")
#h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirRus.txt","w")
with open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\coordenadasBra.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in d['rows']:
        lineas = 0
        coordenada = str((x ['key']))
        a = x ['value']
        y= a.upper()
    
        if "#BRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MEX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RUSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FIFAWORLDCUP" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "NEY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MEX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "#BEL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "MEXICO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "BELGIUM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "DE BRUYNE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "LUKAKU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "HAZARD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1       
        if "BEL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "BRASIL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "BRASILEIRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "RUSSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "COPA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "WORLDCUP" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "GABRIEL JESUS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "FERNANDINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "GOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CANARINHA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "NEYMAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "COUTINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1     
        if "PAULINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "FIRMINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "MARCELO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1               
  
        if "JOGO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "JOGAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "TITE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "FUTEBOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RONALDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MIRANDA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FAGNER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FILIPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "CASEMIRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "WILLIAN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "QATAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "LAYUN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "HERRERA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "FUTBOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1    
        if "OSORIO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "NEYMAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "CARLOS VELA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RAUL JIMENEZ" in y:
                          
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "HIRVING" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "SALCEDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FILIPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ALVAREZ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "DOS SANTOS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "#BRAVSMEX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FELLAINI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "JANUZAJ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1    
        if "BATSHUAYI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "VERMAELEN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "KOMPANY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "#BELGIQUE" in y:
                      
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "LUKAKU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "MERTENS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "BRUYNE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        else:

            pass
            
f.write("con coordenadas activadas: " + str((conc))+"no activadas: " +str((sinc)))
f.close()        
csvfile.close()
        