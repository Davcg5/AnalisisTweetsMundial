
import couchdb
import sys
import urllib2
import re
import json
from textblob import TextBlob
import os
import threading

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


with open('coordinates.csv', 'w') as csvfile:
    for x in d['rows']:
        hora = x ['key']
        a = x ['value']
        
        if a ['coordinates']:
            coord = a['coordinates']
            y = a['text']
        #x = re.sub("\W"," ",a) 
            if "#BRA" in y:
                
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
	

            if "#MEX" in y:
                
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})   
            if "#MEX" in y:
                    
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))}) 
            elif "RUSIA2018" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "BEL" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "BELGICA" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "BRASIL" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "BRASILEIRO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "RUSSIA2018" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "COPA" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            
            elif "WORLDCUP" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})    
            elif "GABRIEL JESUS" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})     
            elif "FERNANDINHO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "GOL" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})           

                
            elif "CANARINHA" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "NEYMAR" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "COUTINHO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "PAULINHO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "FIRMINHO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "MARCELO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "JOGO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "JOGAR" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "TITE" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "FUTEBOL" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "RONALDO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "MIRANDA" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "FAGNER" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "FILIPE" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "CASEMIRO" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "WILLIAN" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
            elif "QATAR" in y:
                mylist = str((y)).split("[")
                mylist2 = mylist[1].split(",")
                mylist3 = mylist2[1].split("]")
                fieldnames = ['lat', 'lon']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow({'lat': str ((mylist2[0])), 'lon': str ((mylist3[0]))})
                
            
            else:
                
                desechados = desechados +1;
                h.write(str((y.encode('utf-8')))+ "\n")
                
       
        
	

print (tweets)
print ("---------")
print (desechados)
