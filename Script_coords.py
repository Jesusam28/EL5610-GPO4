# Script para determinar el tiempo a una parada

# ---------- Librerias ----------
import math
import pandas as pd

# ---------- Coord actual ----------

#lat = int(input("Latitud de su coordenada"))
lat = 9.855053
#long = int(input("Longitud de su coordenada"))
long = -83.910603

# ---------- Marcadores ----------

# P1 Parada Diseño
P1_lat = 0.171980189
P1_long = -1.464444794
# P2 Parada Electronica
P2_lat = 0.171995059
P2_long = -1.464455213
# P3 Parada G18
P3_lat = 0.171998061
P3_long = -1.464493558
# P4 Parada Mante
P4_lat = 0.172003053
P4_long = -1.464515584
# P5 Parada Biblioteca
P5_lat = 0.171996019
P5_long = -1.464559863
# P6 Parada Principal
P6_lat = 0.172020087
P6_long = -1.464569253
# P7 Entrada del TEC
P7_lat = 0.172057298
P7_long = -1.464562376
# P8 Parada Cartago Centro
P8_lat = 0.172147584
P8_long = -1.464688075

# ---------- Conversion a radianes ----------

lat_rad = math.radians(lat)
long_rad = math.radians(long)

# ---------- Calculos ----------

# ---------- Distancias ----------
D_P1 = math.acos(math.sin(lat_rad)*math.sin(P1_lat) + math.cos(lat_rad)*math.cos(P1_lat)*math.cos(P1_long - long_rad))*6371
D_P2 = math.acos(math.sin(lat_rad)*math.sin(P2_lat) + math.cos(lat_rad)*math.cos(P2_lat)*math.cos(P2_long - long_rad))*6371
D_P3 = math.acos(math.sin(lat_rad)*math.sin(P3_lat) + math.cos(lat_rad)*math.cos(P3_lat)*math.cos(P3_long - long_rad))*6371
D_P4 = math.acos(math.sin(lat_rad)*math.sin(P4_lat) + math.cos(lat_rad)*math.cos(P4_lat)*math.cos(P4_long - long_rad))*6371
D_P5 = math.acos(math.sin(lat_rad)*math.sin(P5_lat) + math.cos(lat_rad)*math.cos(P5_lat)*math.cos(P5_long - long_rad))*6371
D_P6 = math.acos(math.sin(lat_rad)*math.sin(P6_lat) + math.cos(lat_rad)*math.cos(P6_lat)*math.cos(P6_long - long_rad))*6371
D_P7 = math.acos(math.sin(lat_rad)*math.sin(P7_lat) + math.cos(lat_rad)*math.cos(P7_lat)*math.cos(P7_long - long_rad))*6371
D_P8 = math.acos(math.sin(lat_rad)*math.sin(P8_lat) + math.cos(lat_rad)*math.cos(P8_lat)*math.cos(P8_long - long_rad))*6371

# ---------- Tiempos ----------

# ---------- Horas ----------
T_P1_5 = D_P1 / 5
T_P1_15 = D_P1 / 15
T_P1_25 = D_P1 / 25

T_P2_5 = D_P2 / 5
T_P2_15 = D_P2 / 15
T_P2_25 = D_P2 / 25

T_P3_5 = D_P3 / 5
T_P3_15 = D_P3 / 15
T_P3_25 = D_P3 / 25

T_P4_5 = D_P4 / 5
T_P4_15 = D_P4 / 15
T_P4_25 = D_P4 / 25

T_P5_5 = D_P5 / 5
T_P5_15 = D_P5 / 15
T_P5_25 = D_P5 / 25

T_P6_5 = D_P6 / 5
T_P6_15 = D_P6 / 15
T_P6_25 = D_P6 / 25

T_P7_5 = D_P7 / 5
T_P7_15 = D_P7 / 15
T_P7_25 = D_P7 / 25

T_P8_5 = D_P8 / 5
T_P8_15 = D_P8 / 15
T_P8_25 = D_P8 / 25

