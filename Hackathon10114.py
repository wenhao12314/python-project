# -*- coding: utf-8 -*-

# importieren
import numpy as np
import matplotlib.pyplot as plt
import datetime

"""
PLOT
"""
# with open('2020_weather_temp', 'r') as csv_file:
csv_reader = np.genfromtxt('2020_weather_temp.csv',
                           delimiter=';', skip_header=1)

# Read the SONNENEINSTRAHLUNG data from the CSV file
solar_radiation = []

for row in csv_reader:
    solar_radiation.append((row[4]))

# Read the TIMESTAMP data from the CSV file
timestamp = []
for row in csv_reader:
    timestamp.append((row[0]))

nice_times = []  # Milisekunde zu Zeit zu benutzen
nice_time = [datetime.datetime.fromtimestamp(float(x)/1000.0)
             for x in timestamp]

# Read the REGEN data from the CSV file
regen = []
for row in csv_reader:
    regen.append((row[2]))


# PLOT ERSTELLEN
fig, ax = plt.subplots()

#Sonneneinstrahlung in grün
ax.plot(nice_time, solar_radiation, color='green',label = 'Sonneneinstrahlung')

# kritischen Wert Sonneneinstrahlung
ax.axhline(y=250, color='red')

# Regen mit gleiche x-Achse erstellen
ax2 = ax.twinx()
ax2.plot(nice_time, regen, color='blue',label = 'Regen')

#
solarlist = []
timelist = []

i = 0
for i in range(len(solar_radiation)):
    if solar_radiation[i] > 250:
        solarlist.append(400)
    else:
        solarlist.append(0)
       
ax.bar(nice_time,solarlist,color='darkred')

# X-Achsen Namen
ax.set_title('Mögliche Sendezeiten')
ax.set_xlabel('Zeit')

# Y-Achsen Namen
ax.set_ylabel('Sonneneinstrahlung (KJ/m^2)')
ax2.set_ylabel('Regen (mm/10min)')
ax.legend()
ax2.legend()

# PLOT PRINT
plt.show()


"""
WERTE AUSGEBEN 
"""
# Gemessener Zeitraum (Dauer in Stunden)
duration = (timestamp[-1] - timestamp[0]) / (3600*1000)
print(f'Die Gemessener Zeitraum in Stunden: {duration:.2f} Stunden')

# Gemessener Zeitraum (Dauer in Minuten)
duration_minut=duration*60
print(f'Die Gemessener Zeitraum in Minuten: {duration_minut:.0f} Minuten')

# Durchschnittliche Sonneneinstrahlung
Durchschnitt=np.mean(solar_radiation)
print(f'Die Durchschnittliche Sonneneinstrahlung ist gleich: {Durchschnitt:.2f}')

# Maximale Sonneneinstrahlung
maxi=np.max(solar_radiation)
print(f'Die Maximale Sonneneinstrahlung ist gleich: {maxi}')

# Maximale Regenmenge (in mm/10min)
max_Regen=np.max(regen)
print(f'Die Maximale Sonneneinstrahlung ist gleich: {max_Regen}')

# Regenmenge gesamt
gesamt_Regen=np.sum(regen)
print('Die gesamt Regenmenge ist gleich:',gesamt_Regen )
