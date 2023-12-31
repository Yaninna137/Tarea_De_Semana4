class Libros:
    def __init__(self,titulo,autor,num_pagina):
        self.titulo = titulo                               #Atributo 1    
        self.autor  = autor                                #Atributo 2
        self.num_pag = num_pagina                          #Atributo 3
    def __repr__(self):
        return f'El libro "{self.titulo}" por {self.autor}.Cuenta con {self.num_pag} páginas'       #Retornar una cadena 
class Usuarios:
    def __init__(self,nombre,apellido):
        self.nombre = nombre                               #Atributo 1
        self.apellido = apellido                           #Atributo 2
        self.Historial_Prestamo = []                       #Atributo 3 lista vacia, servira para almacenar todos los historiales
    def __repr__(self):
        return f'{self.nombre} {self.apellido}'                   #Retornar una cadena de texto
    
    def Agregar_HU(self,r_prestamo):                           #metodo, cada vez que se llame este comportamineto dependiendo del objeto este hara:
        self.Historial_Prestamo.append(r_prestamo)             # agregar un Registramos historial , con el argumento que le den 

    def mostrar_historial(self):                          #metodo sin solicitar un argumento nuevo 
        if len(self.Historial_Prestamo) > 0:              #Si la cantidad de elmentos del array es mayor que 0:
            for x in self.Historial_Prestamo:             #Recorrera casa elemnto que este en el array, y lo imprimira por pantalla      
                print('°/',x) 
        else:                                             #Caso contrario , imprimira un mensaje 
            print('No hay ningun historial del usuario')
class Prestamos:
    def __init__(self,usuario,libro,f_prestamo,f_devolucion):
        self.Registro_prestamo = []                      #Atributo 1 
        self.usuario = usuario                           #Atributo 2
        self.libro = libro                               #Atributo 3
        self.f_prestamo = f_prestamo                     #Atributo 4
        self.f_devolver = f_devolucion                   #Atributo 5
        self.Entregas_Anonimas = []                      #Atributo 6 .Listas vacia , cuando el usuario no se encuntre en la lista, se agregar el historia
    def __repr__(self) -> str:
        return f'{self.usuario.nombre} {self.usuario.apellido} {self.libro} {self.f_prestamo} {self.f_devolver}'    
    def añadir_his_ah_usuario(self,usuario):          # mandele el dato al usario de su registro
        registro =  f'El usuario {self.usuario.nombre} {self.usuario.apellido}  pidio prestado: {self.libro}, el dia {self.f_prestamo}.Fecha ah devolver: {self.f_devolver}'
        usuario.Agregar_HU(registro)
        self.Registro_prestamo.append(registro)

    def añadir_hist_devolucion(self,usuario = 'anonimo'):
        if usuario != 'anonimo':
            registro =  f'El usuario {self.usuario} devolvio el {self.libro}, el dia {self.f_prestamo}.'
            usuario.Agregar_HU(registro)
            self.Registro_prestamo.append(registro)
        else:
            registro =  f'El libro {self.libro.titulo} fue devuelo el dia {self.f_prestamo} por un usuario desconocido/anonimo.'
            self.Entregas_Anonimas.append(registro)
            self.Registro_prestamo.append(registro)
