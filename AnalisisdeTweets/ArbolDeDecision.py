
import couchdb
import sys
import urllib2
import re
import json
from textblob import TextBlob
import os
import threading

regex = re.compile(r'[A-za-z0-9]+')
positive = 0
negative = 0
neutral =0
from couchdb import view


f = open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\SentimientosBra.txt","w")

with open("C:\\Users\\davcg\\Desktop\\InteligenciaDeNegocios\\horasBra.txt", "r") as lineas:

    for linea in lineas:
        y=linea.split(",")[1]
        hora=y.split(",")[0]
        
        if "GANAMOS" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "GANAR" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "WIN" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "CAMPEON" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "CHAMPION" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "LOSE" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "DEFEAT" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "BACK HOME" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "SAD" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "CRYING" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "CRY" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "BOSTA" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "BOSTA" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "AMO" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "LOVE" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "VAMOS" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "TORCER" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "GO" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1
        elif "GOL" in y:
            sent = "positive"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            positive = positive + 1       
        elif "BYE" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "SHIT" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "BAD" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        elif "MAL" in y:
            sent = "negative"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            negative = negative + 1
        else: 
            sent = "neutral"
            f.write(str((sent))+ "  ," + str((y)) + "\n")
            neutral = neutral +1
    
print (positive)
print (negative)
print (neutral)
#.close()	
f.close()

