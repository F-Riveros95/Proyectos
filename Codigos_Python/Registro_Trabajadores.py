# Sistema de Registro de Trabajadores

# Definición de la clase Trabajador
class Trabajador:
    def __init__(self, nombre, edad, puesto):
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto

# Definición de la clase RegistroTrabajadores
class RegistroTrabajadores:
    def __init__(self):
        self.trabajadores = []

    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def eliminar_trabajador(self, nombre):
        self.trabajadores = [t for t in self.trabajadores if t.nombre != nombre]

    def mostrar_trabajadores(self):
        print("\nRegistro de Trabajadores:")
        if not self.trabajadores:
            print("No hay trabajadores registrados.")
        else:
            for trabajador in self.trabajadores:
                print(f"Nombre: {trabajador.nombre}, Edad: {trabajador.edad}, Puesto: {trabajador.puesto}")

# Función principal para el uso del programa
def main():
    # Crear una instancia de RegistroTrabajadores
    registro_trabajadores = RegistroTrabajadores()

    while True:
        # Menú de opciones
        print("\nOpciones:")
        print("1. Agregar Trabajador")
        print("2. Mostrar Trabajadores")
        print("3. Eliminar Trabajador")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == "1":
            # Agregar un nuevo trabajador
            nombre = input("Ingrese el nombre del trabajador: ")
            edad = int(input("Ingrese la edad del trabajador: "))
            puesto = input("Ingrese el puesto del trabajador: ")
            nuevo_trabajador = Trabajador(nombre, edad, puesto)
            registro_trabajadores.agregar_trabajador(nuevo_trabajador)
            print("Trabajador agregado con éxito.")

        elif opcion == "2":
            # Mostrar la lista de trabajadores
            registro_trabajadores.mostrar_trabajadores()

        elif opcion == "3":
            # Eliminar un trabajador por nombre
            nombre_eliminar = input("Ingrese el nombre del trabajador a eliminar: ")
            registro_trabajadores.eliminar_trabajador(nombre_eliminar)
            print("Trabajador eliminado con éxito.")

        elif opcion == "4":
            # Salir del programa
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            # Manejar una opción no válida
            print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    # Llamar a la función principal si el script se ejecuta directamente
    main()
