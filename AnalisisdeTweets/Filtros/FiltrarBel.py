
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



url = 'http://127.0.0.1:5984/belgica/_design/lenguaje/_view/belgica'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []

f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\lenguajeBel.txt","w")
h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirBel.txt","w")

for x in d['rows']:
    hora = x ['key']
    a = x ['value']
    y = a.upper()
    
	#x = re.sub("\W"," ",a) 
    if "#BRA" in y:
        
      
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
    if "#tHANKYOUBELGIUM" in y:
            
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1  

    if "RUSIA2018" in y:
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
    if "#BELGIUM" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "WORLDCUP2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WORLDCUP2018" in y:
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
    if "SEMIFINAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FINAL" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ENGLAND" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    
    if "#ENG" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FRANCE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "FRA" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BRONZE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "THIRD PLACE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BRAZIL" in y:
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
    if "#JPN" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "JAPON" in y:
	    
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
	
    if "JAPAN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1      
    if "BELVSJPN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1       
    if "BELVSENG" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "BELVSFRA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1               
    if "BRUSSELS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "FIFAWORLDCUP" in y:
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
    if "COMEBACK" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SOCCER" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "THIRD" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#GERMANY" in y:
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
    if "VERMAELEN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KOMPANY" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KANE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PICKFORD" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ON VA BELGICA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WE GAN BELGICA" in y:
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
