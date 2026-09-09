sel = ["Brasil", "Francia", "Argentina", "Alemania", "España", "Inglaterra", "Portugal", "Bélgica", "Países Bajos", "Italia", "Croacia", "Uruguay", "México", "Estados Unidos", "Japón", "Marruecos"]

def enumeracion(n,lista): # Funcion que da los equipos en forma de lista
    print(f"{lista}. {sel[n]}")

# Funcion para la pregunta de cuantos minuts duro el partido de cierta fase
def pregunta(fase, numero):
    return int(input(f"\nElige los minutos que quieres que dure el partido de {fase} {numero} (90 o 120): "))

enumeracion(0,1)
enumeracion(1,2)
enumeracion(2,3)
enumeracion(3,4) # Uso de funcion enumeracion
enumeracion(4,5)
enumeracion(5,6)
enumeracion(6,7)
enumeracion(7,8)
enumeracion(8,9)
enumeracion(9,10)
enumeracion(10,11)
enumeracion(11,12)
enumeracion(12,13)
enumeracion(13,14)
enumeracion(14,15)                # Las funciones se puden simplificar con un ciclo for

# Llamamos la funcion de pregunta
p1 = pregunta("octavos", 1)
p2 = pregunta("octavos", 2)
p3 = pregunta("octavos", 3)
p4 = pregunta("octavos", 4)
p5 = pregunta("octavos", 5)
p6 = pregunta("octavos", 6)
p7 = pregunta("octavos", 7)
p8 = pregunta("octavos", 8)

c1 = pregunta("cuartos", 1)
c2 = pregunta("cuartos", 2)
c3 = pregunta("cuartos", 3)
c4 = pregunta("cuartos", 4)

s1 = pregunta("semis", 1)
s2 = pregunta("semis", 2)

# Operacion de los minutos totales de las fases
octavos = (p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8) / 8
cuartos = (c1 + c2 + c3 + c4) / 4
semis = (s1 + s2) / 2

#  Resultados
print("\nLa fase de octavos sumando sus partidos dura un total de: ", octavos)
print("La fase de cuartos sumando sus partidos dura un total de: ", cuartos)
print("La fase de semis sumando sus partidos dura un total de: ", semis)

# Mejor optimizado si se usara ciclos y condicionales
