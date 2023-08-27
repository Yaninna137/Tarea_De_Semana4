'''1. Consultar vuelos disponibles.
    ¬ mostar lista de vuelos disponibles
2. Reservar un vuelo.
    ¬ pedir nombre y apellido
    ¬ solicitar el ide del vuelo ah reservar 
    + mostrar un mensaje de cuantos numeros de asinetos disponibles hay en ese vuelo 
    + mostrar mensaje de que se registro , con los datos a mostra
    - crear el objeto pasajero
    - crear el objeto reserva
3. Cancelar una reservación.
    ¬ pedir el nombre y apellido 
    ¬ ingresar el ide de la reserva a cancelar. 
    + mostrar todas las reservas.
    + mostrar mensaje de que su reserva ah sido cancelada
    - buscar el objeto pasajero
    - buscar el objeto reserva 
4. Ver las reservaciones de un pasajero.
    ¬ solitar el nombre y apelido del pasajero a ver
    ¬ mostar las reservas del pasajero
5. Ver la lista de pasajeros en un vuelo.
    ¬ soliciar el ide del vuelo a ver
    + mostrar lista del vuelo en el pasajero
'''
#----------------------------------------------------------------------------------------------
''' objetos creados = avion , pasajero , vuelo y reserva  , guardar en listas temporales
1. Crear vuelos y añadirlos a una lista de vuelos disponibles. Mostrar vuelos disponibles.          ///
    ¬ crear el objeto avion
    ¬ crar los objetos vuelos 3x
    ¬ añadir los vuelos en la lista del objeto avion.
    ¬ llamar el metodo de 'Mostrar_vuelos_disponibles()' del objeto avion  
2. Reservar un vuelo: Al reservar, se crea una nueva reservación y se añade a la lista de reservaciones del vuelo y del pasajero.
    ¬ crear el objeto reserva
    ¬ añadir reserva en el atributo 'lista_de_reservas' del objeto vuelo
    ¬ añadir reserva en el atributo 'lista_de_reservas' del objeto pasajero
3. Cancelar una reservación: Cambia el estado de una reservación a “cancelado”.
    ¬ buscar el objeto pasajero 
    ¬ usar metodo 'cambia estado' en la reserva 
    ¬ buscar objeto reserva
4. Mostrar todas las reservaciones de un pasajero.
    ¬ buscar pasajero
    ¬ llamar metodo 'mostrar_reservas'
5. Mostrar la lista de pasajeros de un vuelo.
    - miar atributo de vuelo
6. Validar que no se puedan sobrepasar el número de asientos de un avión al realizar reservaciones.
7. Validar que un pasajero no pueda reservar el mismo vuelo más de una vez.'''
class Avion:
    def __init__(self,modelo,num_asientos):
        self.modelo = modelo
        self.capacidad = num_asientos  
        self.Lista_vuelos_dispo = []                      # Almacenar todos los vuelos que se crean en estas lista.
    def __repr__(self):
        return f'{self.modelo}.Capcidad de {self.capacidad} asientos'
    
    def Mostrar_vuelos_disponibles(self):
        if len(self.Lista_vuelos_dispo) > 0:
            print('\t'*4,'-- Vuelos disponibles --')         # decoarcion
            for i in range(len(self.Lista_vuelos_dispo)):           # Recorrer los indices de la lista
                print(self.Lista_vuelos_dispo[i])                   # imprimir cada elemento 
            return 1
        else:
            print('No hay vuelo disponible')
            return 0

class Vuelo:
    def __init__(self,num_vuelo,origen,destino,Fecha_hora,Avion_asigando):    # Vuelo(num_vuelo,origen,destino,fecha-hora,Avion asignado)
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = Fecha_hora
        self.Avion_a = Avion_asigando
        self.lista_de_reserva = []
    def __repr__(self):
        return f'{self.num_vuelo}¬. vuelo de Origen:{self.origen}  Destino:{self.destino}  Fecha-hora:{self.fecha_hora}  Avión Asignado:{self.Avion_a.modelo}'
