class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo 
        self.num_asistentos = num_asientos
    def __str__(self):
        return

class Vuelos:
    def __init__(self, num_vuelo, origen, destino, fecha, hora, avion_asignado, lista_de_reservaciones):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.avion_asignado = avion_asignado
        self.lista_de_reserva = lista_de_reservaciones

    def __str__(self):
        return 
    
class Pasajeros:
    def __init__(self, nombre, num_pasaporte,lista_de_vuelos_reservados):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.lista_de_vuelos_reservas = lista_de_vuelos_reservados
    def __str__(self):
        return
    
class Reservaciones:
    def __init__(self, num_reservacion, pasajero, vuelo, estado):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = estado
    def __str__(self):
        return
    def Estado(self):
        pass
