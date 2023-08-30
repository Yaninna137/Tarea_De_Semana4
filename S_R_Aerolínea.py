
class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo                #Atributo 1
        self.capacidad = num_asientos       #Atributo 2
        self.Lista_vuelos_dispo = []        #Atributo 3  # Lista vacia ,Su funcion sera Almacenar todos los vuelos 'Disponibles'
        self.Lista_de_vuelos_creados = []   #Atributo 4 # array vacia , almacenara Todos los objetos vuelos del avion
    def __repr__(self):
        return f'---- Modelo: {self.modelo},Num.Asientos: {self.capacidad}'
    
    def Agregar_vuelo_disponible(self, vuelo):
        self.Lista_vuelos_dispo.append(vuelo)
class Vuelo:
    def __init__(self, num_vuelo, origen, destino, Fecha_hora, Avion_asigando):    # Vuelo(num_vuelo,origen,destino,fecha-hora,Avion asignado)
        self.num_vuelo = num_vuelo                        #Atributo 1
        self.origen = origen                              #Atributo 2
        self.destino = destino                            #Atributo 3
        self.Fecha_hora = Fecha_hora                      #Atributo 4
        self.Avion_asigando = Avion_asigando                     #Atributo 5
        self.lista_de_reserva = []                        #Atributo 6  #Con lista vacia ,#Su funcion sera 
        self.Estado = True                                #Atributo 7 # Su funcion es que cuando se llegue al tope de reservas (num-asinetos del avion) , este se ponga falso y mostrar que este vuelo ya no esta disponible                           
    def __repr__(self):
        return f'{self.num_vuelo}¬. vuelo de Origen:{self.origen}  Destino:{self.destino}  Fecha-hora:{self.Fecha_hora}  Avión Asignado:{self.Avion_asigando.modelo}'
    def Agregar_pasajero(self,r_pasajero):
        self.lista_de_reserva.append(r_pasajero)
        
    def mostrar_pasajero(self):
        if len(self.lista_de_reserva) > 0:
            for registro in self.lista_de_reserva:
                print('¬ ',registro.pasajero)
        else:
            print('No hay ningun pasajero en este vuelo')
class Pasajero:
    def __init__(self, nombre_apellido, num_pasaporte):    # pasajeros(nombre,numero de pasaporte, lista de vuelos reservados)
        self.nombre_apellido = nombre_apellido                     #Atributo 1
        self.num_pasaporte = num_pasaporte                #Atributo 2
        self.L_Vuelos_Reser = []                          #Atributo 3 #lista vacia#Su funcion ser alamcenar todas las reservas del pasajero
    def __repr__(self):
        return f'{self.nombre_apellido} {self.num_pasaporte} {self.L_Vuelos_Reser}'
    def Agregar_historial(self,reserva):
        self.L_Vuelos_Reser_Vuelos_Reser.append(reserva)
    def Mostrar_lista_de_reservas_del_pasajero(self):
        if len(self.L_Vuelos_Reser_Vuelos_Reser) > 0:
            for registro in self.L_Vuelos_Reser:
                print('¬ ',registro.vuelos)
        else:
            print('No hay ningun pasajero en este vuelo')     

class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo, Estado = 'reservado'):
        self.num_reservacion = num_reservacion                      #Atributo 1
        self.pasajero = pasajero                          #Atributo 2
        self.vuelo = vuelo                                #Atributo 3
        self.Estado = Estado                              #Atributo 4        
    def __repr__(self):
        return f'{self.num_reservacion} ¬.Reserva de: {self.pasajero.nombre_apellido} en el vuelo: {self.vuelo.num_vuelo}.Estado: {self.Estado}' 
# -Esta clase servira para almacenar todos los objetos que se crean: avion, pasajero, vuelo, reserva.
    def cancelar_reserva(self):
        self.Estado = 'Cancelado'

