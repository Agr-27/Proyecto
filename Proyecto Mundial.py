import random  # Librería random para generar los goles
import os # Libreria os para checar si existe el archivo de texto
 
SEL = [
    "Brasil", "Francia", "Argentina", "Alemania",
    "España", "Inglaterra", "Portugal", "Bélgica",
    "Países Bajos", "Italia", "Croacia", "Uruguay",
    "México", "Estados Unidos", "Japón", "Marruecos",
]

# Matriz para guardar el historial de todos los partidos
historial = []

def cambiar_selecciones():
    while True:
        limpiar_pantalla()
        print("Selecciones Participantes:\n")
        for i in range(len(SEL)):
            enumeracion(i, i + 1)

        numero = int(input("\nIngresa el número de la selección que deseas cambiar (1-16) o 0 para volver: "))
        if numero == 0:
            break
        elif 1 <= numero <= 16:
            nuevo_equipo = input("Ingresa el nombre de la nueva selección: ")
            SEL[numero - 1] = nuevo_equipo
            print(f"\nEquipo #{numero} cambiado a {nuevo_equipo}")
            
            otra = input("\n¿Quieres cambiar otra selección? (s/n): ").lower()
            if otra != "s":
                break
        else:
            print("\nNúmero inválido. Intenta de nuevo.")
            input("Presiona Enter para continuar...")

def limpiar_pantalla():
    """Limpia la pantalla de la consola donde se ejecute el programa."""
    print("\n" * 50)

def enumeracion(indice, numero):
    """Imprime una selección con su número de lista."""
    print(f"{numero}. {SEL[indice]}")
 
def pregunta(fase, numero):
    """Pide la duración del partido (90 o 120 minutos) y la regresa."""
    mensaje = (f"\nElige los minutos que quieres que dure el partido de "
               f"{fase} {numero} (90 o 120): ")
    minutos = int(input(mensaje))
 
    # Se aseguro que solo si puedan asignar 90 o 120 mins
    if minutos != 90 and minutos != 120:
        print("Valor no válido, será de 90 minutos")
        minutos = 90
 
    return minutos
 
def jugar_partido(equipos, nombre_fase):
    """Juega un partido entre dos equipos y regresa al ganador."""
    ganadores = []
    
    # Ciclo for (inicio, condicion, secuencia) Se empieza del 0 por como la lista es interpretada por python
    for i in range(0, len(equipos), 2): # len permite conocer cuantos datos en la lista
        e1 = equipos[i]
        e2 = equipos[i+1] # Selecciona los enfrentamientos
        print(f"\nPartido: {e1} vs {e2}")
        
        opcion = int(input("Ingresa 1 o 2 para escoger al ganador\n"))

        # Si se ingresa un número que no sea 1 o 2
        if opcion != 1 and opcion != 2:
            print("Opción no válida, gana el equipo 1 por defecto")
            opcion = 1
 
        goles_ganador = random.randint(1, 5)
        goles_perdedor = random.randint(0, goles_ganador - 1)
 
        # Decide al ganador y asigna sus goles
        if opcion == 1:
            goles_e1 = goles_ganador
            goles_e2 = goles_perdedor
            ganador = e1
        elif opcion == 2:
            goles_e1 = goles_perdedor
            goles_e2 = goles_ganador
            ganador = e2
        print(f"Marcador final: {e1} {goles_e1} - {goles_e2} {e2}")
        ganadores.append(ganador)
        input("\nPresiona Enter para continuar...")
     
        # Se agrega una fila (lista) con los datos del partido a la matriz
        partido_resumen = [nombre_fase, e1, e2, f"{goles_e1}-{goles_e2}", ganador]
        historial.append(partido_resumen)
        
    return ganadores

def imprime_matriz(matriz):
    """Crea la matriz para mostrar el historial de los partidos."""
    i = 0
    for linea in matriz:
        j = 0
        fila_texto = ""
        for columna in linea:
            elemento = str(matriz[i][j])
            fila_texto = fila_texto + elemento + " | "
            j = j + 1
        print(fila_texto)
        i = i + 1

