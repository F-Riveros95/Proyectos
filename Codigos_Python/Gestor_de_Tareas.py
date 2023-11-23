# Lista para almacenar las tareas
tareas = []

# Función para agregar una nueva tarea a la lista
def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada.")

# Función para mostrar las tareas pendientes
def mostrar_tareas():
    if not tareas:
        print("No hay tareas pendientes.")
    else:
        print("Tareas pendientes:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")

# Función para completar una tarea
def completar_tarea():
    mostrar_tareas()
    indice = int(input("Ingrese el número de la tarea completada: "))
    if 1 <= indice <= len(tareas):
        tarea_completada = tareas.pop(indice - 1)
        print(f"Tarea completada: {tarea_completada}")
    else:
        print("Número de tarea inválido.")

# Bucle principal del programa
while True:
    print("Gestor de Tareas")
    print("1. Agregar Tarea")
    print("2. Mostrar Tareas")
    print("3. Completar Tarea")
    print("4. Salir")
    
    # Solicitar al usuario que elija una opción
    opcion = int(input("Seleccione una opción: "))

    # Evaluar la opción seleccionada y realizar la acción correspondiente
    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        mostrar_tareas()
    elif opcion == 3:
        completar_tarea()
    elif opcion == 4:
        break
    else:
        print("Opción inválida.")
