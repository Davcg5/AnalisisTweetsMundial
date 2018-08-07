
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



url = 'http://127.0.0.1:5984/brasil/_design/fecha/_view/brasil'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []

f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\fechasBra.txt","w")
h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirBra.txt","w")

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
    if "#MEX" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    elif "RUSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "#FIFAWORLDCUP" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "NEY" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "#MEX" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1 
    elif "#BEL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "MEXICO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "BELGICA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "BELGIUM" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1   
    elif "DE BRUYNE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    elif "LUKAKU" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  
    elif "HAZARD" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1         
    elif "BEL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "BELGICA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "BRASIL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "BRASILEIRO" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "RUSSIA2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "COPA" in y:
	    
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
	
    elif "WORLDCUP" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1      
    elif "GABRIEL JESUS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1       
    elif "FERNANDINHO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "GOL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1               

	 	 
    elif "CANARINHA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "NEYMAR" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "COUTINHO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "PAULINHO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "FIRMINHO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "MARCELO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "JOGO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "JOGAR" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "TITE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "FUTEBOL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "RONALDO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "MIRANDA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "FAGNER" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "FILIPE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "CASEMIRO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "WILLIAN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    elif "QATAR" in y:
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
    if "VERMAELEN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KOMPANY" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#BELGIQUE" in y:
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
    if "BRUYNE" in y:
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
