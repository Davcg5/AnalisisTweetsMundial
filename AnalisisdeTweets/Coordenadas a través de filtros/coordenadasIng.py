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



url = 'http://127.0.0.1:5984/inglaterra/_design/coordenadas/_view/inglaterra'
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
with open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\coordenadasIng.csv", 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in d['rows']:
        lineas = 0
        coordenada = str((x ['key']))
        a = x ['value']
        y= a.upper()
    
        if "#ENG" in y:
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
        if "#INGLATERRA" in y:
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

        if "#WC2018" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "GOAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1

        if "GARETH SOUTHGATE" in y:
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
        if "CUARTOS DE FINAL" in y:
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
        if "ERIC DIER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OLSON" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "JANSSON" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "ARIAS" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "BACCA" in y:
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
        if "#ITSNOTCOMINGHOME" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FOURTPLACE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "KYLE WALKER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "RASHFORD" in y:
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
        if "TRIPPIER" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "PENALTIES" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        
        if "SEMI-FINAL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1      
        if "QUARTER-FINAL" in y:
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
        if "#ENGVSCOL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1   
        if "#CROVSENG" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1 
        if "#ENGVSSWE" in y:
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
        if "ENGLAND" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#ENGLAND" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "INGLATERRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "INGLATERRA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "OSPINA" in y:
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
        if "#THREELIONS" in y:
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
        if "GOD SAVE THE QUEEN" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#ITSCOMINGHOME" in y:
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
        if "#SOCCER" in y:
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
        if "#SWE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "FALCAO" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "YERRY MINA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "JAMES" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "LARSSON" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "DELE ALLI" in y:
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
        if "LINGARD" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "STERLING" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "KANE" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#COL" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "COLOMBIA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#GRACIASCOLOMBIA" in y:
            if "None" not in coordenada:
                mylist = str((coordenada)).split("[")
                
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                writer.writerow({'lat': str ((mylist3[0])), 'lon': str ((mylist2[0]))})
                conc = conc +1
            else : 
                sinc= sinc +1
        if "#SWE" in y:
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
        if "SWEDEN" in y:
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
            
f.write("Inglaterra \n" "con coordenadas activadas: " + str((conc))+"no activadas: " +str((sinc)))
f.close()        
csvfile.close()
        