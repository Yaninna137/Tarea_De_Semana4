
class Avion:
    def __init__(self, modelo, num_asientos):
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
class Pasajero:
    def __init__(self, nombre_apellido, num_pasaporte):    # pasajeros(nombre,numero de pasaporte, lista de vuelos reservados)
        self.nombre_apellido = nombre_apellido                     #Atributo 1
        self.num_pasaporte = num_pasaporte                #Atributo 2
        self.L_Vuelos_Reser = []                          #Atributo 3 #lista vacia#Su funcion ser alamcenar todas las reservas del pasajero
    def __repr__(self):
        return f'{self.nombre_apellido} {self.num_pasaporte} {self.L_Vuelos_Reser}'
class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo, Estado = 'reservado'):
        self.num_reservacion = num_reservacion                      #Atributo 1
        self.pasajero = pasajero                          #Atributo 2
        self.vuelo = vuelo                                #Atributo 3
        self.Estado = Estado                              #Atributo 4
    def __repr__(self):
        return f'{self.num_reservacion} ¬.Reserva de: {self.pasajero.nombre_apellido} en el vuelo: {self.vuelo.num_vuelo}' 
# -Esta clase servira para almacenar todos los objetos que se crean: avion, pasajero, vuelo, reserva.
class Almacenamineto_de_datos:
    def __init__(self):
        self.Almacenamiento_Avion = []        # Atributo 1    # Almacenar cada objeto Avion  
        self.Almacenamineto_Vuelo = []        # Atributo 2    # // Vuelos
        self.Almacenamiento_Pasajero = []     # Atributo 3    # // Pasajeros
        self.Almacenamiento_Reserva  = []     # Atributo 4    # // Rervaciones
        
aviones = []
vuelos = []
pasajeros = []
reservas = []

def crearAvion():
    modelo = input("Ingrese el modelo del avion: ")
    numAsientos = int(input("Ingrese el numero de asientos del avion: "))
    avion = Avion(modelo, numAsientos)
    aviones.append(avion)
    print(f"El avion modelo {modelo} ha sido correctamente registrado, con capacidad para {numAsientos} pasajeros")
        
def mostrarAviones():
    print("Aviones disponibles:")
    for i, avion in enumerate(aviones):
        print(f"{i + 1}.---- Modelo: {avion.modelo}, Asientos: {avion.capacidad}") 
            
def crearVuelo():
    origen = input("Ingrese la cuidad de origen del vuelo: ")
    destino = input("Ingres la cuidad de destino del vuelo: ")
    fecha_hora = input("Ingrese la fecha y hora del vuelo: ")
    mostrarAviones()
    respAvion = int(input("Ingrese el numero de avion para el vuelo: ")) - 1
    Avion_asigando = aviones[respAvion]
    num_vuelo = Avion_asigando
    vuelo = Vuelo(num_vuelo, origen, destino, fecha_hora, Avion_asigando)
    vuelos.append(vuelo)
    print("Se ha registrado el vuelo.")

def mostrarVuelos():
    for i, vuelo in enumerate(vuelos):
        print(f".- {vuelo.origen} hasta {vuelo.destino}, {vuelo.fecha_hora}, {vuelo.Avion_asigando}")
    
def crearReserva():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    
    pasajero = None
    for p in pasajeros:
        if p.nombre == nombre and p.apellido == apellido:
            pasajero = p
            break
    if not pasajero:
        pasajero = Pasajero(nombre, apellido)
        pasajeros.append(pasajero)

    mostrarVuelos()
    respVuelo = int(input("Ingrese el numero de vuelo para el viaje: "))

    if 0 <= respVuelo < len(vuelos):
        vueloSelec = vuelos[respVuelo]
        reserva = reserva(pasajero, vueloSelec)
        pasajero.reservas.append(reserva)
        print("La reserva ha sido creada.")
    else:
        ("El numero de vuelo no es valido.")

while True:
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
        elif subopcion == "b":
            mostrarAviones()

    elif opcion == 2:
        print("a) Registrar nuevo vuelo.")
        print("b) Ver vuelos disponibles.")
        print("c) Lista de vuelos.")
        print("d) Lista de pasajeros en un vuelo.")
        subopcion2 = input("Seleccione una opcion: ")
        if subopcion2 == "a":
            crearVuelo()
        elif subopcion2 == "c":
            mostrarVuelos()
        elif subopcion2 == "d":
            print(pasajeros)
    
    elif opcion == 3:
        print("a) Hacer una reserva.")
        print("b) Ver vuelos disponibles.")
        print("c) Lista de reservas de un pasajero.")
        print("d) Lista de pasajeros en un vuelo.")
        subopcion3 = input("Seleccione una opción: ")
        if subopcion3 == "a":
            crearReserva()
        elif subopcion3 == "b":
            mostrarVuelos()
        elif subopcion3 == "c":
            print("modulo aun no creado.")
        elif subopcion3 == "d":
            print("modulo aun no creado.")

    elif opcion == 4:
        print("Saliendo del sistema...")
        break
