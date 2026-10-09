import random  #Librería random para generar los goles
 
SEL = [
    "Brasil", "Francia", "Argentina", "Alemania",
    "España", "Inglaterra", "Portugal", "Bélgica",
    "Países Bajos", "Italia", "Croacia", "Uruguay",
    "México", "Estados Unidos", "Japón", "Marruecos",
]
 
def enumeracion(indice, numero):
    """Imprime una selección con su número de lista."""
    print(f"{numero}. {SEL[indice]}")
 
def pregunta(fase, numero):
    """Pide la duración del partido (90 o 120 minutos) y la regresa."""
    mensaje = (f"\nElige los minutos que quieres que dure el partido de "
               f"{fase} {numero} (90 o 120): ")
    minutos = int(input(mensaje))
 
    #Se aseguro que solo si puedan asignar 90 o 120 mins
    if minutos != 90 and minutos != 120:
        print("Valor no válido, será de 90 minutos")
        minutos = 90
 
    return minutos
 
def jugar_partido(equipos):
    """Juega un partido entre dos equipos y regresa al ganador."""
    ganadores = []
    
    #Ciclo for (inicio, condicion, secuencia) Se empieza del 0 por como la lista es interpretada por python
    for i in range(0, len(equipos), 2): #len permite conocer cuantos datos en la lista
        e1 = equipos[i]
        e2 = equipos[i+1] #Selecciona los enfrentamientos
        print(f"\nPartido: {e1} vs {e2}")
        
        opcion = int(input("Ingresa 1 o 2 para escoger al ganador\n"))

        #Si se ingresa un número que no sea 1 o 2
        if opcion != 1 and opcion != 2:
            print("Opción no válida, gana el equipo 1 por defecto")
            opcion = 1
 
        goles_ganador = random.randint(1, 5)
        goles_perdedor = random.randint(0, goles_ganador - 1)
 
        #Decide al ganador y asigna sus goles
        if opcion == 1:
            print(f"Marcador final: {e1} {goles_ganador} - {goles_perdedor} {e2}")
            ganador = e1
        elif opcion == 2:
            print(f"Marcador final: {e1} {goles_perdedor} - {goles_ganador} {e2}")
            ganador = e2
            
        ganadores.append(ganador)
        input("\nPresiona Enter para continuar...")
 
    if len(ganadores) == 1:
        return ganadores[0]
        
    return ganadores
 
#Se muestra en consola los equipos seleccionados en forma de lista
print("\nSelecciones Participantes:")
for i, equipo in enumerate(SEL, start=1): #Funcion enumerate(forma facil de realizar una lista sin un contador)
    print(f"{i}. {equipo}")


#Octavos 
total_octavos = 0
for i in range(1, 9):
    total_octavos += pregunta("octavos", i)
 
#Cuartos 
total_cuartos = 0
for i in range(1, 5):
    total_cuartos += pregunta("cuartos", i)
 
#Semifinales 
total_semis = 0
for i in range(1, 3):
    total_semis += pregunta("semis", i)
 
#Final 
total_final = 0
for i in range(1, 2): 
    total_final += pregunta("final", i)
 

#RESULTADOS Y SIMULACIÓN 

print("\n--- INICIAN LOS OCTAVOS ---")
octavos = jugar_partido(SEL)
print("\nLa fase de octavos sumando sus partidos dura un total de:", total_octavos, "minutos")

print("\n--- INICIAN LOS CUARTOS ---")
cuartos = jugar_partido(octavos)
print("\nLa fase de cuartos sumando sus partidos dura un total de:", total_cuartos, "minutos")

print("\n--- INICIAN LAS SEMIFINALES ---")
semis = jugar_partido(cuartos)
print("\nLa fase de semis sumando sus partidos dura un total de:", total_semis, "minutos")

print("\n--- INICIA LA GRAN FINAL ---")
final = jugar_partido(semis)
print(f"\nEl campeón es {final} con un partido de {total_final} minutos")
