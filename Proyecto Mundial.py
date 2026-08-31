sel = ""
for i in range(0, 24):
    cont = input(f"Ingresa la selección {i + 1} de 24: ")
    sel = sel + f"{i + 1}. {cont}\n"

print("\nSelecciones Participantes:")
print(sel)