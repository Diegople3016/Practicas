personas = {}

for i in range(1, 4):  
    nombre = input(f"Ingrese el nombre de la persona {i}: ")
    identificacion = input(f"Ingrese la identificación de la persona {i}: ")
    personas[nombre] = identificacion

print("\nDatos de las personas:")
for nombre, identificacion in personas.items():
    print(f"Nombre: {nombre} - Identificación: {identificacion}")