class Almacenamineto_de_datos:
    def __init__(self):
        self.Almacenamiento_Avion = []        # Atributo 1    # Almacenar cada objeto Avion  
        self.Almacenamineto_Vuelo = []        # Atributo 2    # // Vuelos
        self.Almacenamiento_Pasajero = []     # Atributo 3    # // Pasajeros
        self.Almacenamiento_Reserva  = []     # Atributo 4    # // Rervaciones

    def mostrarAviones(self):
        if len(self.Almacenamiento_Avion) > 0:
            print("Aviones disponibles:")
            for index, avion in enumerate(self.Almacenamiento_Avion):
                print(f"{index + 1}.{avion}")
        else:
            print('No se encuentra nigún avión registrado en el sistema')
    def mostrar_TVuelos(self):
        if len(self.Almacenamineto_Vuelo) > 0:
            for i,cada_avion in enumerate(self.Almacenamiento_Avion):
                print(f'-------{i+1}.{cada_avion}')
                for x ,cada_vuelo in enumerate(cada_avion.Lista_de_vuelos_creados):
                    print(f'{x+1} ¬. {cada_vuelo}')

        else:
            print('No Hay ningun registro de vuelo')
    def mostrar_vuelos_disponibles(self):
        if len(self.Almacenamineto_Vuelo) > 0:
            for i,cada_avion in enumerate(self.Almacenamiento_Avion):
                print(f'-------{i+1}.{cada_avion}')
                if len(cada_avion.Lista_de_vuelos_creados) > 0:
                    for x ,cada_vuelo in enumerate(cada_avion.Lista_de_vuelos_creados):
                        print(f'{x+1} ¬. {cada_vuelo}')
                else: 
                    print('No hay vuelos registrados,para este avión')
        else:
            print('No hay vuelos disponibles :(')
    def mostrar_Tpasajeros(self):
        if len(self.Almacenamiento_Pasajero) > 0:
            for i,cada_pasajero in enumerate(self.Almacenamiento_Pasajero):
                print(f'-------{i+1}.{cada_pasajero.nombre_apellido}')
        else:
            print('No hay Pasajeros registrados en el sistema ')
    def Verificar_disponibilidad_vuelo(self,indice):
        if len(self.Almacenamineto_Vuelo) > 0:
            return self.Almacenamineto_Vuelo[indice]
        else:
            return -1 # el vuelo no se encuntra
    def Buscar_pasajero(self, Pasajero):
        # Buscar al usuario ingresado en la lista de usuarios registrados
        for pasajero in self.Almacenamiento_Pasajero:
            if pasajero.nombre_apellido == Pasajero.nombre_apellido:
                return self.Almacenamiento_Pasajero.index(pasajero)                     # Si se encuentra al usuario, devolver su índice en la lista
        
        return -1  # Si no se encuentra al usuario, devolver -1  
T_objetosC = Almacenamineto_de_datos()

def crearAvion():
    modelo = input("Ingrese el modelo del avion: ")
    numAsientos = int(input("Ingrese el numero de asientos del avion: "))
    avion = Avion(modelo, numAsientos)
    T_objetosC.Almacenamiento_Avion.append(avion)
    print(f"El avion de modelo '{avion.modelo}',con capacidad para {avion.capacidad} pasajeros. \nHa sido correctamente registrado")    
def crearVuelo():
    print('Estos son los aviones que se encuentran en el registro')
    T_objetosC.mostrarAviones()
    respAvion = int(input("Ingrese el numero de avion para crear un nuevo vuelo: ")) - 1
    if respAvion >= 0 and respAvion <= len(T_objetosC.Almacenamiento_Avion):

        Avion_Asigando = T_objetosC.Almacenamiento_Avion[respAvion]     # en el objeto t_objetos llamos su atributo alamcenmiento_avion (donde se encuntra almacenado cada avion) , y le colocamos el indice ingresado por el usuario
        print('Este avion cuenta con {} vuelos creados.'.format(len(Avion_Asigando.Lista_de_vuelos_creados)))
        for i ,vuelos_creados in enumerate(Avion_Asigando.Lista_de_vuelos_creados):
            print(f'{i +1} ¬. {vuelos_creados}')
        origen = input("Ingrese la cuidad de origen del vuelo: ")
        destino = input("Ingres la cuidad de destino del vuelo: ")
        fecha_hora = input("Ingrese la fecha y hora del vuelo: ")

        Num_vuelo = (len(Avion_Asigando.Lista_de_vuelos_creados))   #ver cuantos elementos tine la lista_de_vuelos_creados, para que cunado se agrege el avion al sistema , sea con el numero siguiente de los elemtos anterios
        vuelo = Vuelo(Num_vuelo +1, origen, destino, fecha_hora,Avion_Asigando)
        #AGREGAR A VUELO DISPONIBLE por defaut 
        Avion_Asigando.Agregar_vuelo_disponible(vuelo)
        # GUARDAR EL OBJETO VUELO EN almacenamineto vuelo y en en el objeto avion
        T_objetosC.Almacenamineto_Vuelo.append(vuelo)
        Avion_Asigando.Lista_de_vuelos_creados.append(vuelo)
        print(F'{vuelo} \n Se ah registrado en el sistema')
    else:
        print('Error.Numero Fuera de rango.\nIngrese un numero valido')

