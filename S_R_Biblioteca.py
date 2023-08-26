class Libros():
    def __init__(self,titulo,autor,genero):
        self.titulo = titulo
        self.author = autor
        self.genero = genero
        self.lista_de_libros = {}
    def __str__(self):
        return f'{self.titulo},{self.author},{self.genero},' 
         
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
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre
        self.r_libro = []
        self.r_usuario = None
        self.r_prestamo = None

    def Registros_de_libros(self):
        pass
    def eliminar_libro_cat(self,libro):
        pass
    def agregar_libro_cat(self,libro):
        pass


ventana = True
while ventana == True:
    print('....:::Bienvenido al Sistema de gestión de la Biblioteca:::.....')
    print('Menu:\n')

    print('1. Añadir y eliminar libros al catálogo.') 
    print('2. Registrar usuarios.') 
    print('3. Prestar y devolver libros.' )
    print('4. Consultar libros disponibles.') 
    print('5. Ver el historial de préstamos de un usuario.')
    print('6. Salir del menu')

    respuesta = input('\nIngrese un número dentro de las opciones disponibles: ')

    if respuesta == '1':
        pass
    if respuesta == '2':
        pass
    if respuesta == '3':
        pass
    if respuesta == '4':
        pass
    if respuesta == '5':
        pass
    if respuesta == '6':
        print('mensaje de despedida')
        ventana = False
    else:
        print('Error. Has ingresado un número invalido')
        respuesta = input('Ingrese un número dentro de las opciones disponibles: ')

