from Perro import Perro
from Adoptante import Adoptante
from datetime import date, datetime, timedelta, timezone
import random

class SistemaAdopcion(object):
    #Patron Singleton, verifica que el sistema se inicie solo 1 vez
    instance = None
    primer_sistema = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.primer_sistema = args #no tiene parametros, por eso no se le pasan [indices], solo args
            print(f"Iniciando Sistema de adopcion...")
        return cls.instance
    
    def __init__(self):
        if not hasattr(self, 'perros'):
            self.perros = []
            self.perros_adoptados = []
    def cargarPerro(self, perro: Perro):
        self.perros.append(perro)
        print(f"Se cargo a {perro.nombre} a la lista de perros para adoptar")
        print(f"La lista actualizada: {[p.nombre for p in self.perros]}")
    
    def eliminarRegistro(self, perro: Perro | int):
        if isinstance(perro, Perro):
            id = perro.id
        elif isinstance(perro, int):
            id = perro
        else: 
            raise ValueError("No se reconoce el parametro")
            
        i = 0
        while i < len(self.perros):
            p = self.perros[i].id
            if p == id:
                print(f'Se encontro coincidencia: {self.perros[i].nombre}')
                valor = input("Quieres eliminarlo de la lista de adopcion? ").lower()
                if valor == 'si':
                    del self.perros[i]
                    print('Perro eliminado de la lista correctamente, esta es la lista actual:')
                    print(self.perros)
            i += 1
        
    def registrarse(self, adoptante: Adoptante):
        adoptante.registro = True
        print(f"Se registro para adopciones, el usuario: {adoptante.nombre}")
        
    def mostrarPerros(self):
        i = 0
        print("Esta es la lista de perros:")
        if not self.perros:
            print("Aun no tenemos perros en la lista")
        else:
            while i < len(self.perros):
                p = self.perros[i]
                print(f"nombre: {p.nombre}, raza: {p.raza}, edad: {p.edad}, temperamento: {p.temperamento}, peso: {p.peso}, salud: {p.salud}, tamanio: {p.tamanio}, estado: {p.estado}")
                i += 1
    
    def mostrarPerrosAdoptados(self):
        i = 0
        print("Lista de perros adoptados: ")
        if not self.perros_adoptados:
            print("Todavia no hay ningun servicio de adopcion realizado")
        else:
            while i < len(self.perros_adoptados):
                p = self.perros_adoptados[i]
                print(p)
                i += 1
        
    def sugerencia(self, adoptante: Adoptante):
        if not self.perros:
            #si la lista de perros esta vacia.
            raise ValueError("No existen registros de perros en el sistema")
        elif adoptante.preferencia == 'ninguna' or adoptante.preferencia == 'no se aclaro':
            #si el adoptante no tiene preferencias pero aun asi quiere una recomendacion, dara un random
            recomendacion = random.choice(self.perros)
            print(f"Como no tiene ninguna preferencia, puedo recomendar a este perrito: {recomendacion.nombre}")
        elif adoptante.preferencia == 'edad':
            recomendacion = min(self.perros, key=lambda p : p.edad)
            print(f"Segun tu preferenica este es el perrito mas joven para adoptar: {recomendacion.nombre}, con {recomendacion.edad} anios de edad")
        elif adoptante.preferencia == 'tamanio':
            ordenar_tamanio = {'chico': 1, 'mediano': 2, 'grande': 3}
            recomendacion = min(self.perros, key=lambda p: ordenar_tamanio.get(p.tamanio))
            print(f"Segun tu preferencia este es el perrito mas chico en tamanio: {recomendacion.nombre}, con su tamanio: {recomendacion.tamanio}")
        elif adoptante.preferencia == 'raza':
            perros_de_raza=[]
            i = 0
            while i < len(self.perros):
                perro = self.perros[i]
                if perro.raza != 'callejero':
                    perros_de_raza.append(perro)
                i += 1
            if perros_de_raza:
                print(f"Tenemos estos perros de raza para adopcion:")
                for p in perros_de_raza:
                    print(f"{p.nombre}, raza: {p.raza}")
        else:
            raise ValueError('Error de preferencia')
        
    def adoptar(self, adoptante: Adoptante, perro: Perro | int | str):
        i = 0
        if isinstance(perro, Perro):
            id = perro.id
        elif isinstance(perro, int):
            id = perro
        elif isinstance(perro, str):
            id = perro
        else:
            raise ValueError(f'Error, parametro no identificado')
        
        if adoptante.registro == True:
            while i < len(self.perros):
                p = self.perros[i]
                if p.id == id or p.nombre == id:
                    if p.estado == 'Disponible':
                        pregunta = input(f'Estas seguro que quieres adoptar a: {self.perros[i].nombre}? ').lower()
                        if pregunta == 'si':
                            print(f'Perfecto! Te felicito {adoptante.nombre} por la adopcion de: {self.perros[i].nombre}')
                            self.perros[i].estado = "Adoptado"
                            self.perros_adoptados.append({"Perro" : self.perros[i].nombre, "Estado": self.perros[i].estado ,"Adoptante:" : adoptante.nombre, "Fecha": date.today()})
                            adoptante.agregar_adopcion({date.today() : self.perros[i].nombre})
                            del self.perros[i]
                        else:
                            print(f"Seguiremos buscando un perro que se adapte a lo que busca.")
                        return
                    else:
                        print(F"Lo siento el estado de ese perro es: {self.perros[i].estado}, por ende no puede adoptarlo")
                        return
                i += 1
            raise ValueError(f'Perro inexistente en la lista.')
        else:
            print("No estas registrado para adoptar perros.")
            registrarlo = input("Quieres registrarte para adoptar? ").lower()
            if registrarlo == 'si':
                self.registrarse(adoptante)
                return self.adoptar(adoptante, perro)
            else: 
                raise ValueError("Atencion! para seguir con la adopcion es obligacion estar registrado en el sistema.")
    

