# Importar los módulos random y string para generar contraseñas aleatorias
import random
import string

# Definir la función para generar contraseñas aleatorias
def generar_contraseña(longitud):
    """Genera una contraseña aleatoria."""
    
    # Definir los caracteres posibles para la contraseña
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar la contraseña combinando caracteres aleatorios
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    
    # Devolver la contraseña generada
    return contraseña

# Solicitar al usuario la longitud deseada para la contraseña
longitud_contraseña = int(input("Ingrese la longitud de la contraseña deseada: "))

# Generar la contraseña utilizando la función
contraseña_generada = generar_contraseña(longitud_contraseña)

# Mostrar la contraseña generada
print(f"\nContraseña generada: {contraseña_generada}")
