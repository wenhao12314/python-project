# -*- coding: utf-8 -*-


import random

## Diese Klasse stellt eine Karte dar.
#
# Eine Karte hat einen Wert und eine Farbe. Sie kann auch unsichtbar sein.
#
# @author Jens Dede, <jd@comnets.uni-bremen.de>
# @date May-2019
class Card():
    ## Wert für ein Kreuz
    CARD_COLOR_CLUB = "♣"

    ## Wert für ein Pik
    CARD_COLOR_SPADE = "♠"

    ## Wert für ein Herz
    CARD_COLOR_HEART = "♥"

    ## Wert für ein Karo
    CARD_COLOR_DIAMOND = "♦"

    ## Dieses Symbol wird bei unsichtbaren Karten zurückgegeben
    CARD_ICON_INVISIBLE = "■"


    ## Diese Liste enthält alle verfügbaren Kartenfarben
    CARD_COLORS = [
            CARD_COLOR_CLUB,
            CARD_COLOR_SPADE,
            CARD_COLOR_HEART,
            CARD_COLOR_DIAMOND
            ]

        ## Liste mit den Kartenwerten
    CARD_RANKS = [str(i) for i in range(2,11)] + ["J", "Q", "K", "A"]

    ## Der Konstruktor.
    #
    # Setzt den Wert und die Farbe für jede Karte. Die Karte kann auch
    # "unsichtbar" sein.
    #
    # @param color  Die Farbe der Karte
    # @param rank   Der Wert der Karte
    # @param visible Ist die Karte sichtbar? (Standardwert: True)
    #
    # @return   None
    def __init__(self, color, rank, visible=True):
        if color in Card.CARD_COLORS:
            self.__color = color
        else:
            raise ValueError(str(color) +\
                    " is not of type " + str(Card.CARD_COLORS))
        if str(rank) in Card.CARD_RANKS:
            self.__rank = rank
        else:
            raise ValueError(str(rank) +\
                    " is not of type " + str(Card.CARD_RANKS))
        self.__visible = visible

    ## Gibt die Farbe der Karte zurück.
    #
    # Piek, Karo, Herz, Kreuz
    #
    # @return   Die Farbe der Karte (Piek, Karo, Herz, Kreuz)
    def getColor(self):
        return self.__color

    ## Prüft, ob es sich um eine rote Karte handelt
    #
    # Gibt True zurück, wenn es sich um ein Herz oder ein Karo handelt
    #
    # @return   True, wenn Karo oder Herz, sonst False
    def isRed(self):
        return self.__color in [Card.CARD_COLOR_HEART, Card.CARD_COLOR_DIAMOND]

    ## Gibt den Wert der Karte zurück.
    #
    # @return Der Wert der Karte
    def getRank(self):
        return self.__rank

    ## String-Darstellung der Instanzen der Klasse.
    #
    # Dies erlaubt die Darstellung der Karte via print(cardInstance)
    #
    # @return   Die String-Darstellung der Karte
    def __repr__(self):
        # Nur sichtbare Karten werden angezeigt. Unsichtbare Karten werden
        # durch den Wert von CARD_ICON_INVISIBLE ersetzt.
        if self.__visible:
            return self.__color + self.__rank
        else:
            return 2*Card.CARD_ICON_INVISIBLE

    ## Vergleich: <
    #
    # Erlaubt den Vergleich zweier Instanzen via < (lt = less than)
    #
    # @return   True wenn <, sonst False
    def __lt__(self, other):
        return Card.CARD_RANKS.index(self.getRank()) <\
                Card.CARD_RANKS.index(other.getRank())

    ## Vergleich: <=
    #
    # Erlaubt den Vergleich zweier Instanzen via <= (le = less equal)
    #
    # @return   True wenn <=, sonst False
    def __le__(self, other):
        return Card.CARD_RANKS.index(self.getRank()) <=\
                Card.CARD_RANKS.index(other.getRank())

    ## Vergleich: >
    #
    # Erlaubt den Vergleich zweier Instanzen via > (gt, greater than)
    #
    # @return True, wenn >, sonst False
    def __gt__(self, other):
        return Card.CARD_RANKS.index(self.getRank()) >\
                Card.CARD_RANKS.index(other.getRank())

    ## Vergleich: >=
    #
    # Erlaubt den Vergleich zweier Instanzen via >= (ge, greater equal)
    #
    # @return True, wenn >=, sonst False
    def __ge__(self, other):
        return Card.CARD_RANKS.index(self.getRank()) >=\
                Card.CARD_RANKS.index(other.getRank())
                


    ## Setzt die Sichtbarkeit der Karte.
    #
    # @param visible    Sichtbarkeit der Karte
    #
    # @return None
    def setVisible(self, visible):
        self.__visible = visible

    ## Gibt die Sichtbarkeit der Karte zurück.
    #
    # @return True, wenn die Karte sichtbar ist, sonst False
    def getVisible(self):
        return self.__visible

    ## Statische Funktion, die ein Kartendeck erzeugt.
    #
    # Diese Funktion erzeugt komplette Kartendecks.
    #
    # @param num    Anzahl der zu erzeugenden Kartendecks. Standardwert: 1
    #
    # @return   Die Kartendecks
    @staticmethod
    def createCardDecks(self=0, num=1):
        cards = []
        for n in range(num):
            for c in Card.CARD_COLORS:
                for r in Card.CARD_RANKS:
                    cards.append(Card(c, r))
        return cards


###############################################################################
##########                  Das Spiel beginnt hier                   ##########
###############################################################################


## Implementieren Sie Ihren Code hier!

