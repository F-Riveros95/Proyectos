from datetime import date
from datetime import datetime
import os

class Socio:
    def __init__(self, dni, nombre, telefono, domicilio):
        # Constructor de la clase Socio
        self.dni = dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def mostrar(self):
        # Muestra los detalles del socio
        print("RUT:{}\nNombre:{}\nTelefono:{}\nDireccion:{}".format(
            self.dni, self.nombre, self.telefono, self.domicilio))

class Pelicula:
    def __init__(self, titulo, genero, dias_arriendo_max, dias_arriendo, devolucion, dias_diferencia, dia_arrendado, cantidad):
        # Constructor de la clase Pelicula
        self.titulo = titulo
        self.genero = genero
        self.dia_arrendado = dia_arrendado
        self.dias_arriendo_max = dias_arriendo_max
        self.dias_arriendo = dias_arriendo
        self.devolucion = devolucion
        self.dias_diferencia = dias_diferencia
        self.arrendada = None
        self.cantidad = cantidad

    def mostrar(self):
        # Muestra los detalles de la película
        print("Titulo:{}\nGenero:{}\nDias de arriendo:{}".format(
            self.titulo, self.genero, self.dias_arriendo_max))

class Videoclub:
    def __init__(self):
        # Constructor de la clase Videoclub
        self.socios = []
        self.peliculas = []
        self.generos = []
        self.titulos = []
        self.cantidad = 0

    def buscar_socio(self, dni):
        # Busca un socio por su DNI
        for socio in self.socios:
            if socio.dni == dni:
                return True
        return False

    def buscar_pelicula(self, titulo):
        # Busca una película por su título
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                return True
        return False

    def agregar_socio(self, socio):
        # Agrega un socio a la lista
        self.socios.append(socio)

    def agregar_pelicula(self, pelicula):
        # Agrega una película a la lista
        self.peliculas.append(pelicula)

    def elimina_socio(self, dni):
        # Elimina un socio de la lista
        for i in range(len(self.socios)):
            if self.socios[i].dni == dni:
                del self.socios[i]
                break

    def elimina_pelicula(self, titulo):
        # Elimina una película de la lista
        i = 0
        while i < len(self.peliculas):
            if self.peliculas[i].titulo == titulo and self.peliculas[i].arrendada == None:
                del self.peliculas[i]
                break
            else:
                i += 1

    def arrendar_pelicula(self, titulo, dni):
        # Arrienda una película a un socio
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.arrendada == None:
                pelicula.arrendada = dni
                pelicula.dia_arrendado = date.today()
                pelicula.dias_arriendo = int(input("Ingrese cuantos dias va a arrendar la pelicula(max {}):".format(pelicula.dias_arriendo_max)))
                ds = pelicula.dias_arriendo
                print(ds)
                return True, ds
        return False

    def devolver_pelicula(self, titulo, dni):
        # Devuelve una película arrendada
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.arrendada == dni:
                pelicula.arrendada = None
                return 0
        return -1

def menu():
    # Muestra el menú principal
    print("SISTEMA ARRIENDO DE PELICULAS")
    print("_____________________________")
    print("1.- Crear socio")
    print("2.- Mostrar socios")
    print("3.- Eliminar socio")
    print("4.- Crear pelicula")
    print("5.- Arrendar pelicula")
    print("6.- Eliminar pelicula")
    print("7.- Devolver pelicula")
    print("8.- Mostrar peliculas")
    print("9.- Consultar peliculas por genero")
    print("10.- Mostrar peliculas arrendadas")
    print("11.- Salir")
    op = 0
    while op < 1 or op > 12:
        op = int(input("Ingrese opción: "))
    return op

def nuevo_socio():
    # Crea un nuevo objeto Socio con la información proporcionada por el usuario
    dni = input("Ingrese Dni del socio: ")
    nombre = input("ingrese Nombre: ")
    telefono = input("ingrese telefono: ")
    domicilio = input("Ingrese domicilio: ")
    return Socio(dni, nombre, telefono, domicilio)

def nueva_pelicula():
    # Crea un nuevo objeto Pelicula con la información proporcionada por el usuario
    titulo = input("Pelicula: ")
    genero = ""
    while genero != "ACCION" and genero != "DRAMA" and genero != "INFANTIL":
        genero = str(input("Genero [Accion / Drama / Infantil]: ")).upper()
    dias_arriendo_max = int(input("Dias de arriendo: "))
    num_copias = int(input("Nª Copias extra: "))
    for i in range(0, num_copias):
        new_pelicula = Pelicula(
            titulo, genero, dias_arriendo_max, None, None, None, None, None)
        video_club.agregar_pelicula(new_pelicula)
    video_club.cantidad += num_copias
    video_club.titulos.append(titulo)
    genero_titulo = [genero, titulo]
    video_club.generos.append(genero_titulo)
    return Pelicula(titulo, genero, dias_arriendo_max, None, None, None, None, None)

def llamado_menu():
    # Solicita al usuario si desea continuar con la opción actual del menú
    menus = input("Desea continuar con la opcion?(si/no):  ").strip().lower()
    if menus == "no":
        menu()

