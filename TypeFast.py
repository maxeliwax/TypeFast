#Maximilian Walldov 
#TypeFast 
#teinf-20
#2022 VT

import time
import random

"""
Denna funktion läsen en fil och returnerar en lista med ord

Args:
Filnamn (string) Namn på filen som skall läsa
"""
def get_word_list(f):# en funktion som läser in filen f och returnerar en lista med ord
    a = open(f, "r", encoding="utf8")#https://www.w3schools.com/python/python_file_open.asp
    return a.readlines()


"""
Denna funktion skriver ut välkomstmeddelande 

Args:
"""
def welcome():
    print()
    print()
    print("Welcome to Fasttype")
    print()

"""
Denna funktion räknar ned i ett antal sekunder 

Args:
Antal sekunder (int)
"""
def countdown(r):# nedräkning i r sekunder, https://www.programiz.com/python-programming/time
    for t in range(r):#loop
        a=r-t
        print (str(a) + "...")
        time.sleep(1)# väntar en sekund
    print()

"""
Denna funktion jämför två strängar och returnerar antal skillnader

Args:
Sträng_1 (string)
Sträng_2 (string)

Return:
Antal skillnader (int)
"""
def check_word(inp, wo): # jämför varje bokstav i två strängar, känd bugg jämför endast samma position, klarar inte förskjutning
    l = min(len(inp), len(wo))# utgår från den kortaste strängen 
    fel = 0
    for t in range(l-1):
        if inp[t] != wo[t]:
            fel = fel+1
    return fel

"""
Denna funktion skriver ut en summering av resultat

Args:
Antal fel (int)
Tid i sekunder (int)
Antal ord (int)
Ord per minut (int)

"""
def summary(f, t, ws, wpm):
    print ("--------------------------")
    print ("Antal fel:" + str(f))
    print ("Tid:" + str(t))
    print ("Antal ord:" + str(ws))
    print ("Ord per minut:" + str(wpm))
    print ("--------------------------")


# Här börjar programmet

words = get_word_list("TypeThis.txt") # Hämtar lista med ord
random.shuffle(words)# slumpvis ordning på meningarna, https://www.w3schools.com/python/ref_random_shuffle.asp


welcome()


# huvudloop
for x in words: # för varje mening i filen
    input("Tryck enter")
    countdown(3)# nedräkning
    print("Skriv:")
    print(x)# skriv ut mening

    timed = time.time()# spara undan tid 
    text = input()# skriv in ord
    timed = round(time.time()-timed, 2)# jämföra tiden med tiden man sparade undan

    if text == "": # om inget skrivet lämna huvudloopen
        break
   
    fel = check_word(text,x)# räkna fel
    ws = len(text.split())# räkna antal ord
    wpm = round((60/timed)*ws)# räkna ord per minut
    summary(fel,timed,ws,wpm)# skriva ut resultat

print()
print("Tack och adjö")