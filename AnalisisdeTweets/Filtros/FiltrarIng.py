
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



url = 'http://127.0.0.1:5984/inglaterra/_design/lenguaje/_view/inglaterra'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []

f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\lenguajeIng.txt","w")
h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirIng.txt","w")

for x in d['rows']:
    hora = x ['key']
    a = x ['value']
    y = a.upper()
    
	#x = re.sub("\W"," ",a) 
    if "#ENG" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "#FRANCE" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#INGLATERRA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PENALTI" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1


    if "MODRIC" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "VIDA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "RAKITIC" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MANDZUKIC" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PERISIC" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#VAR" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1


    if "#BEL" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1    
    if "BELGICA" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1 
    if "#THANKYOUBELGIUM" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  

    if "RUSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "RUSSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUPRUSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MUNDIAL2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1   
    if "BELGIUM" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    if "NATIONAL TEAM" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1 
    if "#WORLDCUPWINNER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FIFA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUPFEVER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "#CROATIANPRIDE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#HRVATSKA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#CRO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#CROACIA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "#WC2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GOAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "GARETH SOUTHGATE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1   
    if "#BELGIUM" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "WORLDCUP2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUP" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "WORLDCUP" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#COPAMUNDIAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "COPA DEL MUNDO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "OCTAVOS DE FINAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CUARTOS DE FINAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUP2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ERIC DIER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "OLSON" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    
    if "JANSSON" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ARIAS" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BACCA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GOLD" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#ITSNOTCOMINGHOME" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FOURTPLACE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KYLE WALKER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "RASHFORD" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FIFAWORLDCUP" in y:
        x = re.sub("\W"," ",y) 
    	
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BRUYNE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "HAZARD" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#COURTOIS" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "GOALKEEPER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "TRIPPIER" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PENALTIES" in y:
	    
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
	
    if "SEMI-FINAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1      
    if "QUARTER-FINAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1       
    if "#FRAVSARG" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#ENGVSCOL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1   
    if "#CROVSENG" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1  
    if "#ENGVSSWE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1              
    if "BRUSSELS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "ENGLAND" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "#ENGLAND" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "INGLATERRA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "INGLATERRA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "OSPINA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "FIFA WORLD CUP" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "#FIFAWORLDCUP" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "#BELGIQUE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUPLIVE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FIFACOM" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "LUKAKU" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MERTENS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#THREELIONS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SOCCER" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GOD SAVE THE QUEEN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#ITSCOMINGHOME" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#GERMANY" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#SOCCER" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FOOTBALL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FELLAINI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "JANUZAJ" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BATSHUAYI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUPFINAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#SWE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FALCAO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "YERRY MINA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "JAMES" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "LARSSON" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "DELE ALLI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "WHAT A GOAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FIFA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "LINGARD" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "STERLING" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KANE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#COL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "COLOMBIA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#GRACIASCOLOMBIA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#SWE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SUECIA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SWEDEN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
        
        
     
    else:
        
        desechados = desechados +1;
        h.write(str((hora))+ "  ,"+str((y.encode('utf-8')))+ "\n")
        
       
        
	
h.close()	
f.close()
print (tweets)
print ("---------")
print (desechados)
