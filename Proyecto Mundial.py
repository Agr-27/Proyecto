import random
import os
# Inicio de la lista con los 16 equipos
sel = ["Brasil", "Francia", "Argentina", "Alemania", "España", "Inglaterra", "Portugal", "Bélgica", "Países Bajos", "Italia", "Croacia", "Uruguay", "México", "Estados Unidos", "Japón", "Marruecos"]
# Ciclo for para almacenar los 16 equipos

# Se muestra en consola los equipos seleccionados en forma de lista
print("\nSelecciones Participantes:")
for i, equipo in enumerate(sel, start=1):
    print(f"{i}. {equipo}")
    
input("\nPresiona Enter para continuar...")
print("\n" * 40) #Opcion de limpiar consola para thonny
#os.system('cls' if os.name == 'nt' else 'clear') No funciona en thonny, solo en terminal

def ronda(sel):
    ganadores = []
    for i in range(0, len(sel), 2):
        e1 = sel[i]
        e2 = sel[i+1]
        print(f"Partido: {e1} vs {e2}")
        gp = int(input("\nIngresa 1 o 2 para escoger al ganador\n"))
        if gp == 1:
                 golesg = random.randint(1,5)
                 golesp = random.randint(0,golesg - 1)   
                 print(f"\nEl marcador final es: {golesg} - {golesp} Favor {e1}\nPartido: {e1} vs {e2}")
                 ganadores.append(e1) 
        elif gp == 2:
                 golesg = random.randint(1,5)
                 golesp = random.randint(0,golesg - 1)
                 print(f"\nEl marcador final es: {golesp} - {golesg} Favor {e2}\nPartido: {e1} vs {e2}")
                 ganadores.append(e2)
        input("\nPresiona Enter para continuar...")
        print("\n" * 40) #Opcion de limpiar consola para thonny
        #os.system('cls' if os.name == 'nt' else 'clear') No funciona en thonny, solo en terminal  
                 
    return ganadores
ganadores_ronda = ronda(sel)
print("\nEquipos que pasan a la siguiente ronda:", ganadores_ronda)