def simulacion_mundial():   
    # Se muestra en consola los equipos seleccionados en forma de lista
    print("\nSelecciones Participantes:")
    for i in range(len(SEL)):
        enumeracion(i, i + 1)

    # Octavos 
    total_octavos = 0
    for i in range(1, 9):
        total_octavos += pregunta("octavos", i)
    
    # Cuartos 
    total_cuartos = 0
    for i in range(1, 5):
        total_cuartos += pregunta("cuartos", i)
    
    # Semifinales 
    total_semis = 0
    for i in range(1, 3):
        total_semis += pregunta("semis", i)
    
    # Final 
    total_final = 0
    for i in range(1, 2): 
        total_final += pregunta("final", i)
    

    # Resultados y simulacion 

    # Uso de cadenas de texto
    texto_clasificados = "Equipos clasificados a Cuartos de Final: "
    texto_semis = texto_clasificados.replace("Cuartos de Final", "Semifinales")
    texto_final = texto_clasificados.replace("Cuartos de Final", "la Gran Final")

    print("\n--- inician los octavos ---".upper())
    octavos = jugar_partido(SEL, "Octavos")
    print("\n", texto_clasificados, octavos)
    print("\nLa fase de octavos sumando sus partidos dura un total de:", total_octavos, "minutos")
    input("\nPresiona Enter para continuar con los Cuartos de Final...")

    print("\n--- inician los cuartos ---".upper())
    cuartos = jugar_partido(octavos, "Cuartos") 
    print("\n", texto_semis, cuartos)
    print("\nLa fase de cuartos sumando sus partidos dura un total de:", total_cuartos, "minutos")
    input("\nPresiona Enter para continuar con las Semifinales...")

    print("\n--- inician las semifinales ---".upper())
    semis   = jugar_partido(cuartos, "Semis") 
    print("\n", texto_final, semis)
    print("\nLa fase de semis sumando sus partidos dura un total de:", total_semis, "minutos")
    input("\nPresiona Enter para continuar con la Gran Final...")

    print("\n--- inicia la gran final ---".upper())
    final   = jugar_partido(semis, "Final")

    # Impresión final de la matriz
    print("                    historial del torneo                    ".upper())
    imprime_matriz(historial)

    print(f"\n¡El campeón es {final[0]} con un partido de {total_final} minutos!")

    guardar_simulacion(historial, final[0])
    historial.clear()  # Limpia la matriz para que no se repitan partidos en la siguiente simulación
    print("\nSimulación guardada")

def guardar_simulacion(matriz, campeon):
    """Guarda la simulacion en un archivo texto."""
    with open("historial_mundial.txt", "a", encoding="utf-8") as archivo:
        archivo.write("----------------------------------------------\n")
        archivo.write(f"SIMULACION DE MUNDIAL | CAMPEON: {campeon}\n")
        archivo.write("----------------------------------------------\n")
        
        for fila in matriz:
            linea = ""
            for dato in fila:
                linea = linea + str(dato) + " | "
            archivo.write(linea + "\n")
            
        archivo.write("\n")

def leer_simulaciones():
    """Lee el archivo guardado con las simulaiones."""
    if os.path.exists("historial_mundial.txt"):
        with open("historial_mundial.txt", "r", encoding="utf-8") as archivo:
            print(archivo.read())
    else:
        print("\nNo hay simulaciones guardadas")

# Codigo principal(Menu)
while True:
    limpiar_pantalla()
    print("--- SIMULADOR DE MUNDIAL ---")
    print("Elige que quieres hacer a continuacion")
    print("1. Cambiar selecciones de la simulacion")
    print("2. Simular mundial")
    print("3. Mostrar simulaciones pasadas")
    print("4. Salir")

    opcion = int(input())
    if opcion == 1:
        limpiar_pantalla()
        cambiar_selecciones()
    elif opcion == 2:
        limpiar_pantalla()
        simulacion_mundial()
        input("\nPresiona Enter para volver al menu...")
    elif opcion == 3:
        limpiar_pantalla()
        leer_simulaciones()
        input("\nPresiona Enter para volver al menu...")
    elif opcion == 4:
        limpiar_pantalla()
        print("---- Gracias por usar el simulador ----".upper())
        break
    else:
        print("Opcion no valida, intentalo de nuevo")
        input("\nPresiona Enter para volver al menu...")


