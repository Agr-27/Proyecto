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
 
 
def jugar_partido(equipo_1, equipo_2, minutos):
    """Juega un partido entre dos equipos y regresa al ganador."""
    print(f"\nPartido: {equipo_1} vs {equipo_2}")
    opcion = int(input("Ingresa 1 o 2 para escoger al ganador: "))
 
    #Si se ingresa un número que no sea 1 o 2
    if opcion != 1 and opcion != 2:
        print("Opción no válida, gana el equipo 1 por defecto")
        opcion = 1
 
    goles_ganador = random.randint(1, 5)
    goles_perdedor = random.randint(0, goles_ganador - 1)
 
    #Decide al ganador y asigna sus goles
    if opcion == 1:
        print(f"Marcador final: {equipo_1} {goles_ganador} - "
              f"{goles_perdedor} {equipo_2}")
        ganador = equipo_1
    elif opcion == 2:
        print(f"Marcador final: {equipo_1} {goles_perdedor} - "
              f"{goles_ganador} {equipo_2}")
        ganador = equipo_2
 
    #Aviso de que el partido se fue a tiempos extra
    if minutos == 120:
        print("El partido se fue a tiempos extra")
 
    input("\nPresiona Enter para continuar...")
    return ganador
 
 
#Lista de selecciones
enumeracion(0, 1)
enumeracion(1, 2)
enumeracion(2, 3)
enumeracion(3, 4)
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
enumeracion(14, 15)
enumeracion(15, 16)
 
#Octavos
#Se pueden simplificar los partidos con un ciclo for (siguiente entrega)
mins_octavos_1 = pregunta("octavos", 1)
ganador_octavos_1 = jugar_partido(SEL[0], SEL[1], mins_octavos_1)
 
mins_octavos_2 = pregunta("octavos", 2)
ganador_octavos_2 = jugar_partido(SEL[2], SEL[3], mins_octavos_2)
 
mins_octavos_3 = pregunta("octavos", 3)
ganador_octavos_3 = jugar_partido(SEL[4], SEL[5], mins_octavos_3)
 
mins_octavos_4 = pregunta("octavos", 4)
ganador_octavos_4 = jugar_partido(SEL[6], SEL[7], mins_octavos_4)
 
mins_octavos_5 = pregunta("octavos", 5)
ganador_octavos_5 = jugar_partido(SEL[8], SEL[9], mins_octavos_5)
 
mins_octavos_6 = pregunta("octavos", 6)
ganador_octavos_6 = jugar_partido(SEL[10], SEL[11], mins_octavos_6)
 
mins_octavos_7 = pregunta("octavos", 7)
ganador_octavos_7 = jugar_partido(SEL[12], SEL[13], mins_octavos_7)
 
mins_octavos_8 = pregunta("octavos", 8)
ganador_octavos_8 = jugar_partido(SEL[14], SEL[15], mins_octavos_8)
 
total_octavos = (mins_octavos_1 + mins_octavos_2 + mins_octavos_3
                 + mins_octavos_4 + mins_octavos_5 + mins_octavos_6
                 + mins_octavos_7 + mins_octavos_8)
 
#Cuartos
mins_cuartos_1 = pregunta("cuartos", 1)
ganador_cuartos_1 = jugar_partido(ganador_octavos_1, ganador_octavos_2,
                                  mins_cuartos_1)
 
mins_cuartos_2 = pregunta("cuartos", 2)
ganador_cuartos_2 = jugar_partido(ganador_octavos_3, ganador_octavos_4,
                                  mins_cuartos_2)
 
mins_cuartos_3 = pregunta("cuartos", 3)
ganador_cuartos_3 = jugar_partido(ganador_octavos_5, ganador_octavos_6,
                                  mins_cuartos_3)
 
mins_cuartos_4 = pregunta("cuartos", 4)
ganador_cuartos_4 = jugar_partido(ganador_octavos_7, ganador_octavos_8,
                                  mins_cuartos_4)
 
total_cuartos = (mins_cuartos_1 + mins_cuartos_2 + mins_cuartos_3
                 + mins_cuartos_4)
 
#Semifinales
mins_semis_1 = pregunta("semis", 1)
ganador_semis_1 = jugar_partido(ganador_cuartos_1, ganador_cuartos_2,
                                mins_semis_1)
 
mins_semis_2 = pregunta("semis", 2)
ganador_semis_2 = jugar_partido(ganador_cuartos_3, ganador_cuartos_4,
                                mins_semis_2)
 
total_semis = mins_semis_1 + mins_semis_2
 
#Final
mins_final = pregunta("final", 1)
campeon = jugar_partido(ganador_semis_1, ganador_semis_2, mins_final)
 
#Resultados
print("\nLa fase de octavos sumando sus partidos dura un total de:",
      total_octavos, "minutos")
print("La fase de cuartos sumando sus partidos dura un total de:",
      total_cuartos, "minutos")
print("La fase de semis sumando sus partidos dura un total de:",
      total_semis, "minutos")
print(f"\n¡El campeón es {campeon}!")
