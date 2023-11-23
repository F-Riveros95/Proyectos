# Definición de la función para sumar dos números
def sumar(a, b):
    return a + b

# Definición de la función para restar dos números
def restar(a, b):
    return a - b

# Definición de la función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Definición de la función para dividir dos números
def dividir(a, b):
    # Verificar si el divisor no es cero antes de realizar la división
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

# Mensaje de bienvenida
print("Calculadora Básica")

# Obtener los números de entrada del usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Solicitar al usuario que seleccione una operación
print("Seleccione la operación (+, -, *, /): ")
operacion = input()

# Realizar la operación seleccionada y mostrar el resultado
if operacion == '+':
    print("Resultado:", sumar(num1, num2))
elif operacion == '-':
    print("Resultado:", restar(num1, num2))
elif operacion == '*':
    print("Resultado:", multiplicar(num1, num2))
elif operacion == '/':
    print("Resultado:", dividir(num1, num2))
else:
    print("Operación inválida.")