def llamado_genero():
    # Muestra la cantidad de películas por género
    lista_drama = []
    lista_accion = []
    lista_infantil = []
    for pelicula in video_club.peliculas:
        if pelicula.genero == "DRAMA":
            lista_drama.append(pelicula)
        elif pelicula.genero == "ACCION":
            lista_accion.append(pelicula)
        elif pelicula.genero == "INFANTIL":
            lista_infantil.append(pelicula)
    print(f"|Drama|   |Cantidad|:{len(lista_drama)}")
    for pelicula in lista_drama:
        print(pelicula.titulo)
    print(f"|Accion|   |Cantidad|:{len(lista_accion)}")
    for pelicula in lista_accion:
        print(pelicula.titulo)
    print(f"|Infantil|   |Cantidad|:{len(lista_infantil)}")
    for pelicula in lista_infantil:
        print(pelicula.titulo)

def peliculas_arrendadas():
    # Muestra la cantidad de películas arrendadas por género
    cont_drama = 0
    cont_accion = 0
    cont_infantil = 0
    for i in video_club.peliculas:
        if i.genero == "DRAMA" and i.arrendada != None:
            cont_drama += 1
        elif i.genero == "ACCION" and i.arrendada != None:
            cont_accion += 1
        elif i.genero == "INFANTIL" and i.arrendada != None:
            cont_infantil += 1
    print(f"Nº de peliculas  drama : {cont_drama}")
    print(f"Nº Numero de peliculas accion : {cont_accion}")
    print(f"Nº Numero de peliculas infantiles : {cont_infantil}")

# Programa principal
video_club = Videoclub()
op = menu()
while op != 11:
    if op == 1:
        socio = nuevo_socio()
        if video_club.buscar_socio(socio.dni):
            print("Ya existe el socio, su rut es: ", socio.dni)
        else:
            video_club.agregar_socio(socio)
            print("Socio creado")
            socio.mostrar()  # Mostrará los datos del objeto creado
        input("Presione cualquier tecla para continuar...")

    elif op == 2:
        # Opción 2: Mostrar socios
        print("Los socios actuales son:")
        for socio in video_club.socios:
            print(socio.nombre)

    elif op == 3:
        # Opción 3: Eliminar socio
        dni = input("ingrese dni del socio: ")
        if video_club.buscar_socio(dni):
            video_club.elimina_socio(dni)
            print("Socio eliminado")
        else:
            print("Socio no existe con ese rut")

    elif op == 4:
        # Opción 4: Crear película
        pelicula = nueva_pelicula()
        video_club.agregar_pelicula(pelicula)
        pelicula.mostrar()

    elif op == 5:
        # Opción 5: Arrendar película
        titulo = input("Ingrese pelicula a arrendar: ")
        dni = input("ingrese dni del socio:")
        fecha_arriendo = str(input("Ingrese fecha de arriendo: DD-MM-AAAA: "))
        ffecha_arriendo = datetime.strptime(fecha_arriendo, '%d-%m-%Y')
        hay_pelicula = video_club.buscar_pelicula(titulo)
        hay_socio = video_club.buscar_socio(dni)
        if hay_pelicula and hay_socio:
            bol, dias = video_club.arrendar_pelicula(titulo, dni)
            if bol == True:
                print("Pelicula Arrendada")
                cont_copias = 0
                for pelicula in video_club.peliculas:
                    if pelicula.titulo == titulo and pelicula.arrendada == None:
                        cont_copias += 1

                print(f"Quedan {cont_copias} copias disponibles")

            else:
                print("Pelicula no disponible")
        if not hay_socio:
            print("El socio no existe")
        if not hay_pelicula:
            print("pelicula no existe")

    elif op == 6:
        # Opción 6: Eliminar película
        titulo = input("Ingrese pelicula a eliminar: ")
        video_club.elimina_pelicula(titulo)
        print("Pelicula Eliminada")

    elif op == 7:
        # Opción 7: Devolver película
        titulo = input("Ingrese pelicula a devolver: ")
        dni = input("ingrese dni del socio:")

        hay_pelicula = video_club.buscar_pelicula(titulo)
        hay_socio = video_club.buscar_socio(dni)
        if hay_pelicula and hay_socio:
            resultado = video_club.devolver_pelicula(titulo, dni)
            if resultado == 0:
                fecha_devolucion = str(input("Ingrese fecha de devolucion: DD-MM-AAAA: "))
                fecha_dev = datetime.strptime(fecha_devolucion, '%d-%m-%Y')
                Dias_diferencia = fecha_dev - ffecha_arriendo
                print(Dias_diferencia)

                if Dias_diferencia.days > dias:
                    dias_d = Dias_diferencia.days - dias
                    print("Dias Morosos: ", dias_d, " dias")
                else:
                    print("Devolucion a tiempo. Gracias")

    elif op == 8:
        # Opción 8: Mostrar películas
        print("Las peliculas son:")
        for pelicula in video_club.peliculas:
            print(pelicula.titulo)
        if video_club.peliculas == []:
            print('No se encuentran peliculas disponibles...')

    elif op == 9:
        # Opción 9: Consultar películas por género
        llamado_genero()

    elif op == 10:
        # Opción 10: Mostrar películas arrendadas
        peliculas_arrendadas()

    elif op == 11:
        # Opción 11: Salir
        exit()

    # Solicitar si desea volver al menú
    limpieza = input("Desea entrar al menu?(si/no): ").strip().lower()

    if limpieza == "si":
        os.system("cls")
        op = menu()
    else:
        print("Adios al sistema de Arriendos")
        exit()
