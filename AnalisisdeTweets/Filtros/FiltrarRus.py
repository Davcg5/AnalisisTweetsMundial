
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



url = 'http://127.0.0.1:5984/rusia/_design/lenguaje/_view/rusia'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
data = {}
data ['people'] = []

f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\lenguajeRus.txt","w")
h = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\aTraducirRus.txt","w")

for x in d['rows']:
    hora = x ['key']
    a = x ['value']
    y = a.upper()
    
	#x = re.sub("\W"," ",a) 
    if "#FRA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ARGENTINA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#ARGENTINA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FRANCE" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PENALTI" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#ARG" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MESSI" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MERCADO" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ARMANI" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "TAGLIAFICO" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MASCHERANO" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MUSLERA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GIMENEZ" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GODIN" in y:
        
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

    if "KUN" in y:
        
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
    if "#FIERESDETREBLEUS" in y:
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
    if "#BLEUBLANCROUGE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#WC2018" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#VOLIMHRAVATSKU" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "#EQUIPEDEFRANCE" in y:
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
    if "CAVANI" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SUAREZ" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "URUGUAY" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    
    if "#URU" in y:
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
    if "GOLD" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CHAMPIONS" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "WORLD CHAMPIONS" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "CHAMPIONS DU MONDE" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1

    if "SEMIFINAL" in y:
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
    if "#MESSI" in y:
        x = re.sub("\W"," ",y) 
		
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "ARGENTINA" in y:
	    
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
	
    if "#ARG" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1      
    if "FRAVSCRO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1       
    if "#FRAVSARG" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#BELVSFRA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1   
    if "#FRAVSBEL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1  
    if "#FRAVSURU" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1              
    if "BRUSSELS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n") 
        tweets = tweets + 1
    if "LEOMESSI" in y:
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
    if "COMEBACK" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "SOCCER" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "VIVE LA FRANCE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#VIVELAFRANCE" in y:
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
    if "#WORLDCUPFINAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#FRA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "VARANE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "UMTITI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "LLORIS" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "GRIEZMANN" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "PAVARD" in y:
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
    if "OWN GOAL" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#MBAPPE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "MBAPPE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#KANTE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KANTE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
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
    if "#BRA" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#POL" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#POLAND" in y:
        
        x = re.sub("\W"," ",y) 
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#LEWANDOWSKI" in y:
        
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
    if "NEXT ROUND" in y:
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
    if "SAMURAI BLUE" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "JFA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "KAGAWA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "OKAZAKI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "HONDA" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "AKIRA NISHINO" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1
    if "#INUI" in y:
        x = re.sub("\W"," ",y)
        f.write(str((hora))+ "  ," + str((x)) + "\n")
        tweets = tweets + 1       
    
        if "#POR" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "#CR7" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1  
        if "CRISTIANO RONALDO" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1                  
        if "PEPE" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1          
        if "#ESP" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1  
  
        if "REAL MADRID" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1    
        if "BARCELONA" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1  
        if "SPAIN" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
 
        if "SPAIN" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1                 
        if "DE GEA" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1        
        if "LOPETEGUI" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "RAMOS" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1    
        if "ALBA" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "BUSQUETS" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "DIEGO COSTA" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1                 
        if "VASQUEZ" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1         
        if "ASENSIO" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "INIESTA" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1         
        if "KOKE" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "ASPAS" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "AKINFEEV" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1                 
        if "#SUI" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1         
        if "SHAKIRI" in y:
            x = re.sub("\W"," ",y)
            f.write(str((hora))+ "  ," + str((x)) + "\n")
            tweets = tweets + 1 
        if "SWITZERLAND" in y:
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