class Catalogo_Bib:
    def __init__(self):
        self.lista_librosCB = []                                # Atributo alamacenmineto para los objeto libros que se creen 
        self.Estado_librosCB_D = {}                             # Atributo de almancenamineto que se tendra cada objeto del libro como clave y en valor Tre or False # Si esta disponible o no 
        self.lista_UsuariosR = []                               # Atributo alamacenmineto para los objeto libros que se creen 
    def Agregar_LCB(self,libro):
        self.lista_librosCB.append(libro)                       #Agregar al array a el objeto libro crado 
        self.Estado_librosCB_D[libro] = True                    #Agregar al diccionario el libro como clave y como valor "defaut " True
    def Agregar_UCB(self,usuario):
        self.lista_UsuariosR.append(usuario)                    #Agregar al array el cada objeto usuario creado 
    def Eliminar_LCB(self,ide):
        self.Estado_librosCB_D.pop(self.lista_librosCB[ide])       #Eliminar libro del diccionario de disponibilidad
        self.lista_librosCB.remove(self.lista_librosCB[ide])       #Eliminar libro de lista 
    def Cambiar_Estado(self,libro):                               #Cambiar estado del libro true:disponible, false: no disponible
        if self.Estado_librosCB_D[libro] == False:
            self.Estado_librosCB_D[libro] = True
        else:
            self.Estado_librosCB_D[libro] = False
    def Libros_disponibles(self):                                #Entegar una lista de los libros disponibles

        contador = 0                                         #Creamos una varibale acumulador con valor inicial 0   
        log = len(self.Estado_librosCB_D)                    #Contar los elemntos del diccionario
        libros_disponibles = []                              # un array vacion , para almacenar los libros disponibles
        if log > 0:                                                                  #Si la longitud del libro es mayor que 0 , recorrera con un for cada clave 'libro'
            for i in self.Estado_librosCB_D:
                contador += 1                                                        #por caa ciclo que se haga se sumara 1
                if self.Estado_librosCB_D[i] == True:                                # Si el liblo que se esta con el valor True:  colocaremos el libro en lista 'libros_disponibles'
                    libros_disponibles.append(f'{contador}. {self.lista_librosCB[contador -1]}')        # para agregar , se busca en la lista general donde esten todos los libros y llamamos el libro que se encuntre en el idex indicado , por ello creamos el contador 
                                                            
            if len(libros_disponibles) >0:                        # Luego que se termine el for s verifica si se agregar elmentos a la lista , y si hay entonces 
                return libros_disponibles                      #Retornara una lista                             
            else:
                return '0'                                   # En caso de no enontrar ningun dato retornar un string '0'
        else: 
            return '0'                               # En caso de que la longitud del diccionario sea 0 este retornna un string '0'
 
    def Mostra_libros(self):
        if len(self.lista_librosCB) > 0: 
            for i in range(len(self.lista_librosCB)):
                print(i+1,'.-',self.lista_librosCB[i])
        else:
            return -1                                        # Si no encuntra ningun libro por mostrar , retornara -1
    def Buscar_usuario(self, nombre, apellido):
        # Buscar al usuario ingresado en la lista de usuarios registrados
        for usuario in self.lista_UsuariosR:
            if usuario.nombre == nombre and usuario.apellido == apellido:
                return self.lista_UsuariosR.index(usuario)                     # Si se encuentra al usuario, devolver su índice en la lista
        
        return -1  # Si no se encuentra al usuario, devolver -1    
    def Buscar_libro(self,titulo,autor):
        for libro in self.lista_librosCB:
            if libro.titulo == titulo and libro.autor == autor:
                return self.lista_librosCB.index(libro)
        return -1 # En caso de no encontra el libro