max = Perro('max','siberiano',5,'hiperactivo', 40, 'saludable', 'grande')
moro = Perro('moro', 'callejero', 7, 'esquizofrenico', 35, 'saludable', 'mediano')
shago = Perro('shago', 'caniche', 10, 'enfermito mental',5, 'bien', 'chico')
sistema = SistemaAdopcion()
sistema.cargarPerro(max)
sistema.cargarPerro(moro)
sistema.cargarPerro(shago)

adoptante = None
while True:
    print("|---- Menu de opciones ----|")
    print("1. Crear Adoptante")
    print("2. Ver su informacion")
    print("3. Registrar al Adoptante")
    print("4. Modificar su informacion (Debe estar registrado)")
    print("5. Cargar perrito para adopcion")
    print("6. Lista de perros disponibles")
    print("7. Ver historial de adopciones del Adoptante")
    print("8. Sugerir perro al adoptante(Debe tener su informacion cargada)")
    print("9. Adoptar perro (Debe estar su informacion en el sistema y registrado en el mismo para adopcion)")
    print("10. Mostrar perros adoptados")
    print("11. Salir")
    
    elegir = input("Seleccione una opcion: ").lower()
    
    if elegir == '1':
        nombre = input("Ingrese su nombre: ").lower()
        dni = input("Ingrese su DNI: ")
        email = input("Ingrese su correo electronico: ").lower()
        preferencia = input("Si tiene alguna preferencia (raza, edad o tamanio) ingreselo sino, dejar vacio: ").lower()
        adoptante = Adoptante(nombre,dni,email,preferencia)
        print(f"Se cargo sus datos exitosamente al sistema. Para adoptar debe registrase con la opcion 3!")
    elif elegir == '2':
        if adoptante is not None:
            print(adoptante)
        else:
            print("Ingrese su informacion al Sistema con la opcion 1.")
    elif elegir == '3':
        if adoptante is not None:
            if adoptante.registro:
                print(f"{adoptante.nombre}, usted ya esta registrado para adoptar")
            else:
                sistema.registrarse(adoptante)
                print("Se registro exitosamente, ahora puede adoptar")
        else:
            print("ATENCION!!! Primero debe agregar sus datos. Por favor utiliza la opcion 1.")
    elif elegir == '4':
        if adoptante is not None:
            print("Modifique la informacion a cambiar, la que no, deje en vacio el campo.")
            new_nombre = input("Modifique su nombre: ").lower()
            new_dni = input("Modifique su DNI: ")
            new_email = input("Modifique su correo electronico: ").lower()
            new_preferencia = input("Modifique o agregue alguna preferencia (raza, edad o tamanio) ingreselo sino, dejar vacio: ").lower()
            adoptante.modificar_datos(new_nombre,new_dni,new_email,new_preferencia)
        else: 
            print("Para modificar la informacion, primero debe existir...")
    elif elegir == '5':
        nombre_perro = input("Ingrese el nombre del perrito: ").lower()
        raza = input("Ingrese la raza, sino tiene declarelo mestizo o callejero, etc: ").lower()
        edad = input("Ingrese la edad: ").lower()
        temperamento = input("Califique el temperamento: ").lower()
        peso = input("Ingrese el peso aproximado: ").lower()
        salud = input("Identifique la salud del canino: ").lower()
        tamanio = input("Ingrese el tamanio(chico, mediano o grande): ").lower()
        perro = Perro(nombre_perro,raza,edad,temperamento,peso,salud,tamanio)
        sistema.cargarPerro(perro)
        print(f"Se cargo al perro {perro.nombre} exitosamente al sistema y lista de perros en adopcion.")
    elif elegir == '6':
        sistema.mostrarPerros()  
    elif elegir == '7':
        if adoptante is not None:
            if adoptante.registro:
                adoptante.mostrar_historial()
            else:
                print("Para ver el historial del adoptante, debe estar registrado en el sistema.")
        else:
            print("Primero ingrese sus datos y luego registrese en el sistema para utilizar esta opcion")
        pass
    elif elegir == '8':
        if adoptante is not None:
            sistema.sugerencia(adoptante)
        else:
            print("Debe tener su informacion en el sistema para esta opcion.")
    elif elegir == '9':
        if adoptante is not None:
            if adoptante.registro:
                perro_adoptar = input("Especifique que perro quiere adoptar, puede hacerlo por ID del perro o su nombre: ")
                sistema.adoptar(adoptante, perro_adoptar)
            else: 
                print("Debe estar registrado para adoptar")
        else:
            print("Debe estar su informacion en el sistema y estar registrado")
    elif elegir == '10':
        sistema.mostrarPerrosAdoptados()
    elif elegir == '11':
        print("Gracias por usar nuestro sistema de adopciones caninos! Que tenga buen dia!")
        break
    else:
        print("La opcion seleccionada es invalida. Por favor seleccione una de las listadas.")