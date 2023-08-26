class Libros():
    def __init__(self,titulo,autor,genero,num_pagina):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_pagina = num_pagina
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} con {self.num_pagina} páginas,{self.genero}"
    
    def __repr__(self):
        return f"'{self.titulo}' por {self.autor} con {self.num_pagina} páginas,{self.genero}"   
class Usuarios():
    def __init__(self,nombre,apellido,):
        self.nombre = nombre
        self.apellido = apellido
        self.lista_de_usuarios = []
        self.libros_pedidos = {}

    def __str__(self):
        return f'{self.nombre} {self.apellido}'  
    def Historial_de_prestamos(self):
        pass

class Prestamos():
    def __init__(self,libro,usuario,f_prestamo,f_devolver):
        self.libro = libro
        self.usuario = usuario
        self.f_prestamo = f_prestamo
        self.f_devolver = f_devolver
        self.registro_de_libros_prestados = []
    def __str__(self):
        return f'{self.usuario} {self.libro} {self.f_prestamo} {self.f_devolver}'
    
    def del_libro_prestado(self):
        pass
class Catalogo_Bibloteca(): #registro
    def __init__(self,nombre):
        self.nombre = nombre
        self.r_libro = []
        self.libros_disponibles_y_no = {}                       # Un diccionario de todos los libros , si estan disponibles o no 
        self.r_usuario = []                                  #Una ista para almacenar todos los usuarios
        self.r_prestamo = None

    def Registros_de_libros(self,m = 0):
        longitud = len(self.r_libro)
        if m == 0:
            if longitud > 0:
                for x in range(len(self.r_libro)):                        # Con un for recorremos los libros , que se encuntren en la lista de registros del catalogo
                    print('{}.{}'.format(x+1,self.r_libro[x]))            # mostar cada libro
            else:
                print('No se encuentra ningun libro registrado en el catalogo de la biblioteca')
        if m == '1':
            if longitud >0:
                return self.r_libro
            else:
                return 0
    def eliminar_libro_cat(self,ide):
        if ide <= len(self.r_libro) and ide > 0:                  # Si el ide es menor o igual y diferente a 0, removera el libro que se encuentre en indice -1
                print('El libro {} ah sido eliminado de la lista'.format(self.r_libro[ide-1]))
                self.r_libro.remove(self.r_libro[ide-1])  
        else:
            print('Los datos ingresados no se encuentrar dentro del catalogo')
    def agregar_libro_cat(self,libro):
        print(libro)
        self.r_libro.append(libro)                                    
        a = len(self.r_libro)                                  
        self.libros_disponibles_y_no[libro] = True                    # Añadimos el libro y lo colocamo True de que est disponible
        print('El {} ha sido ingresado al catalogo.'.format(libro))
    def libro_disponible(self):
        cat = Catalogo.libros_disponibles_y_no
        lista_de_libros_disponibles = []                       #Lista que almacena todos los libros disponibles
        for x in cat:
            if  cat[x] == True:                                # Si el libro esta True = 'disponible' , guardar en la lista 
                lista_de_libros_disponibles.append(x)
        return lista_de_libros_disponibles                    # entrehar una lista de los libros disponibles

    def busqueda_de_libro(self,ide):
        return self.r_libro[ide]
    
    def busqueda_de_usuario(self,dato):
        if dato in self.libros_disponibles_y_no:
            return dato
    
    def Agregar_usuario_en_lista_de_registro(self,usuario):
        self.r_usuario.append(usuario)                      #Agregamos a los usarios en una lista de los usuarios
        print('El usuario {} ah sido ingresado al Sistema'.format(usuario))

    def Cambiar_estado_de_libro(self,libro):
        self.libros_disponibles_y_no[libro] = False



            
    

def catalogo(opcion_selecionada):
    if opcion_selecionada == 'a':                               # Si la opcion selcionada es a , ejecutar el sig codigo # Agregrar libro ah una lista
        while True:                                             # Solicitar los datos a agregar 
            a = input('Ingrese el Titulo : ')
            b = input('Ingrese el Autor :  ')
            c = input('Ingrese el Genero : ')
            d = input('Ingrese el Num. Pagina: ')
                                                                   # Crear el objeto libro con los datos ingresados
            Catalogo.agregar_libro_cat(Libros(a,b,c,d))                # Agregar los datos del libro al catalogo
            r = input("Desea agregar otro (si)(no) :  ").lower()    # Consultar si quiere agregar otro mas o no
            if r == 'no':                                           # En caso de que el usuario escriba no , se rompe el bucle y vuelve al menu principal
                break
    if opcion_selecionada == 'b':
        while True:   
            print('Estos son los libros que tienes en el catalogo \n¿Cual de todos quieres elimiar?')     
            Catalogo.Registros_de_libros()                             # Manipulapos el objeto catalogo para que nos muesre los datos de libro que tenemos
            ide = int(input('Ingrese el id ah eliminar: '))            # solicitamos un id en este caso es el index del que le mostramos al usuario 
            Catalogo.eliminar_libro_cat(ide)                           # Manipulamos al objeto catalogo , para que elimine dicho libro , entregandole el ide.
            r = input("Desea eliminar otro (si)(no) :  ").lower()      # Una consulta si quiere continuar.
            if r == 'no':
                break
    if opcion_selecionada == 'c':
        while True:
            Catalogo.Registros_de_libros()                             # En el objeto Catalogo le hacemos que haga la accion de mostrar la lista de todos los libros que tenga.
            salir = input('\n¿Desea volver al menu?.Escriba (exit):  ').lower()   # Consulta para salir del codigo
            if salir == 'exit':
                break
