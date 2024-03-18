# (PJ100224) Pleitez Jimenez, Diego Alejandro
# Se solicitar la cantidad de números a introducir
try:
    cantidad_numeros = int(input("Introduce la cantidad de números a introducir: "))
    # Se inicia contadores
    numeros_mayores = 0
    numeros_menores = 0
    numeros_cero = 0

    # Se solicitara los números
    for i in range(cantidad_numeros):
        numero = float(input("Introduce un número: "))
        if numero > 0:
            numeros_mayores += 1
        elif numero < 0:
            numeros_menores += 1
        else:
            numeros_cero += 1

    # Se muestra los resultados
    print(f"Números mayores que 0: ", numeros_mayores)
    print(f"Números menores que 0: ", numeros_menores)
    print(f"Números iguales a 0: ", numeros_cero)
# Se solicitara un numero que sea válido 
except ValueError:
        print("Por favor, introduce un número válido.")