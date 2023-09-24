# -*- coding: utf-8 -*-

print('Ein Herzliches Willkommen an beide Teams zum heutigen Quiz! \n')
punkt1 = 0 #die gasammten Punkte von Gruppe 1
punkt2 = 0 #die gasammten Punkte von Gruppe 2


#Gruppe 1 Frage 1
print('Die erste Frage geht an Gruppe 1:')
print('Wie viel ist 2 hoch 3? (1Punkt)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')
sicher1 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

#Bonus Part - Sind Sie sicher?
if sicher1 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')

#Überprufung der Antwort
if ant == '8' :
    print('Richtig! Gruppe 1 bekommt 1 Punkt.')
    punkt1 = punkt1 + 1
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 8')
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')


#Gruppe 2 Frage 1
print('Die erste Frage geht an Gruppe 2:')
print('Wie viel ist 3 hoch 2? (1Punkt)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')

#Bonus Part - Sind Sie sicher?
sicher2 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

if sicher2 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')
    
#Überprufung der Antwort   
if ant == '9' :
    print('Richtig! Gruppe 2 bekommt 1 Punkt.')
    punkt2 = punkt2 + 1
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 9')
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
    
#Gruppe 1 Frage 2
print('Die zweite Frage geht an Gruppe 1:')
print('Wie viele Meter ergeben einen Kilometer? (2 Punkte)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')

sicher3 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

if sicher3 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')
    
#Überprufung der Antwort    
if ant == '1000' :
    print('Richtig! Gruppe 1 bekommt 2 Punkt.')
    punkt1 = punkt1 + 2
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 1000.')
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')

#Gruppe 2 Frage 2
print('Die zweite Frage geht an Gruppe 2:')
print('Wie viele Gram ergeben einen Kilogram? (2 Punkte)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')

sicher4 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

if sicher4 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')
    
#Überprufung der Antwort
if ant == '1000' :
    print('Richtig! Gruppe 2 bekommt 2 Punkt.')
    punkt2 = punkt2 + 2
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 1000.')
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
    
#Gruppe 1 Frage 3
print('Die dritte Frage geht an Gruppe 1:')
print('Wie viele Nullpunkte von f(x)=x^4 + 7x^3 - 2x - 4 ? (3 Punkte)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')

sicher5 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

if sicher5 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')

#Überprufung der Antwort    
if ant == '2' :
    print('Richtig! Gruppe 1 bekommt 3 Punkt.')
    punkt1 = punkt1 + 3
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 2.')
    print('Gruppe 1 hat bisher ' + str(punkt1) + ' Punkte. \n')
    
#Gruppe 2 Frage 3
print('Die dritte Frage geht an Gruppe 2:')
print('Wie viele Nullpunkte von f(x)=12x^3 + 5x^2 - 4x +16 ? (3 Punkte)')
ant = input('Was ist die Antwort? Schreiben Sie der Antwort. \n')

sicher6 = input('Sind Sie sicher? Wollen Sie Ihre Antwort ändern? Typen 1 für ja oder 2 für nein.\n')

if sicher6 == '2':
    ant = input('Schreiben Sie der neue Antwort. \n')

#Überprufung der Antwort    
if ant == '1' :
    print('Richtig! Gruppe 2 bekommt 3 Punkt.')
    punkt2 = punkt2 + 3
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
else:
    print('Das war leider falsch! Die richtige Antwort ist 1.')
    print('Gruppe 2 hat bisher ' + str(punkt2) + ' Punkte. \n')
    
#Ende
print('Fertig')
print ('Gruppe 1 hat', str(punkt1), 'Punkte.')
print ('Gruppe 2 hat', str(punkt2), 'Punkte.')

print('Gewonnen hat.....***Trommelwirbel***')

#Wer ist der Sieger
if punkt1 > punkt2:
    print('Gruppe 1. Herzlichen Glückwunsch!!!')
elif punkt2 > punkt1:
    print('Gruppe 2. Herzlichen Glückwunsch!!!')
else:
    print('Beide Gruppen. Herzlichen Glückwunsch!!!')