# ---------- Minutos ----------
T_P1_5m = T_P1_5 * 60
T_P1_15m = T_P1_15 * 60
T_P1_25m = T_P1_25 * 60

T_P2_5m = T_P2_5 * 60
T_P2_15m = T_P2_15 * 60
T_P2_25m = T_P2_25 * 60

T_P3_5m = T_P3_5 * 60
T_P3_15m = T_P3_15 * 60
T_P3_25m = T_P3_25 * 60

T_P4_5m = T_P4_5 * 60
T_P4_15m = T_P4_15 * 60
T_P4_25m = T_P4_25 * 60

T_P5_5m = T_P5_5 * 60
T_P5_15m = T_P5_15 * 60
T_P5_25m = T_P5_25 * 60

T_P6_5m = T_P6_5 * 60
T_P6_15m = T_P6_15 * 60
T_P6_25m = T_P6_25 * 60

T_P7_5m = T_P7_5 * 60
T_P7_15m = T_P7_15 * 60
T_P7_25m = T_P7_25 * 60

T_P8_5m = T_P8_5 * 60
T_P8_15m = T_P8_15 * 60
T_P8_25m = T_P8_25 * 60

# ---------- Segundos ----------
T_P1_5s = T_P1_5m * 60
T_P1_15s = T_P1_15m * 60
T_P1_25s = T_P1_25m * 60

T_P2_5s = T_P2_5m * 60
T_P2_15s = T_P2_15m * 60
T_P2_25s = T_P2_25m * 60

T_P3_5s = T_P3_5m * 60
T_P3_15s = T_P3_15m * 60
T_P3_25s = T_P3_25m * 60

T_P4_5s = T_P4_5m * 60
T_P4_15s = T_P4_15m * 60
T_P4_25s = T_P4_25m * 60

T_P5_5s = T_P5_5m * 60
T_P5_15s = T_P5_15m * 60
T_P5_25s = T_P5_25m * 60

T_P6_5s = T_P6_5m * 60
T_P6_15s = T_P6_15m * 60
T_P6_25s = T_P6_25m * 60

T_P7_5s = T_P7_5m * 60
T_P7_15s = T_P7_15m * 60
T_P7_25s = T_P7_25m * 60

T_P8_5s = T_P8_5m * 60
T_P8_15s = T_P8_15m * 60
T_P8_25s = T_P8_25m * 60

# ---------- Tablas ----------

# Tabla de distancias

distancias = pd.DataFrame({
    'Parada': ['Parada Diseño', 'Parada Electronica', 'Parada G18', 'Parada Mantenimiento', 'Parada Biblioteca', 'Parada Principal', 'Entrada del TEC', 'Parada Cartago Centro'],
    'Distancia (km)': [D_P1, D_P2, D_P3, D_P4, D_P5, D_P6, D_P7, D_P8]
    })

# Tabla de Tiempos
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
tiempos = pd.DataFrame({
    'Parada':['Parada Diseño', 'Parada Electronica', 'Parada G18', 'Parada Mantenimiento', 'Parada Biblioteca', 'Parada Principal', 'Entrada del TEC', 'Parada Cartago Centro'],
    'Tiempo (5 kph)[h]':[T_P1_5, T_P2_5, T_P3_5, T_P4_5, T_P5_5, T_P6_5, T_P7_5, T_P8_5],
    'Tiempo (15 kph)[h]':[T_P1_15, T_P2_15, T_P3_15, T_P4_15, T_P5_15, T_P6_15, T_P7_15, T_P8_15],
    'Tiempo (25 kph)[h]':[T_P1_25, T_P2_25, T_P3_25, T_P4_25, T_P5_25, T_P6_25, T_P7_25, T_P8_25]
    })

