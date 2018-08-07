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



url = 'http://127.0.0.1:5984/rusia/_design/coordenadas/_view/rusia'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []
fieldnames = ['lat', 'lon']
conc = 0 
sinc = 0 
f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\coordenadasporPais.txt","a")
#h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirRus.txt","w")
with open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\coordenadasRus.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in d['rows']:
        lineas = 0
        coordenada = str((x ['key']))
        a = x ['value']
        y= a.upper()
    
        if "#FRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ARGENTINA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#ARGENTINA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "PENALTI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#ARG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MESSI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MERCADO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ARMANI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "TAGLIAFICO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MASCHERANO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MUSLERA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GIMENEZ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GODIN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MODRIC" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "VIDA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RAKITIC" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MANDZUKIC" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "PERISIC" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#VAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1

        if "KUN" in y:
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
        if "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#THANKYOUBELGIUM" in y:
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
        if "RUSSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUPRUSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MUNDIAL2018" in y:
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
        if "NATIONAL TEAM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUPWINNER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FIFA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUPFEVER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FIERESDETREBLEUS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#CROATIANPRIDE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#HRVATSKA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#CRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#CROACIA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#BLEUBLANCROUGE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WC2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#VOLIMHRAVATSKU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1

        if "#EQUIPEDEFRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "#BELGIUM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "WORLDCUP2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUP" in y:
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
        if "#COPAMUNDIAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "COPA DEL MUNDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OCTAVOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CUARTOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CAVANI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "SUAREZ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "URUGUAY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#URU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GOLD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CHAMPIONS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "WORLD CHAMPIONS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CHAMPIONS DU MONDE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1

        if "SEMIFINAL" in y:
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
        if "BRUYNE" in y:
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
        if "#COURTOIS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GOALKEEPER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MESSI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ARGENTINA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#ARG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1      
        if "FRAVSCRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1      
        if "#FRAVSARG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#BELVSFRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "#FRAVSBEL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "#FRAVSURU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1            
        if "BRUSSELS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "LEOMESSI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FIFA WORLD CUP" in y:
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
        if "#BELGIQUE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUPLIVE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FIFACOM" in y:
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
        if "COMEBACK" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "SOCCER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "VIVE LA FRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#VIVELAFRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#GERMANY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FOOTBALL" in y:
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
        if "#WORLDCUPFINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "VARANE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "UMTITI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "LLORIS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GRIEZMANN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "PAVARD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "WHAT A GOAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#FIFA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OWN GOAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MBAPPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MBAPPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#KANTE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "KANTE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
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
        if "#MEX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        elif "RUSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "#FIFAWORLDCUP" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "NEY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "#MEX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "#BEL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "MEXICO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "BELGIUM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        elif "DE BRUYNE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "LUKAKU" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        elif "HAZARD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1       
        elif "BEL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "BRASIL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "BRASILEIRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "RUSSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "COPA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        elif "WORLDCUP" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1     
        elif "GABRIEL JESUS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1      
        elif "FERNANDINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "GOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1              

            
        elif "CANARINHA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "NEYMAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "COUTINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "PAULINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "FIRMINHO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "MARCELO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "JOGO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "JOGAR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "TITE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "FUTEBOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "RONALDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "MIRANDA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "FAGNER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "FILIPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "CASEMIRO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "WILLIAN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        elif "QATAR" in y:
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
        if "MEXICO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#GRACIASMEXICO" in y:
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
        if "#RUSIA2018" in y:
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
        if "#RUSSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#SELECCIONMEXICANA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MEXICOPRESENTE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CIELITOLINDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#GRACIASKOREA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#MUNDIAL2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#COPAMUNDIAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "COPA DEL MUNDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OCTAVOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CUARTOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ALEMANIA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "SUECIA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "MISELECCIONMX" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "2X0" in y:
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
        if "GIO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FUERA OSORIO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "KOREA" in y:
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
        if "CH14" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "YOSOY8A" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#VAMOSMEXICO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1

        if "LOZANO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#CHUKYLOZANO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MUNDIAL2018" in y:
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
        if "CHICHARITO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1      
        if "MARQUEZ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RAFA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1               
        if "PARTIDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CRUZ AZUL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GUARDADO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OCHOA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MEMO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#NOERAPENAL" in y:
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
        if "#BRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#POL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#POLAND" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#LEWANDOWSKI" in y:
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
        if "BELGICA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#THANKYOUBELGIUM" in y:
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
        if "#WORLDCUPRUSIA2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "MUNDIAL2018" in y:
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
        if "NATIONAL TEAM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "#BELGIUM" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "WORLDCUP2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#WORLDCUP2018" in y:
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
        if "#COPAMUNDIAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "COPA DEL MUNDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OCTAVOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "CUARTOS DE FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "SEMIFINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ENGLAND" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#ENG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "FRANCE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "FRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "BRONZE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "THIRD PLACE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "NEXT ROUND" in y:
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
        
        if "BRUYNE" in y:
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
        
        if "#COURTOIS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "GOALKEEPER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#JPN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "JAPON" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        
        if "JAPAN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
           
        if "#BELVSJPN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
             
        if "#BELVSENG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#BELVSFRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
                      
        if "BRUSSELS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "FIFAWORLDCUP" in y:
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
        
        if "COMEBACK" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "SOCCER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "THIRD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#GERMANY" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#FOOTBALL" in y:
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
        
        if "SAMURAI BLUE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "JFA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "KAGAWA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "OKAZAKI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "HONDA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "AKIRA NISHINO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "#INUI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1






        if "#POR" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "#CR7" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "CRISTIANO RONALDO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1                 
        if "PEPE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1         
        if "#ESP" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
  
        if "REAL MADRID" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1     
        if "BARCELONA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1  
        if "SPAIN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
 
        if "SPAIN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1                 
        if "DE GEA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1         
        if "LOPETEGUI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "RAMOS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1     
        if "ALBA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "BUSQUETS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "DIEGO COSTA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1                 
        if "VASQUEZ" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1         
        if "ASENSIO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "INIESTA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1         
        if "KOKE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "ASPAS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "AKINFEEV" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1                 
        if "#SUI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1         
        if "SHAKIRI" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "SWITZERLAND" in y:
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
            
f.write("Rusia \n" "con coordenadas activadas: " + str((conc))+"no activadas: " +str((sinc)))
f.close()        
csvfile.close()
        