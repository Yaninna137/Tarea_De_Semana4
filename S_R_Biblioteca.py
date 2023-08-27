class Libros:
    def __init__(self,titulo,autor,num_pagina):
        self.titulo = titulo
        self.autor  = autor
        self.num_pag = num_pagina
    def __repr__(self):
        return f'El libro "{self.titulo}" por {self.autor}.Cuenta con {self.num_pag} numeros de páginas'
class Usuarios:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.Historial_Prestamo = []
    def __repr__(self):
        return f'{self.nombre} {self.apellido}'
    
    def Agregar_HU(self,r_prestamo):
        self.Historial_Prestamo.append(r_prestamo)              # Registramos historial
    def mostrar_historial(self):
        return self.Historial_Prestamo
class Prestamos:
    def __init__(self,usuario,libro,f_prestamo,f_devolucion):
        self.R_prestamo = f'El usuario {usuario} pidio prestado: {libro}, el dia {f_prestamo}.Fecha ah devolver: {f_devolucion}'
        self.usuario = usuario
        self.libro = libro
        self.f_prestamo = f_prestamo
        self.f_devolver = f_devolucion
        self.Libros_Prestados = []
    def __repr__(self) -> str:
        return f'{self.usuario} {self.libro} {self.f_prestamo} {self.f_devolver}'    
    def añadir_his_ah_usuario(self,usuario):          # mandele el dato al usario de su registro
        usuario.Agregar_HU(self.R_prestamo)
class Catalogo_Bib:
    def __init__(self):
        self.lista_librosCB = []
        self.Estado_librosCB_D = {}
        self.lista_UsuariosR = []
    def Agregar_LCB(self,libro):
        self.lista_librosCB.append(libro)
        self.Estado_librosCB_D[libro] = True
    def Agregar_UCB(self,usuario):
        self.lista_UsuariosR.append(usuario)
    def Eliminar_LCB(self,ide):
        self.Estado_librosCB_D.pop(self.lista_librosCB[ide])       #Eliminar libro del diccionario de disponibilidad
        self.lista_librosCB.remove(self.lista_librosCB[ide])       #Eliminar libro de lista 
    def Cambiar_Estado(self,libro):                               #Cambiar estado del libro true:disponible, false: no disponible
        if self.Estado_librosCB_D[libro] == False:
            self.Estado_librosCB_D[libro] = True
        else:
            self.Estado_librosCB_D[libro] = False
    def Libros_disponibles(self):                                #Entegar una lista de los libros disponibles

        contador = 0
        log = len(self.Estado_librosCB_D)
        libros_disponibles = []
        if log > 0:
            for i in self.Estado_librosCB_D:
                contador += 1
                if self.Estado_librosCB_D[i] == True:
                    libros_disponibles.append(f'{contador}. {self.lista_librosCB[contador -1]}')
            return libros_disponibles  
        else: 
            print('0 libro disponible')
    def Mostra_libros(self):
        for i in range(len(self.lista_librosCB)):
            print(i+1,'.-',self.lista_librosCB[i])
Catalogo = Catalogo_Bib()
salir = True
while salir == True:
    print('Bienvenido')
    print('1.Registrar Usuario')
    print('2.Añadir libro al catalogo')
    print('3.Eliminar libro al catalogo')
    print('4.Solicitar libro.')
    print('5.Devolución de libro')
    print('7.Libros disponibles')
    print('8.Veer historial del Usuario')
    print('9.Salir')
    opcion = input('Ingrese un numero: ')
    if opcion == '1':
        print('Porfavor ingrese los siguientes datos para completar sus registro:')
        while True:
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            Persona = Usuarios(nombre,apellido)
            Catalogo.Agregar_UCB(Persona)
            print(f'El usuario {Persona} ah sido ingresado al sistema')
            respuesta = input('¿Desea agregar otro usuario? (si)(no): ').lower()
            if respuesta == 'si' or respuesta =='no':
                if respuesta == 'no':
                    break
            else:
                print('Error.El dato ingresado es incorrecto.')
                break
    if opcion == '2':
        print('Para registrar libro agrege los suiguientes datos:')
        while True:
            Titulo = input('Ingrese el titulo: ')
            Autor = input('Ingrese el autor: ')
            Num_pagina = input('Ingrese el num. de páginas: ')
            libro = Libros(Titulo,Autor,Num_pagina)
            Catalogo.Agregar_LCB(libro)
            print(libro,'Ha sido ingresado al sistema')
            respuesta = input('¿Desea agregar otro libro? (si)(no): ').lower()
            if respuesta == 'si' or respuesta =='no':
                if respuesta == 'no':
                    break
            else:
                print('Error.El dato ingresado es incorrecto.')
                break
    if opcion == '3':
        print('Contamos con los siguientes libros:')
        Catalogo.Mostra_libros()
        respuesta = (int(input('Ingrese el id del libro ah eliminar.Para salir ingrese (0): '))-1)
        if respuesta <= len(Catalogo.lista_librosCB):
            alerta = input('Estas seguro de eliminar este libro (si)(no):')
            if alerta == 'si':
                Catalogo.Eliminar_LCB(respuesta)
                print('El libro ah sido eliminado del sisteme')
            else:
                break
        else:
            break
    if opcion == '4':
        pass
        
    if opcion == '9':
        break
#print(Catalogo.lista_UsuariosR)
print(Catalogo.lista_librosCB)