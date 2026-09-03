import random
import os
# Se incializa la lista con las 16 selcciones
sel = ["Brasil", "Francia", "Argentina", "Alemania", "España", "Inglaterra", "Portugal", "Bélgica", "Países Bajos", "Italia", "Croacia", "Uruguay", "México", "Estados Unidos", "Japón", "Marruecos"]


# Se muestra en consola los equipos seleccionados en forma de lista
print("\nSelecciones Participantes:")
for i, equipo in enumerate(sel, start=1): # Funcion enumerate(forma facil de realizar una lista sin un contador)
    print(f"{i}. {equipo}")
    
input("\nPresiona Enter para continuar...")
print("\n" * 40) #Opcion de limpiar consola para thonny
#os.system('cls' if os.name == 'nt' else 'clear') No funciona en thonny, solo en terminal

# Se declara la funcion que se usara en las rondas. Ejemplo: ronda(octavos) ronda(cuartos)
def ronda(sel):
    # Declaracion de la lista donde se guardaran los ganadores
    ganadores = []
    # Ciclo for (inicio, condicion, secuencia) Se empieza del 0 por como la listaes interpretada por python
    for i in range(0, len(sel), 2): # len permite conocer cuantos datos en la lista
        e1 = sel[i]
        e2 = sel[i+1] # Selecciona los enfrentamientos
        print(f"Partido: {e1} vs {e2}")
        gp = int(input("\nIngresa 1 o 2 para escoger al ganador\n"))
        
        # Condicionales if (victoria, derrota)
        if gp == 1:
                 golesg = random.randint(1,5)
                 golesp = random.randint(0,golesg - 1)  # Funcion random (randint para solo enteros) (minimo, maximo) 
                 print(f"\nEl marcador final es: {golesg} - {golesp} Favor {e1}\nPartido: {e1} vs {e2}")
                 ganadores.append(e1) # .append para guardar el equipo en la lista
        elif gp == 2:
                 golesg = random.randint(1,5)
                 golesp = random.randint(0,golesg - 1)
                 print(f"\nEl marcador final es: {golesp} - {golesg} Favor {e2}\nPartido: {e1} vs {e2}")
                 ganadores.append(e2)
            
        input("\nPresiona Enter para continuar...")
        print("\n" * 40) #Opcion de limpiar consola para thonny
        #os.system('cls' if os.name == 'nt' else 'clear') No funciona en thonny, solo en terminal  

    # Return para sacar la lista ganadores fuera de la funcion
    return ganadores
Octavos = ronda(sel) # Se llama la funcion
print("\nEquipos que pasan a la siguiente ronda:", Octavos) # Se visualiza los equipos ganadores