def CrearReserva():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    if len(T_objetosC.Almacenamiento_Avion) > 0 and len(T_objetosC.Almacenamineto_Vuelo) > 0:
        print(f'Estimado {nombre} {apellido} Contamos con los siguintes vuelos\n ¿Cuall desea reservar?: ')
        for i,vuelo in enumerate(T_objetosC.Almacenamineto_Vuelo):
            print(f'{i+1} ¬. {vuelo}')
        while True:
            r = int(input('Ingrese un numero de vuelo a reservar: '))-1  
            if r >= 0 and r <= len(T_objetosC.Almacenamineto_Vuelo):
                vuelo_seleccionado = T_objetosC.Verificar_disponibilidad_vuelo(r)
                num_asiento_avion = T_objetosC.Almacenamineto_Vuelo[r].Avion_asigando.capacidad         #en el objeto almacenamiento.llamos el atributo Almacenamineto_Vuelo' qe es una lisata de los  objeto vuelos.A continuacion especificamos que objeto vuelo queremos usanos el 'r'
                                                                                                        # 'r' seria el index .Ya con el obejto vuelo indicaco .Llamos el atributo del objeto vuelo que es'Avion_asigando'
                                                                                                        # este atributo contiene al objeto avion.
                                                                                                        # por ultimo en este objeto avion llamos su atributo 'capacidad', el cual gurda el numero de asinetos que tiene :D
                long_reserva = len(T_objetosC.Almacenamineto_Vuelo[r].lista_de_reserva)
                if long_reserva <= num_asiento_avion:     # arreglar para que no entre ah esa condicion
                    cuantos_tiene_now = len(vuelo_seleccionado.lista_de_reserva)
                    print(f'El vuelo dispone de {(num_asiento_avion) - (cuantos_tiene_now )} de cupos:')
                    print(f'¿Desea usted reservar este vuelo ?')
                    consulta = input('Ingrese (si).para confirmar reserva (Cancelar)para caso contrario: ')
                    if consulta == 'si':
                        #codigo para encontrar los la posicion del objeto avion , para crearla como ide para el passport        
                        indice = T_objetosC.Almacenamineto_Vuelo[r].Avion_asigando 
                        contador = 0
                        for avion_b in T_objetosC.Almacenamiento_Avion:
                            contador += 1
                            if avion_b == indice:
                                break
                               
                        # creacion del objeto pasajero 
                        # y reservación
                        passport = f'#{contador}{vuelo_seleccionado.num_vuelo}{long_reserva +1}'              #creacion del numero de pasaporte {id.avion}{id.vuelo}{id.reserva}{id.modelo_deavion}'
                        Pasajero_n = Pasajero(f'{nombre} {apellido}',passport)
                        Reservacion_n = Reservacion(long_reserva + 1,Pasajero_n,vuelo_seleccionado,'Reservado')
                        #Guardar reservas en los objetos.
                        T_objetosC.Almacenamiento_Reserva.append(Reservacion_n)                        #Guardar registro(reserva) en el atributo del obejto Almacenamineto
                        T_objetosC.Almacenamiento_Pasajero.append(Pasajero_n)
#                        vuelo_seleccionado.lista_de_reserva.append(Reservacion_n)                      #Guardar registro(reserva) en el atributo del obejto vuelo

                        Pasajero_n.Agregar_historial(Reservacion_n)                                #Guardar registro(reserva) en el atributo del obejto pasajero
                        vuelo_seleccionado.Agregar_pasajero(Reservacion_n)
                        print(f'Su vuelo ah sido reservado. su numero de pasaporte es:{passport}')
                        print(vuelo_seleccionado.lista_de_reserva)
                        print(Pasajero_n.L_Vuelos_Reser)
                        print(T_objetosC.Almacenamiento_Reserva)
                        break
                    else:
                        break
                else:
                    print('Estan completas las reservas de este vuelo .\n¿Desea eligir otro vuelo? (si) (no) : ')
        else:
            print('Error.El numero ingresado se encuentra fuera de rango.Vuelva intentarlo')
    else:
        print(f'Estimado {nombre} {apellido} , en este momento, no hay vuelos disponibles para reservar' )