karten = Card.createCardDecks(104) #karten erzeugen
print(karten)

#zufällige Karten aus dem Decke
a= random.choice(karten)
b = random.choice(karten)
c = random.choice(karten)
d = random.choice(karten)
e = random.choice(karten)
f = random.choice(karten)
g = random.choice(karten)
h = random.choice(karten)
i = random.choice(karten)
j = random.choice(karten)
k = random.choice(karten)
l = random.choice(karten)
m = random.choice(karten)
n = random.choice(karten)
o = random.choice(karten)
p = random.choice(karten)


#unser Board als Listen
reihe1 = [a]
reihe2 = [b,c]
reihe3 = [d,e,f]
reihe4 = [g,h,i,j]
reihe5 = [k,l,m]
reihe6 = [n,p]
reihe7 = [o]

#print board
print("    ", reihe1)
print("  ", reihe2)
print(" ", reihe3)
print(reihe4)
print(" ",reihe5)
print("  ",reihe6)
print("    ", reihe7)
    

#unsichtbar machen
a= reihe1[0].setVisible(False)
b = Card.setVisible(b, False)
c = Card.setVisible(c, False)
d = Card.setVisible(d, False)
e = Card.setVisible(e, False)
f = Card.setVisible(f, False)
g = Card.setVisible(g, False)
h = Card.setVisible(h, False)
i = Card.setVisible(i, False)
j = Card.setVisible(j, False)
k = Card.setVisible(k, False)
l = Card.setVisible(l, False)
m = Card.setVisible(m, False)
n = Card.setVisible(n, False)
o = Card.setVisible(o, False)
p = Card.setVisible(p, False)


#Spiel beginnt
print("Herzlich Willkommen bei dem Spiel Busfahrer")

check = True #Shleife, ob Karte kein Person ist
while check :
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    
    
    #1. Runde
    print("Erste Runde. Decke eine Karte der ersten Reihe auf")
    karte = input("Welche Karte soll aufgedeckt werden?\n")


    Card.visible= reihe1[0].setVisible(True) #Karte sichtbar machen


    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)

    #Checken ob Karte eine Person ist
    if reihe1[0].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe1[0].getRank() == "J" :
        print("Pech gehabt!") 
        break
    if reihe1[0].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe1[0].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!") #keine Person, Spiel geht weiter


    #2. Runde
    print("Zweite Runde. Decke eine Karte der 2. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    if karte == 1:
        Card.visible= reihe2[0].setVisible(True)
    if karte == 2:
        Card.visible= reihe2[1].setVisible(True)
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    
    #checken ob Person ist
    if reihe2[karte-1].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe2[karte-1].getRank() == "J" :
        print("Pech gehabt!")
        break
    if reihe2[karte-1].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe2[karte-1].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!")

    #3. Runde
    print("Dritte Runde. Decke eine Karte der 3. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    if karte == 1:
        Card.visible= reihe3[0].setVisible(True)
    if karte == 2:
        Card.visible= reihe3[1].setVisible(True)
    if karte == 3:
        Card.visible= reihe3[2].setVisible(True)
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)

    if reihe3[karte-1].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe3[karte-1].getRank() == "J" :
        print("Pech gehabt!") 
        break
    if reihe3[karte-1].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe3[karte-1].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!")

    #4. Runde
    print("Vierte Runde. Decke eine Karte der 4. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    if karte == 1:
        Card.visible= reihe4[0].setVisible(True)
    if karte == 2:
        Card.visible= reihe4[1].setVisible(True)
    if karte == 3:
        Card.visible= reihe4[2].setVisible(True)
    if karte == 4:
        Card.visible= reihe4[3].setVisible(True)
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    if reihe4[karte-1].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe4[karte-1].getRank() == "J" :
        print("Pech gehabt!") 
        break
    if reihe4[karte-1].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe4[karte-1].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!")

    #5. Runde
    print("Fünfte Runde. Decke eine Karte der 5. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    if karte == 1:
        Card.visible= reihe5[0].setVisible(True)
    if karte == 2:
        Card.visible= reihe5[1].setVisible(True)
    if karte == 3:
        Card.visible= reihe5[2].setVisible(True)

    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    if reihe5[karte-1].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe5[karte-1].getRank() == "J" :
        print("Pech gehabt!")  
        break
    if reihe5[karte-1].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe5[karte-1].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!")



    #6. Runde
    print("Sechste Runde. Decke eine Karte der 6. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    if karte == 1:
        Card.visible= reihe6[0].setVisible(True)
    if karte == 2:
        Card.visible= reihe6[1].setVisible(True)
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    if reihe6[karte-1].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe6[karte-1].getRank() == "J" :
        print("Pech gehabt!")  
        break
    if reihe6[karte-1].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe6[karte-1].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Glück gehabt!")


    #7. Runde
    print("Siebte Runde. Decke eine Karte der 7. Reihe auf")
    karte = int(input("Welche Karte soll aufgedeckt werden?\n"))
    Card.visible= reihe7[0].setVisible(True)
    print("    ", reihe1)
    print("  ", reihe2)
    print(" ", reihe3)
    print(reihe4)
    print(" ",reihe5)
    print("  ",reihe6)
    print("    ", reihe7)
    if reihe7[0].getRank() == "A" :
        print("Pech gehabt!")
        break
    if reihe7[0].getRank() == "J" :
        print("Pech gehabt!") 
        break
    if reihe7[0].getRank() == "Q" :
        print("Pech gehabt!")
        break
    if reihe7[0].getRank() == "K" :
        print("Pech gehabt!")
        break
    else:
        print("Du hast gewonnen!")
              