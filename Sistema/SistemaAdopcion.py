from .Perro import Perro
from .Adoptante import Adoptante
from datetime import datetime, date
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
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
        
        self.perros.append(perro)
        print(f"Se cargo a {perro.nombre} a la lista de perros para adoptar")
        print(f"La lista actualizada: {[p.nombre for p in self.perros]}")
        with open('logs.log', 'a+') as log:
            log.write(f'[{fecha_hora}]Se ingreso en el sistema al perro: {perro.nombre} \n')
    
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
                    print('Perro eliminado de la lista correctamente, esta es la lista actual:')
                    print(self.perros)
                    with open('logs.log', 'a+') as log:
                        ahora = datetime.now()
                        fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                        log.write(f'[{fecha_hora}]Se elimino del sistema al perro: {self.perros[i].nombre} \n')                    
                    del self.perros[i]
            i += 1
        
    def registrarse(self, adoptante: Adoptante):
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
        adoptante.registro = True
        print(f"Se registro para adopciones, el usuario: {adoptante.nombre}")
        with open('logs.log', 'a+') as log:
            log.write(f'[{fecha_hora}]El usuario {adoptante.nombre} se registro para poder adoptar. \n')
        
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
        ahora = datetime.now()
        fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
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
        
        with open('logs.log', 'a+') as log:
            log.write(f'[{fecha_hora}]El usuario {adoptante.nombre} pidio una sugerencia. \n')
        
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
                            ahora = datetime.now()
                            fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                            
                            print(f'Perfecto! Te felicito {adoptante.nombre} por la adopcion de: {self.perros[i].nombre}')
                            self.perros[i].estado = "Adoptado"
                            self.perros_adoptados.append({"Perro" : self.perros[i].nombre, "Estado": self.perros[i].estado ,"Adoptante:" : adoptante.nombre, "Fecha": fecha_hora})
                            adoptante.agregar_adopcion({fecha_hora : self.perros[i].nombre})
                            with open('logs.log', 'a+') as log:
                                log.write(f'[{fecha_hora}]El usuario {adoptante.nombre} adopto a: {self.perros[i].nombre} \n')
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