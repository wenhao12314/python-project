#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

# Ziffern Liste erzeugen 1 bis 6
L1=random.randint(1,6)
L2=random.randint(1,6)
L3=random.randint(1,6)
L4=random.randint(1,6)
list_l=[L1,L2,L3,L4]
print(list_l)

#input von Spieler
Wahl1=int(input("Deine Wahl 1: "))
Wahl2=int(input("Deine Wahl 2: "))
Wahl3=int(input("Deine Wahl 3: "))
Wahl4=int(input("Deine Wahl 4: "))
Wahl=[Wahl1,Wahl2,Wahl3,Wahl4]
print(Wahl)

# check ob Ziffern korrekt ist
def check(list_l,Wahl):
#umzu checken ob wir sonst Variable sollen addieren, weil es kann 1 Nummer 2 mal vorkommt
    ver1=0 
    ver2=0 
    ver3=0 
    ver4=0 
    
    rp=0 # richtige Position
    sr=0 # sonst richtig
    
    #erste Ziffer checken
    if(list_l[0]==Wahl[0]):
        print(list_l[0])
        print(Wahl[0])
        if(ver1==0):
            ver1+=1
        rp+=1
    if(list_l[0]==Wahl[1]):
        print(list_l[0])
        print(Wahl[1])
        if(ver2==0):
            ver2+=1
            sr+=1
    if(list_l[0]==Wahl[2]):
        print(list_l[0])
        print(Wahl[2])
        if(ver3==0):
            ver3+=1
            sr+=1
    if(list_l[0]==Wahl[3]):
        print(list_l[0])
        print(Wahl[3])
        if(ver4==0):
            ver4+=1
            sr+=1
            
   #zweite Ziffer checken
    if(list_l[1]==Wahl[0]):
        print(list_l[1])
        print(Wahl[0])
        if(ver1==0):
            ver1+=1
            sr+=1
    if(list_l[1]==Wahl[1]):
        print(list_l[1])
        print(Wahl[1])
        if(ver2==0):
            ver2+=1
        rp+=1
    if(list_l[1]==Wahl[2]):
        print(list_l[1])
        print(Wahl[2])
        if(ver3==0):
            ver3+=1
            sr+=1    
    if(list_l[1]==Wahl[3]):
        print(list_l[1])
        print(Wahl[3])
        if(ver4==0):
            ver4+=1
            sr+=1
            
    #dritte Ziffer checken   
    if(list_l[2]==Wahl[0]):
        print(list_l[2])
        print(Wahl[0])
        if(ver1==0):
            ver1+=1
            sr+=1
    if(list_l[2]==Wahl[1]):
        print(list_l[2])
        print(Wahl[1])
        if(ver2==0):
            ver2+=1
            sr+=1
    if(list_l[2]==Wahl[2]):
        print(list_l[2])
        print(Wahl[2])
        if(ver3==0):
            ver3+=1
        rp+=1    
    if(list_l[2]==Wahl[3]):
        print(list_l[2])
        print(Wahl[3])
        if(ver4==0):
            ver4+=1
            sr+=1
            
     #vierte Ziffer checken 
    if(list_l[3]==Wahl[0]):
        print(list_l[3])
        print(Wahl[0])
        if(ver1==0):
            ver1+=1
            sr+=1
    if(list_l[3]==Wahl[1]):
        print(list_l[3])
        print(Wahl[1])
        if(ver2==0):
            ver2+=1
            sr+=1
    if(list_l[3]==Wahl[2]):
        print(list_l[3])
        print(Wahl[2])
        if(ver3==0):
            ver3+=1
            sr+=1    
    if(list_l[3]==Wahl[3]):
        print(list_l[3])
        print(Wahl[3])
        if(ver4==0):
            ver4+=1
        rp+=1     
      
        
    print(str(rp) + " richtige Position\n" +(str(sr) + " sonst richtig" ))
    #prüfen ob Spieler gewonnen hat
    if(rp==4):
        print("Du hast es geschafft !")
        return 0
    else:
        return 1

#läuft immer noch bis zum richtigen Antwort            
while check(list_l,Wahl):
    Wahl1=int(input("Deine Wahl 1: "))
    Wahl2=int(input("Deine Wahl 2: "))
    Wahl3=int(input("Deine Wahl 3: "))
    Wahl4=int(input("Deine Wahl 4: "))
    Wahl=[Wahl1,Wahl2,Wahl3,Wahl4]
    print(Wahl)
    if not check(list_l,Wahl): #wenn richtig, endet das Programm
        break