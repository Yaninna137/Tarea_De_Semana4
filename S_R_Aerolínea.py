
class Avion:
    def __init__(self,modelo,num_asientos):
        self.modelo = modelo                #Atributo 1
        self.capacidad = num_asientos       #Atributo 2
        self.Lista_vuelos_dispo = []        #Atributo 3  # Lista vacia ,Su funcion sera Almacenar todos los vuelos disponibles
    def __repr__(self):
        return f'{self.modelo}.Capcidad de {self.capacidad} asientos'
    
    def Mostrar_vuelos_disponibles(self):                   # Cuando se llame este metodo.Mostra una lista de los vulos disponibles
        if len(self.Lista_vuelos_dispo) > 0:                # si el numero de elemntos es mayor que 0, mostrara ell mensaje de "vuelos disponibles" y las lista
            print('\t'*4,'-- Vuelos disponibles --')       
            for i in range(len(self.Lista_vuelos_dispo)):           # Con un for , se recorrera 
                print(self.Lista_vuelos_dispo[i])                   # imprimir cada elemnto en este caso cada vuelo disponible
        else:
            print('No hay vuelo disponible')                #En caso que no cumpla condicion posterior , imprimira solo un mensaje
class Vuelo:
    def __init__(self,num_vuelo,origen,destino,Fecha_hora,Avion_asigando):    # Vuelo(num_vuelo,origen,destino,fecha-hora,Avion asignado)
        self.num_vuelo = num_vuelo                        #Atributo 1
        self.origen = origen                              #Atributo 2
        self.destino = destino                            #Atributo 3
        self.fecha_hora = Fecha_hora                      #Atributo 4
        self.Avion_a = Avion_asigando                     #Atributo 5
        self.lista_de_reserva = []                        #Atributo 6  #Con lista vacia ,#Su funcion sera 
        self.Estado = True                                #Atributo 7 # Su funcion es que cuando se llegue al tope de reservas (num-asinetos del avion) , este se ponga falso y mostrar que este vuelo ya no esta disponible                           
    def __repr__(self):
        return f'{self.num_vuelo}¬. vuelo de Origen:{self.origen}  Destino:{self.destino}  Fecha-hora:{self.fecha_hora}  Avión Asignado:{self.Avion_a.modelo}'
class Pasajero:
    def __init__(self,nombre_apellido,num_pasaporte):    # pasajeros(nombre,numero de pasaporte, lista de vuelos reservados)
        self.nombre = nombre_apellido                     #Atributo 1
        self.num_pasaporte = num_pasaporte                #Atributo 2
        self.L_Vuelos_Reser = []                          #Atributo 3 #lista vacia#Su funcion ser alamcenar todas las reservas del pasajero
    def __repr__(self):
        return f'{self.nombre} {self.num_pasaporte} {self.L_Vuelos_Reser}'
class Reservacion:
    def __init__(self,num_reservacion,pasajero,vuelo,Estado = 'reservado'):
        self.num_r = num_reservacion                      #Atributo 1
        self.pasajero = pasajero                          #Atributo 2
        self.vuelo = vuelo                                #Atributo 3
        self.estado = Estado                              #Atributo 4
    def __repr__(self):
        return f'{self.num_r} ¬.Reserva de: {self.pasajero.nombre} en el vuelo: {self.vuelo.num_vuelo}' 
# -Esta clase servira para almacenar todos los objetos que se crean: avion, pasajero, vuelo, reserva.
class Almacenamineto_de_datos:
    def __init__(self):
        self.Almacenamiento_Avion = []        # Atributo 1    # Almacenar cada objeto Avion  
        self.Almacenamineto_Vuelo = []        # Atributo 2    # // Vuelos
        self.Almacenamiento_Pasajero = []     # Atributo 3    # // Pasajeros
        self.Almacenamiento_Reserva  = []     # Atributo 4    # // Rervaciones
