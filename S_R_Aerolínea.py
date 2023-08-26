class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo 
        self.num_asistentos = num_asientos
    def __str__(self):      
        return f'{self.modelo}{self.num_asistentos}'

class Vuelos:
    def __init__(self, num_vuelo, origen, destino, fecha, hora, avion_asignado,estado):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
        self.avion_asignado = avion_asignado
        self.lista_de_reserva = []
    def __repr__(self):
        return f'id_vuelo: {self.num_vuelo}/Origen:{self.origen}/Destino:{self.destino}/Fecha-Hora:{self.fecha} {self.hora}/Avion: {self.avion_asignado}/disponible:{self.estado}'
class Pasajeros:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.lista_de_vuelos_reservas = []
    def __str__(self):
        return f'{self.nombre}{self.num_pasaporte}'
    def Agregar_vuelo_a_lista_de_reservados(self,vuelo):
        self.lista_de_vuelos_reservas.append(vuelo)     
class Reservaciones:
    def __init__(self, num_reservacion, pasajero, vuelo, estado):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = estado
    def __str__(self):
        return f'{self.num_reservacion}.Reservado{self.pasajero} en el {self.vuelo} en estado: {self.estado}'
    def Estado(self):
        pass  
# avion (modelo, num_asiento)
avion = Avion('Las Estrellas',3)      # nombre y num_asientos

# pasajero (nombre,num_pasaporte,lista_vuelo_reservados)
pasajero_1 = Pasajeros('Marcelo',21697089-7)
pasajero_2 = Pasajeros('Juan',21697089-7)
pasajero_3 = Pasajeros('Pedro',21697089-7)
lista_pasarejos = [pasajero_1,pasajero_2,pasajero_3]
#vuelos (num_vuelo,origen,destino,fecha,hora,avion_asigando, lista_reserva)
vuelo_1 = Vuelos(1,'Labranza','Santiago','3 de julio','1.pm',avion,True)
vuelo_2 = Vuelos(1,'Labranza','Santiago','3 de julio','1.pm',avion,True)
vuelo_3 = Vuelos(1,'Labranza','Santiago','3 de julio','1.pm',avion,True)
lista_vuelos_disponibles = [vuelo_1,vuelo_2,vuelo_3]
#reservacion (num_reserva,pasajero, vuelo, estado R/C)
Reserva_1 = Reservaciones(1,pasajero_1,vuelo_1,'Reservado')
Reserva_2 = Reservaciones(1,pasajero_2,vuelo_2,'Reservado')
Reserva_3 = Reservaciones(1,pasajero_3,vuelo_3,'Reservado')
listas_de_vuelos_reservados = [Reserva_1,Reserva_2,Reserva_3]
#------------------------------------------------------------------------------------
# Sistema = 'open'
# num_vuelo = 1
# while Sistema != 'si':
#     origen = input('Escriba origen: ')
#     destino = input('Escriba destino')
#     vuelo = Vuelos(num_vuelo,'labranza','Temuco','4 de septiembre','1.pm',avion,True)
#     num_vuelo +=1
#     Sistema = input('Desea salir?(si)(no)')

    
