from Perro import Perro
from Adoptante import Adoptante
import random

class SistemaAdopcion(object):
    def __init__(self):
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
        while i < len(self.perros):
            p = self.perros[i]
            print(f"nombre: {p.nombre}, raza: {p.raza}, edad: {p.edad}, temperamento: {p.temperamento}, peso: {p.peso}, salud: {p.salud}, tamanio: {p.tamanio}, estado: {p.estado}")
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
                        # mandar perro adoptado a un array de perros adoptados + el nombre del adoptante
                        # crear verificacion del parametro
        i = 0
        if isinstance(perro, Perro):
            id = perro.id
        elif isinstance(perro, int):
            id = perro
        elif isinstance(perro, str):
            id = perro
        else:
            raise ValueError(f'Error, parametro no identificado')
        
        while i < len(self.perros):
            p = self.perros[i]
            if p.id == id or p.nombre == id:
                if p.estado == 'Disponible':
                    pregunta = input(f'Estas seguro que quieres adoptar a: {self.perros[i].nombre}? ').lower()
                    if pregunta == 'si':
                        print(f'Perfecto! Te felicito {adoptante.nombre} por la adopcion de: {self.perros[i].nombre}')
                        self.perros_adoptados.append(self.perros[i])
                        del self.perros[i]
                    else:
                        print(f"Seguiremos buscando un perro que se adapte a lo que busca.")
                    return 
                else:
                    print(F"Lo siento el estado de ese perro es: {self.perros[i].estado}, por ende no puede adoptarlo")
                    return
            i += 1
        raise ValueError(f'Perro inexistente en la lista.')

max = Perro('max','siberiano',5,'hiperactivo', 40, 'saludable', 'grande')
moro = Perro('moro', 'callejero', 7, 'esquizofrenico', 35, 'saludable', 'mediano')
shago = Perro('shago', 'caniche', 10, 'enfermito mental',5, 'bien', 'chico')
roberto = Adoptante('roberto', 30303030,'aaaa@aaa.com','raza')
sistema = SistemaAdopcion()
sistema.cargarPerro(max)
sistema.cargarPerro(moro)
sistema.cargarPerro(shago)
# sistema.registrarse(roberto)
# sistema.sugerencia(roberto)
# print(sistema.perros)
# sistema.mostrarPerros()
# sistema.eliminarRegistro(2)
sistema.adoptar(roberto, 'max')