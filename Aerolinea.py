'''
menu pirncipal
    - 1. avion
        - a) Registrar nuevo avion                             # Crear avion
                + solicitar modelo, numero_asientos
        - b) Ver lista de aviones
                +mostrar lista de aviones                      # Llamar un metodo
                
    - 2. vuelo
        - a) Registrar nuevo vuelo                             # Crear vuelo
                + Solicitar origen, destino, fecha-hora, [Avion asignado]
        - b) Ver vuelos disponibles 
                + llamar metodo                                # Mostrar list_v_disponible
        - c) Lista de vuelos                      
                + mostrar lista_de_vuelos creados              # llamar metodo
        - d) Lista de pasajeros en un vuelo
        
    - 3. Reserva
        - a) Hacer una reserva                                 #crear reserva
                + solicitar nombre y apellido (creacion de pasajero)
                + solicitar el vuelo a reservar (buscar vuelo)
        - b) Cancelar reserva
                + solicitar nombre y apellido (buscar pasajero)
                + mostrar las reservas que tiene
                + solicitar el ID de la reserva a cancelar
        - c) Lista de reservas de un pasajero
                + mostrar lista                                # Llamar metodo
        - d) Lista de pasajeros en un vuelo
                + mostrar lista                                # Llamar metodo
    - 5. Salida del sistema
'''

class Avion:
    def __init__(self, modeloA, numAsientos):
        self.modeloA = modeloA
        self.numAsientos = numAsientos
        
class Vuelo:
    def __init__(self, origen, destino, fecha_hora, avionDesignado):
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avionDesignado = avionDesignado
        
class Pasajero:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
class Reserva:
    def __init__(self, pasajero, vuelo):
        self.pasajero = pasajero
        self.vuelo = vuelo
        
aviones = []
vuelos = []
pasajeros = []
reservas = []

def crearAvion():
    modeloA = input("Ingrese el modelo del avion: ")
    numAsientos = int(input("Ingrese el numero de asientos del avion: "))
    avion = Avion(modeloA, numAsientos)
    aviones.append(avion)
    print(f"El avion modelo {modeloA} ha sido correctamente registrado, con capacidad para {numAsientos} pasajeros")
        
def mostrarAviones():
    for i, avion in enumerate(aviones):
        print(f"{i + 1}.- Aviones disponibles: \n MODELO: {Avion.modeloA}, Asientos: {Avion.numAsientos}") 
            
def crearVuelo():
    origen = input("Ingrese la cuidad de origen del vuelo: ")
    destino = input("Ingres la cuidad de destino del vuelo: ")
    fecha_hora = input("Ingrese la fecha y hora del vuelo: ")
    mostrarAviones()
    respAvion = int(input("Ingrese el numero de avion para el vuelo: ")) + 1
    avionDesignado = aviones[respAvion]
    vuelo = Vuelo(origen, destino, fecha_hora, avionDesignado)
    vuelos.append(vuelo)
    print("Se ha registrado el vuelo.")

def mostrarVuelos():
    for i, vuelo in enumerate(vuelos):
        print(f".- {Vuelo.origen} hasta {Vuelo.destino}, {Avion.fecha_hora}, {Avion.avionDesignado}")
    
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
        reserva = Reserva(pasajero, vueloSelec)
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

    opcion = int(input("Seleccione una opción:"))

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








    
    
    
    
    
    

        
        
    
    
        
        
    
        