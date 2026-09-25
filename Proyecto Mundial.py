import random # Uso de libreria random para la generacion de goles aleatorios
SEL = [
    "Brasil",
    "Francia",
    "Argentina",
    "Alemania",
    "España",
    "Inglaterra",
    "Portugal",
    "Bélgica",
    "Países Bajos",
    "Italia",
    "Croacia",
    "Uruguay",
    "México",
    "Estados Unidos",
    "Japón",
    "Marruecos",
]

def enumeracion(indice, lista): # Funcion que da los equipos en forma de lista
    print(f"{lista}. {SEL[indice]}")
"""Acomodo de las selecciones en forma de una lista enumerada"""

# Funcion para la pregunta de cuantos minuts duro el partido de cierta fase
def pregunta(fase, numero):
    return int(input(f"\nElige los minutos que quieres que dure 
    el partido de {fase} {numero} (90 o 120): "))
"""Pregunta para decidir si se fue a tiempos extra el partido"""

enumeracion(0, 1)
enumeracion(1, 2)
enumeracion(2, 3)
enumeracion(3, 4) # Uso de funcion enumeracion
enumeracion(4, 5)
enumeracion(5, 6)
enumeracion(6, 7)
enumeracion(7, 8)
enumeracion(8, 9)
enumeracion(9, 10)
enumeracion(10, 11)
enumeracion(11, 12)
enumeracion(12, 13)
enumeracion(13, 14)
enumeracion(14, 15)                # Las funciones se puden simplificar con un ciclo for

# Llamamos la funcion de pregunta
mins_octavos_1 = pregunta("octavos", 1)
mins_octavos_2 = pregunta("octavos", 2)
mins_octavos_3 = pregunta("octavos", 3)
mins_octavos_4 = pregunta("octavos", 4)
mins_octavos_5 = pregunta("octavos", 5)
mins_octavos_6 = pregunta("octavos", 6)
mins_octavos_7 = pregunta("octavos", 7)
mins_octavos_8 = pregunta("octavos", 8)

mins_cuartos_1 = pregunta("cuartos", 1)
mins_cuartos_2 = pregunta("cuartos", 2)
mins_cuartos_3 = pregunta("cuartos", 3)
mins_cuartos_4 = pregunta("cuartos", 4)

mins_semis_1 = pregunta("semis", 1)
mins_semis_2 = pregunta("semis", 2)

ganadores = []
for i in range(0, len(SEL), 2):
    e1 = SEL[i]
    e2 = SEL[i + 1]
    print(f"Partido: {e1} vs {e2}")
    opcion_ganador = int(input("\nIngresa 1 o 2 para escoger al ganador\n"))

    if opcion_ganador == 1:
        goles_ganador = random.randint(1, 5)
        goles_perdedor = random.randint(0, goles_ganador - 1)
        print(f"\nEl marcador final es: {goles_ganador} - {goles_perdedor} Favor {e1}\nPartido: {e1} vs {e2}")
        ganadores.append(e1)
    elif opcion_ganador == 2:
        goles_ganador = random.randint(1, 5)
        goles_perdedor = random.randint(0, goles_ganador - 1)
        print(f"\nEl marcador final es: {goles_perdedor} - {goles_ganador} Favor {e2}\nPartido: {e1} vs {e2}")
        ganadores.append(e2)

    input("\nPresiona Enter para continuar...")

# Operacion de los minutos totales de las fases
octavos = (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8) / 8
cuartos = (c1 + c2 + c3 + c4) / 4
semis = (s1 + s2) / 2

#  Resultados
print("\nLa fase de octavos sumando sus partidos dura un total de: ", octavos)
print("La fase de cuartos sumando sus partidos dura un total de: ", cuartos)
print("La fase de semis sumando sus partidos dura un total de: ", semis)

# Mejor optimizado si se usara ciclos y condicionales