Catalogo = Catalogo_Bib()
salir = True
while salir == True:
    print(' ¬ '*30,'\n','\t'*4,'Bienvenido','\n',' ¬ '*30)
    print('1.Registrar Usuario')
    print('2.Añadir libro al catalogo')
    print('3.Eliminar libro al catalogo')
    print('4.Solicitar libro.')
    print('5.Devolución de libro')
    print('6.Libros disponibles')
    print('7.Veer historial del Usuario')
    print('8.Salir')
    opcion = input('Ingrese un numero: ')
    print('° '*30)
    if opcion == '1':
        print('Porfavor ingrese los siguientes datos para completar sus registro:')
        while True:
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            Persona = Usuarios(nombre,apellido)
            Catalogo.Agregar_UCB(Persona)
            print(f'El usuario {Persona.nombre} {Persona.apellido} ah sido ingresado al sistema')
            respuesta = input('¿Desea agregar otro usuario? (si)(no): ').lower()
            if respuesta == 'si' or respuesta =='no':
                if respuesta == 'no':
                    break
            else:
                print('Error.dato invalido.Salida forzada')
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
                print('Error.Dato invalido.Salida Forzada ')
                break
    if opcion == '3':
        if Catalogo.Mostra_libros() != -1:
            print('Contamos con los siguientes libros:')
            while True:
                respuesta = (int(input('Ingrese el id del libro ah eliminar.Para salir ingrese (0): '))-1)
                if respuesta <= len(Catalogo.lista_librosCB) and respuesta != 0:
                    alerta = input('Estas seguro de eliminar este libro (si)(no):')
                    if alerta == 'si':
                        Catalogo.Eliminar_LCB(respuesta)
                        print('El libro ah sido eliminado del sisteme')
                    else:
                        break
                else:
                    break
        else:
            print('No hay registro de libros en el Catalogo')

    if opcion == '4':
        if len(Catalogo.lista_librosCB) > 0:
            print('¿Que libro quieres solicitar?.Contamos con los suiguientes libro: ')
            for x in range(len(Catalogo.lista_librosCB)):
                print(x+1,'¬.',Catalogo.lista_librosCB[x])
            while True:
                ide = int(input('Ingrese el ide del libro ah solicitar: '))-1
                if ide <= len(Catalogo.lista_librosCB) and ide >= 0:  
                    s_libro = Catalogo.lista_librosCB[ide]
                    if Catalogo.Estado_librosCB_D[s_libro] == True:
                        print('El libro se encuentra disponible.Porfavor ingrese los suiguientes datos.\n')
                        nombre = input('Ingrese el nombre: ')
                        apellido = input('Ingrese el apellido: ')
                        index = Catalogo.Buscar_usuario(nombre, apellido)
                        if index != -1:
                            usuario = Catalogo.lista_UsuariosR[index]
                            fecha_prestamos = input('Ingrese la fecha del Prestamo   : ')
                            fecha_devolucion = input('Ingrese la fecha del devolucion : ')
                            Prestar_libro = Prestamos(usuario,s_libro,fecha_prestamos,fecha_devolucion)
                            Prestar_libro.añadir_his_ah_usuario(usuario)                                   # en el objeto prestamos le pedimos que relice la accion , entregandole el usuario ,para que el usuario tenga el registro
                            Catalogo.Cambiar_Estado(s_libro)                                                 # en el objeto de catalogo , cambiamos el estaddo del libro ah false( de que ya no esta disponible)
                            print('Se ha relializado el registro correctamente')
                            respuesta = input('Desea hacer otro registro?(si)(no): ')
                            if respuesta == 'si' or respuesta == 'no':
                                if respuesta == 'no':
                                    break
                            else:
                                print('Error.salida forzada')
                                break
                        else:
                            print('Lo sentimos el usuario ingresado no se encuentra en el sistema.')
                            break
                    else:
                        print('Libro no disponible :(')
                        break
                else:
                    print('Error.El numero ingresado esta fuera de rango')
                    break
        else:
            print('Lo sentimos no contamos con ningun libro en el catalgo ahún.')      
    if opcion == '5':
        while True:
            if len(Catalogo.lista_librosCB) > 0:
                print('\n----Ingrese los datos. para completar la devolucion de libro---\n')
                print('Estos son los libros que se encuntrarn prestados: ')
                for libro in Catalogo.Estado_librosCB_D:
                    if Catalogo.Estado_librosCB_D[libro] == False:
                        print('  ¬ ',libro)
                titulo = input('Ingrese el titulo del libro: ')
                autor = input('Ingrese el nombre del author: ')
                index = Catalogo.Buscar_libro(titulo, autor)
                if index != 1:
                    d_libro = Catalogo.lista_librosCB[index]
                    d_nombre = input('Ingrese el nombre del usuario   :')
                    d_apellido =input('Ingrese el apellido del usuario  :')
                    index_us = Catalogo.Buscar_usuario(nombre,apellido)
                    if index_us != 1:
                        continue
                    else:
                        print('AVERTENCIA: Este usuario no se encuentra en en el sistema.Por ende se registrara como anonimo')
                    fecha_prestamo = input('Ingrese la fecha en que fue prestado:')
                    fecha_devolucion = input('Ingrese la fecha entrega :')
                    index_us = Catalogo.Buscar_usuario(nombre,apellido)
                    if index_us != 1:
                        d_usuario = Catalogo.lista_UsuariosR[index_us]
                        Devolucion = Prestamos(d_usuario,d_libro,fecha_prestamo,fecha_devolucion)
                        Devolucion.añadir_hist_devolucion(d_usuario)
                        Catalogo.Cambiar_Estado(d_libro)
                        print('Se completo el registro de devolución')
                        print(Devolucion,'\n')
                        r = input('Desea agregar otra devolución (si)(no): ').lower()
                        if r == 'si' or r == 'no':
                            if r == 'no':
                                break
                        else:
                            print('Error.')
                            break
                    else:
                        Devolucion = Prestamos('anonimo',d_libro,fecha_prestamo,fecha_devolucion)
                        Catalogo.Cambiar_Estado(d_libro)
                        print('Se completo el registro de devolución, pero como no conside con los datos ingresados del usuario , fue registrado en formato anonimo.')
                        break
                else:
                    print('El libro no se encuentra dento del sistema del catalogo.Vuelva')
                    r = print('Desea volver intentarlo? (si)para continuar (no) para volver al menu:  ')
                    if r == 'si':
                        continue
                    elif r == 'no' or r != 'si':
                        break
            else: 
                print('Tenemos todos los libros disponibles. Por ende no hay registro para devolver nada ')
                break
    if opcion == '6':
        if '0' == Catalogo.Libros_disponibles():
            print('No hay libros disponibles')
        else:
            for i in Catalogo.Libros_disponibles():
                print(i)
        r = input('Para volver al menu presione ''enter'' o escriba algo:')
    if opcion == '7':
        print('Ingrese los siguientes datos para ver el historial del usuario')
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        index = Catalogo.Buscar_usuario(nombre, apellido)
        if index != -1:
            usuario = Catalogo.lista_UsuariosR[index]
            print(f'El historial del usuario {usuario}:')
            usuario.mostrar_historial()
        else:
            print('No se encuentra dicho usuario')

            r = input('¿Desea veer la lista de usarios ingresados en sistema?(si)(no): ')
            if r =='si':
                log = len(Catalogo.lista_UsuariosR)
                if log > 0:
                    for x in range(log):
                        print(x+1,'¬.',Catalogo.lista_UsuariosR[x].nombre, Catalogo.lista_UsuariosR[x].nombre)
                else:
                    print('No hay usuario Registrado')
    if opcion == '8':
        break
    if opcion not in ['1','2','3','4','5','6','7','8']:
        print('Error!.Ingrese un numero valido')
