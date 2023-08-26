class Libros():
    def __init__(self,titulo,autor,genero,num_pagina):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.num_pagina = num_pagina
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} con{self.num_pagina} páginas,{self.genero}"
         
class Usuarios():
    def __init__(self,nombre,apellido,):
        self.f_registro = "Imp_date(fecha de este registro)"
        self.nombre = nombre
        self.apellido = apellido
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
    def libro_disponible(self):
        pass

class Catalogo_Bibloteca(): #registro
    def __init__(self,nombre):
        self.nombre = nombre
        self.r_libro = []
        self.r_usuario = None
        self.r_prestamo = None

    def Registros_de_libros(self):
        for x in range(len(self.r_libro)):                        # Con un for recorremos los libros , que se encuntren en la lista de registros del catalogo
            print('{}.{}'.format(x+1,self.r_libro[x]))            # mostar cada libro

    def eliminar_libro_cat(self,ide):
        if ide <= len(self.r_libro) and ide > 0:                  # Si el ide es menor o igual y diferente a 0 ejecuta el siguiente codigo
            for x in range(len(self.r_libro)):                                #Con un for recorremos cada elemneto 
                if (ide-1) == x:                                                 # en el ide le restamos 1 ,en caso que cumpla dicha condiccion ,mostrar un mensaje y removera el libro de la lista
                    print('El libro {} ah sido elimidado del Catalogo'.format(self.r_libro[x]))
                    self.r_libro.remove(self.r_libro[x])
                    break                                                        #Rompemos el bucle para que no ejecute
        else:
            print('Los datos ingresados no se encuentrar dentro del catalogo')

        pass
    def agregar_libro_cat(self,libro):
        self.r_libro.append(libro)                                    #Añadir libro
        print('El {} ha sido ingresado al catalogo.'.format(libro))


def catalogo(opcion_selecionada):
    if opcion_selecionada == 'a':                               # Si la opcion selcionada es a , ejecutar el sig codigo # Agregrar libro ah una lista
        while True:                                             # Solicitar los datos a agregar 
            a = input('Ingrese el Titulo : ')
            b = input('Ingrese el Autor :  ')
            c = input('Ingrese el Genero : ')
            d = input('Ingrese el Num. Pagina: ')
            Libro_1 = Libros(a,b,c,d)                          # Crear el objeto libro con los datos ingresados
            Catalogo.agregar_libro_cat(Libro_1)                # Agregar los datos del libro al catalogo
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
            catalogo(respuesta_1)
        elif respuesta_1 =='b':
            catalogo(respuesta_1)
        elif respuesta_1 == 'c':
            catalogo(respuesta_1)

    elif respuesta == '2':
        print('a) Registrar Nuevo Usuario')                                   # Registrar usuario
        print('b) Solicitar un libro')                                        # Prestar libro
        print('c) Devolver libro')                                            # Devolver libro
        print('d) Ver libros disponibles')                                   # Consultar libros disponibles
        print('e) Ver el Historial de prestamos')                            # Ver el historial de préstamos de un usuario.
    elif respuesta == '3':
        print('mensaje de despedida')
        ventana = False
    else:
        print('Error. Has ingresado un número invalido.')
        print('Por favor, ingrese un número dentro de las opciones disponibles.')

