
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



url = 'http://127.0.0.1:5984/mexico/_design/lenguaje/_view/mexico'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())


f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\lenguajeMex.txt","w")
h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirMex.txt","w")

for x in d['rows']:
    hora = x ['key']
    a = x ['value']
    y = a.upper()
    
	#x = re.sub("\W"," ",a) 
    if "#BRA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#MEX" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1    
    if "MEXICO" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1 
    if "#GRACIASMEXICO" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  

    if "RUSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#RUSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "RUSSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1   
    if "#RUSSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    if "#SELECCIONMEXICANA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    if "#MEXICOPRESENTE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CIELITOLINDO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#GRACIASKOREA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#MUNDIAL2018" in y:
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
    if "ALEMANIA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SUECIA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    
    if "MISELECCIONMX" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "2X0" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GOL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GIO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FUERA OSORIO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KOREA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FIFAWORLDCUP" in y:
        x = re.sub("\W"," ",y) 
    	
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CH14" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "YOSOY8A" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#VAMOSMEXICO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "LOZANO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#CHUKYLOZANO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MUNDIAL2018" in y:
	    
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
	
    if "WORLDCUP" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1      
    if "CHICHARITO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1       
    if "MARQUEZ" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "RAFA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1               
    if "PARTIDO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "CRUZ AZUL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "GUARDADO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "OCHOA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MEMO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#NOERAPENAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "LAYUN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "HERRERA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FUTBOL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "OSORIO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "NEYMAR" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CARLOS VELA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "RAUL JIMENEZ" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "HIRVING" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SALCEDO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FILIPE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ALVAREZ" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "DOS SANTOS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#BRAVSMEX" in y:
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