class Pasajero:
    def __init__(self,nombre_apellido,num_pasaporte):    # pasajeros(nombre,numero de pasaporte, lista de vuelos reservados)
        self.nombre = nombre_apellido
        self.num_pasaporte = num_pasaporte
        self.L_Vuelos_Reser = []
    def __repr__(self):
        return f'{self.nombre} {self.num_pasaporte} {self.L_Vuelos_Reser}'
class Reservacion:
    def __init__(self,num_reservacion,pasajero,vuelo,Estado = 'reservado'):
        self.num_r = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = Estado
    def __repr__(self):
        return f'{self.num_r} ¬.Reserva de: {self.pasajero.nombre} en el vuelo: {self.vuelo.num_vuelo}' 

class Almacenamineto_de_datos:
    def __init__(self):
        self.listas_vuelos = []                                    # Almacenamiento de los objetos 
        self.listas_pasajeros = []                                 # Almacenmientos de los objetos pasajeros
        self.lista_reservas = []                                   # Almacenamiento de reservas 
    def mostar_vuelos(self):
        for vuelo in self.listas_vuelos:
            print(vuelo)
avion = Avion('Juan', 50)                                                 # Creamos objeto Avion
Vuelo_1 = Vuelo(1,'Temuco','Santiago','3 de julio|17:30',avion)           # Creamos los vuelos
Vuelo_2 = Vuelo(2,'Temuco','La serena','3 de julio|18:30',avion)          # //
Vuelo_3 = Vuelo(3,'Temuco','Rancagua','3 de julio|18:30',avion)           # //
avion.Lista_vuelos_dispo.append(Vuelo_1)                              # Se guardaran los obj vuelos en una lista del objeto avion
avion.Lista_vuelos_dispo.append(Vuelo_2)                              #   //
avion.Lista_vuelos_dispo.append(Vuelo_3)                              #   //
# avion.Mostrar_vuelos_disponibles()
#---------Alamcenamiento de objetos, para luego ser usado---------------------
A_Sistema = Almacenamineto_de_datos()
A_Sistema.listas_vuelos.append(Vuelo_1)
A_Sistema.listas_vuelos.append(Vuelo_2)
A_Sistema.listas_vuelos.append(Vuelo_3)
#-----------------------------------------------------------------------------------------------
salir = False
while not salir:
    print('Bienvenido al sistema de Gestión Aerolinia')
    print('1.Consultar vuelos disponibles')
    print('2.Reservar un vuelo')
    print('3.Cancelar una reservación')
    print('4.Ver las reservacions de un pasajero')
    print('5.Ver la lista de pasajeros en un vuelo')
    print('6.')
    opcion = int(input(f'Escriba el numero destro del rango de las opciones:  '))
    if opcion == 1:
        volver = False
        avion.Mostrar_vuelos_disponibles()
        while not volver:
            r = input('Para volver al menu escriba (exit).Para salir del sistema (close): ')
            if r == 'exit':
                volver = True
            elif r == 'close':
                volver = True
                salir = True
            else:
                print('Error!.vuelva intentarlo')
    elif opcion == 2:
        avion.Mostrar_vuelos_disponibles()
        if len(avion.Lista_vuelos_dispo) > 0:
            print(f'Contamos con los suiguientes vuelos disponibles del avion {avion.modelo}')
            pregunta = input('¿Desea reservar un vuelo?. Escriba(si) para continuar: ')

            if pregunta == 'si':
                volver = False
                while not volver:
                    ide = (int('Ingrese el numero del vuelo a reservar: ')-1)
                    if ide < 3 and -1 < ide:                       
                        nombre = input('Ingrese su nombre: ')
                        apellido = input('Ingrese su nombre: ')
                    else:
                        print('Error.Numero fuera de rango.Vuelva intentarlo')
        else:
            r = input('Presione enter para volver al menu ')
    elif opcion == 6:
        print('Se ah cerrado el sistema correctamente')
        salir = True
    else:
        print('Error.numero inavlido\nSe ah cerrado el sistema.')
        salir = True