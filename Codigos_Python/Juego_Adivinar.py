# Importar el módulo random para generar números aleatorios
import random

# Definir la función para el juego de adivinar el número
def adivinar_numero():
    """Juego de adivinar el número con límite de intentos."""
    
    # Generar un número secreto aleatorio entre 1 y 10
    numero_secreto = random.randint(1, 10)
    
    # Inicializar variables para contar los intentos
    intentos = 0
    intentos_maximos = 3

    # Mensaje de bienvenida
    print("¡Bienvenido al Juego de Adivinar el Número!")
    print("Estoy pensando en un número entre 1 y 10.")
    print(f"Tienes un total de {intentos_maximos} intentos.")

    # Bucle principal del juego
    while intentos < intentos_maximos:
        # Solicitar al usuario que adivine el número
        intento = int(input("Adivina el número: "))
        
        # Incrementar el contador de intentos
        intentos += 1

        # Comprobar si el intento es correcto, demasiado bajo o demasiado alto
        if intento == numero_secreto:
            print(f"¡Correcto! Has adivinado el número en {intentos} intentos.")
            break
        elif intento < numero_secreto:
            print("Demasiado bajo. ¡Intenta de nuevo!")
        else:
            print("Demasiado alto. ¡Intenta de nuevo!")

    # Comprobar si se han agotado los intentos y mostrar el número secreto
    if intentos == intentos_maximos and intento != numero_secreto:
        print(f"\nLo siento, has agotado tus {intentos_maximos} intentos. El número secreto era {numero_secreto}. ¡Has perdido!")

# Llamar a la función para iniciar el juego
adivinar_numero()
