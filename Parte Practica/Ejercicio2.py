#(PJ100224)Pleitez Jiménez, Diego Alejandro
import random
# Se generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 3

# Se crea un Bucle para realizar los intentos
while intentos > 0:
    # Se solicitara un número al usuario
    print("¡Bienvenido al juego de adivinanzas de números!")
    print("Adivina el número entre 1 y 100. Tienes 3 intentos.")
    numero_introducido = int(input("Introduce un número entre 1 y 100: "))
    
    # Se Comprobara si el número introducido es correcto
    if numero_introducido == numero_secreto:
        print(f"¡Has acertado! El número secreto era {numero_secreto} y lo has adivinado en {3-intentos+1} intentos.")
        break
    elif numero_introducido < numero_secreto:
        print("El número secreto es mayor que el introducido.")
    else:
        print("El número secreto es menor que el introducido.")
    
    # Se restar un intento
    intentos -= 1

# Se mostrar un mensaje de error si se ha llegado al límite de intentos
if intentos == 0:
    print("Lo siento, has agotado los intentos. El número secreto era", numero_secreto)