salidad =  False
while not salidad:
    print("----------------MENÚ PRINCIPAL.----------------")
    print("1.- Avión.")
    print("2.- Vuelo.")
    print("3.- Reserva.")
    print("4.- Salir.")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        print("a) Registrar nuevo avión.")
        print("b) Ver lista de aviones.")
        subopcion = input("Seleccione una opción: ")
        if subopcion == "a":
            crearAvion()
            while True:
                r = input('Desea crear otro avion? (si)(no): ')
                if r == 'si':
                    crearAvion()
                else:
                    break
        elif subopcion == "b":
            T_objetosC.mostrarAviones()

    elif opcion == 2:
        print("a) Registrar nuevo vuelo.")
        print("b) Ver vuelos disponibles.")
        print("c) Lista de vuelos.")
        print("d) Lista de pasajeros en un vuelo.")
        subopcion2 = input("Seleccione una opcion: ")
        if subopcion2 == "a":
            if len(T_objetosC.Almacenamiento_Avion) > 0:
                crearVuelo()
                while True:
                    r = input('Desea crear otro vuelo? (si)(no): ')
                    if r == 'si':
                        crearVuelo()
                    else:
                        break
            else:
                print('No hay registro de algún avión.\nPor favor registre un avión antes de crear un vuelo')
        elif subopcion2 == 'b':
            T_objetosC.mostrar_vuelos_disponibles()
        elif subopcion2 == "c":
            T_objetosC.mostrar_TVuelos()
        elif subopcion2 == "d":
            T_objetosC.mostrar_TVuelos()
            r = int(input('numero: ')) -1
            T_objetosC.Almacenamineto_Vuelo[r].mostrar_pasajero()
            # antes de su creacion , se requiere registro de reserva.
    
    elif opcion == 3:
        print("a) Hacer una reserva.")
        print("b) Cancelar una reserva.")
        print("c) Lista de reservas de un pasajero.")
        print("d) Lista de pasajeros en un vuelo.")
        subopcion3 = input("Seleccione una opción: ")

        # HACER UNA RESERVA 
        if subopcion3 == "a":
            CrearReserva()
        # CANCELAR RESERVA: 
        elif subopcion3 == "b":
            print('Ingrese los siguientes datos para Cancelar su reserva: ')
            nombre = input('Ingrese el nombre: ')
            apellido = input('Ingrese el apellido: ')
            index = T_objetosC.Buscar_pasajero(f'{nombre} {apellido}')
            if index != -1:
                # debes bucar y cancelar el dato
                pasajero_n = T_objetosC.Almacenamiento_Pasajero[index]
                print(f'El historial del usuario {pasajero_n}:')
                pasajero_n.Mostrar_lista_de_reservas_del_pasajero()
                print('Cual reservas deseas cancelar?.Ingrese con ')
            else:
                print('No se encuentra dicho usuario')

                r = input('¿Desea veer la lista de usarios ingresados en sistema?(si)(no): ')
                if r =='si':
                    log = len(T_objetosC.Almacenamiento_Pasajero)
                    if log > 0:
                        for x in range(log):
                            print(x+1,'¬.',T_objetosC.Almacenamiento_Pasajero[x].nombre_apellido)
                    else:
                        print('No hay usuario Registrado')
            print('Cancelar una reserva ')
        # LISTA DE RESERVAS DE UN PASAJERO
        elif subopcion3 == "c":
            print('Estos son los pasejeros que estan el sistema: ')
            T_objetosC.mostrar_Tpasajeros()
            r = int(input('numero: '))-1
            T_objetosC.Almacenamiento_Pasajero[r].Mostrar_lista_de_reservas_del_pasajero()
        # LISTAS DE PASAJEROS EN UN VUELO
        elif subopcion3 == "d":
            print("Lista de pasajeros en un vuelo")

    elif opcion == 4:
        print("Saliendo del sistema...")
        salidad = True
