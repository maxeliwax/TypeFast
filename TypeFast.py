#Maximilian Walldov 
#TypeFast 
#teinf-20
#2022 VT

import time
import random

def GetWordlist(f):# en funktion som läser in filen f och får tillbaka en lista med ord
    a = open(f, "r", encoding="utf8")#https://www.w3schools.com/python/python_file_open.asp
    return a.readlines()


def Welcome():
    print()
    print()
    print("Welcome to Fasttype")
    print()

def Countdown(r):# nedräkning i r sekunder, https://www.programiz.com/python-programming/time
    for t in range(r):#loop
        a=r-t
        print (str(a) + '...')
        time.sleep(1)# väntar en sekund
    print()


def CheckWord(inp,wo): # jämför varje bokstav i två strängar, känd bugg jämför endast samma position, klarar inte förskjutning
    l= min(len(inp),len(wo))# utgår från den kortaste strängen 
    fel = 0
    for t in range(l-1):
       if inp[t] != wo[t]:
            fel = fel+1
    return fel

def Summary(f,t,ws,wpm):
    print ("--------------------------")
    print ("Antal fel:" + str(fel))
    print ("Tid:" + str(timed))
    print ("Antal ord:" + str(ws))
    print ("Ord per minut:" + str(wpm))
    print ("--------------------------")


#Här börjar programmet

Words = GetWordlist("TypeThis.txt") #Hämtar lista med ord
random.shuffle(Words)#slumpvis ordning på meningarna, https://www.w3schools.com/python/ref_random_shuffle.asp


Welcome()


#huvudloop
for x in Words: #för varje mening i filen
    input("Tryck enter")
    Countdown(3)#nedräkning
    print("Skriv:")
    print(x)#skriv ut mening

    timed = time.time()#spara undan tid 
    text=input()#skriv in ord
    timed = round(time.time() - timed, 2)#jämföra tiden med tiden man sparade undan

    if text == '': #om inget skrivet lämna huvudloopen
        break
   
    fel = CheckWord(text,x)#räkna fel
    ws=len(text.split())# räkna antal ord
    wpm= round((60/timed)*ws)#räkna ord per minut
    Summary(fel,timed,ws,wpm)#skriva ut resultat

print()
print("Tack för du spelat")