lista_usuario = []
def Opc_Usuario(opcion_select):
    if opcion_select == 'a':
        while True:
            a = input('Ingrese su nombre: ')
            b = input('Ingrese su apellido: ')
            Nuevo_Usuario = Usuarios(a,b) 
            Catalogo.Agregar_usuario_en_lista_de_registro(Nuevo_Usuario)                                             # Creamos el objeto Usuario, con los datos que solicitamos previamente
            res = input('Desea ingresar otro usuario en el sistema (si)(no): ')
            # if res == 'mostrar':
            #     for x in Catalogo.r_usuario:
            #         print(x)
            if res == 'no':
                break

    if opcion_select == 'b':
        pass
    if opcion_select == 'c':
        pass
    if opcion_select == 'd':
        pass
    if opcion_select == 'a':
        pass
    if opcion_select == 'e':
        pass

Catalogo = Catalogo_Bibloteca('Catalogo_1')              
ventana = True

while ventana == True:
    print('\t\t.::Bienvenido al Sistema de gestión de la Biblioteca::.\n')
    print('\t1.Catalogo')
    print('\t2.Usuario')
    print('\t3.Salir')
    respuesta = input('\nIngrese un número: ')
    if respuesta == '1':                
        print('a) Añadir Libro al catalogo')          
        print('b) Eliminar Libro del catalogo') 
        print('c) Mostrar Todos los libros del Catalogo') 
        respuesta_1 = input('\nIngrese una opción: ') 
        if respuesta_1 =='a':
            catalogo('a')
        elif respuesta_1 =='b':
            catalogo('b')
        elif respuesta_1 == 'c':
            catalogo('c')

    elif respuesta == '2':
        print('a) Registrar Nuevo Usuario')                                   # Registrar usuario
        print('b) Solicitar un libro')                                        # Prestar libro
        print('c) Devolver libro')                                            # Devolver libro
        print('d) Ver libros disponibles')                                   # Consultar libros disponibles
        print('e) Ver el Historial de prestamos')                            # Ver el historial de préstamos de un usuario.
        opcion_select = input('Ingrese una opción: ')
        if opcion_select == 'a':
            Opc_Usuario('a')

        if opcion_select == 'b':
            print('¿Que libro desea pedir prestado?.')
            print('¬ Contamos con los siguientes libros disponibles: ')
            for x in range(len(Catalogo.libro_disponible())):
                print(x+1,Catalogo.libro_disponible()[x])
            a =(int(input('Ingrese el id del libro a pedir: '))-1)
            b = input('Ingrese su nombre y apellido :   ')
            c = input('Ingrese la fecha del prestamo:   ')
            d = input('Ingrese la fecha la fecha de devolución')
            if a <= len(Catalogo.r_libro) or a >=0:
                if Catalogo.busqueda_de_libro(a) in Catalogo.libro_disponible():
                    if Catalogo.busqueda_de_usuario(b) in Catalogo.r_usuario:
                        print('Usuario esta :D')
                  #  Catalogo.Cambiar_estado_de_libro(Catalogo.busqueda_de_libro(a))
                else:
                    print('El libro no se encuentra disponible')
            # if a <= len(Catalogo.r_libros):
            #     if b in Usuarios.lista_de_usuarios:
            #         pass
                    
    #                prestamo = Prestamos(Catalogo.)
            # if res == 0:
            #     break

        if opcion_select == 'c':
            pass
        if opcion_select == 'd':
            pass
        if opcion_select == 'a':
            pass
        if opcion_select == 'e':
            pass
    elif respuesta == '3':
        print('mensaje de despedida')
        ventana = False
    else:
        print('Error. Has ingresado un número invalido.')
        print('Por favor, ingrese un número dentro de las opciones disponibles.')

