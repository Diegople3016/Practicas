def main():
    personas = []

    print("Bienvenido al programa de registro de personas")

    for i in range(3): 
        nombre = input("Ingrese el nombre de la persona (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        identificacion = input("Ingrese la identificación de la persona: ")
        personas.append({'nombre': nombre, 'identificacion': identificacion})

    print("\nListado de personas registradas:")
    for persona in personas:
        print("Nombre:", persona['nombre'])
        print("Identificación:", persona['identificacion'])
        print()

if __name__ == "__main__":
    main()
