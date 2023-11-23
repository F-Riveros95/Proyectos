class cliente:
    def __init__(self,rut,nombre,genero,balance):
        self.rut=rut
        self.nombre=nombre
        self.genero=genero
        self.balance=balance
        self.tr=[] # guarda las transacciones de los clientes(Tipo,fecha,glosa,monto)

    def mostrar(self):
        print("Rut: {}\nNombre:{}\nGenero:{}\nBalance:{}".format(self.rut,self.nombre,self.genero,self.balance))
        print(self.tr)
    
    def buscarcliente(self,rut):
        print(rut)
        for cli in clientes:
            if rut == cli.rut:
               return True
        return False


    #Agregar las transacciones de los clientes deben ser realizados dentro de la clase 
    def agregartx(self,transaccion):
        self.tr.append(transaccion)


def crea_cliente():
    rut=input("ingresa rut del cliente: ")
    nombre=input("ingresa nommbre del cliente: ")
    genero=""
    while genero !="F" and genero !="M":
        genero=input("Ingresa genero del cliente ((F)emenino o (M)asculino: ").upper()
    balance=int(input("Ingrese balance inicial de la cuenta: "))
    cl=cliente(rut,nombre,genero,balance) #crea el objeto cl de la clase cliente con sus atributos
    return cl #retorna desde donde se llamo

def agregar_tr(clientes):
    rut=input("ingrese rut del cliente respectivo a la transaccion: ")
    for cli in clientes:
        if rut == cli.rut:
            tipo="" 
            while tipo !="D" and tipo !="G":
                tipo=input("Ingrese tipo de transacción (D)eposito o (G)iro:").upper()
            fecha=input("Ingrese fecha de la transacción (DD-MM-AAAA):")
            glosa=input("ingrese Glosa de la transacción: ")
            monto=int(input("Ingrese monto: "))
            if tipo == "D":
                cli.balance=cli.balance + monto
                tx=(tipo,fecha,glosa,monto)
                cli.agregartx(tx)
            else:
                if cli.balance >= monto:
                    cli.balance=cli.balance - monto
                    tx=(tipo,fecha,glosa,monto)
                    cli.agregartx(tx)
                else:
                    print("saldo insuficiente para realizar la operacion")
        





def menuprincipal():
    print("Menu Sistema Bancario")
    print("_____________________")
    op=int(input("Elija opcion: \n1.- Crear Cliente \n2.-Mostrar Cliente \n3.- Agregar Transaccion \n4.-Salir\n"))
    return op

clientes=[] # lista que guarda los objetos clientes creados(instancias)
op=menuprincipal()
while op !=4:
    if op == 1:
        cl=crea_cliente()
        if cl.buscarcliente(cl.rut): # debe ir a la clase a la funcion buscarcliente
            print()
            print("Cliente ya existe") 
        else:
            clientes.append(cl) # se agrega a la lista cliente el objeto cl(con todos sus atributos)
            print("El cliente ",cl.nombre," se ha creado exitosamente")
    elif op == 2:
        for cli in clientes:
            cli.mostrar() # toma cada cliente de la lista clientes y los muestra de acuerdo al método mostrar
            print("______________")

    elif op == 3:
        agregar_tr(clientes)

    else:
        break

    op=menuprincipal()