# Tabla de Tiempos (minutos)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
tiempos_min = pd.DataFrame({
    'Parada':['Parada Diseño', 'Parada Electronica', 'Parada G18', 'Parada Mantenimiento', 'Parada Biblioteca', 'Parada Principal', 'Entrada del TEC', 'Parada Cartago Centro'],
    'Tiempo (5 kph)[h]':[T_P1_5m, T_P2_5m, T_P3_5m, T_P4_5m, T_P5_5m, T_P6_5m, T_P7_5m, T_P8_5m],
    'Tiempo (15 kph)[h]':[T_P1_15m, T_P2_15m, T_P3_15m, T_P4_15m, T_P5_15m, T_P6_15m, T_P7_15m, T_P8_15m],
    'Tiempo (25 kph)[h]':[T_P1_25m, T_P2_25m, T_P3_25m, T_P4_25m, T_P5_25m, T_P6_25m, T_P7_25m, T_P8_25m]
    })

# Tabla de Tiempos (segundos)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
tiempos_seg = pd.DataFrame({
    'Parada':['Parada Diseño', 'Parada Electronica', 'Parada G18', 'Parada Mantenimiento', 'Parada Biblioteca', 'Parada Principal', 'Entrada del TEC', 'Parada Cartago Centro'],
    'Tiempo (5 kph)[h]':[T_P1_5s, T_P2_5s, T_P3_5s, T_P4_5s, T_P5_5s, T_P6_5s, T_P7_5s, T_P8_5s],
    'Tiempo (15 kph)[h]':[T_P1_15s, T_P2_15s, T_P3_15s, T_P4_15s, T_P5_15s, T_P6_15s, T_P7_15s, T_P8_15s],
    'Tiempo (25 kph)[h]':[T_P1_25s, T_P2_25s, T_P3_25s, T_P4_25s, T_P5_25s, T_P6_25s, T_P7_25s, T_P8_25s]
    })
# ---------- Prints ----------

def menu():
    print("Opciones \n 1. Tutorial \n 2. Valores de rastreo")
    opcion = input("Opción de visualización")
    if opcion == "1":
        print("\nSus coordenadas actuales son: " +str(lat), ", " +str(long) ,"\n")
        print("Para determinar la distancia, primero se debe hacer el cambio a radianes de las coordenadas.")
        print("Coordenadas actuales (en radianes): " + str(lat_rad), ", " + str(long_rad))
        print("\nAhora, se determina la distancia en kilometros mediante la formula:")
        print("ACOS(SENO(lat1)*SENO(lat2)+COS(lat1)*COS(lat2)*COS(long2-long1))*6371")
        print("\nAplicando esta formula, se obtiene el siguiente resultado, respecto a cada parada determinada")
        print(distancias)
        print("\nCon las distancias calculadas, se determina el tiempo que le tomará al transporte el llevar a las distintas paradas.")
        print("Debido a las leyes de tránsito interno en el campus, la velocidad máxima es de 25kph")
        print("\nSe realizarán los estudios de tiempo de forma lineal para las velocidades de 5kph, 15 kph y 25 kph")
        print("---------- Tabla de Tiempos en Horas ----------")
        print(tiempos)
        print("\nSe adjuntas las variantes de tiempos para minutos y segundos.")
        print("\n---------- Tabla de Tiempos en Minutos ----------")
        print(tiempos_min)
        print("\n---------- Tabla de Tiempos en Segundos ----------")
        print(tiempos_seg,"\n")
        return menu()
    elif opcion == "2":
        print("\nCoordenada actual: " +str(lat), ", " +str(long))
        print("\n---------- Distancias ----------")
        print(distancias)
        print("\n---------- Tabla de Tiempos en Horas ----------")
        print(tiempos)
        print("\n---------- Tabla de Tiempos en Minutos ----------")
        print(tiempos_min)
        print("\n---------- Tabla de Tiempos en Segundos ----------")
        print(tiempos_seg, "\n")
        return menu()
    elif opcion == "s":
        return
    else:
        print("\nOpcion no disponible \n")
        return menu()

k = menu()
