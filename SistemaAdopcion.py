from abc import ABC, abstractclassmethod
from Perro import Perro
from Adoptante import Adoptante
import random

class SistemaAdopcion(object):
    def __init__(self):
        self.perros = []
    def cargarPerro(self, perro: Perro):
        self.perros.append(perro)
        print(f"Se cargo a {perro.nombre} a la lista de perros para adoptar")
        print(f"La lista actualizada: {[p.nombre for p in self.perros]}")
    
    def registrarse(self, adoptante: Adoptante):
        adoptante.registro = True
        print(f"Se registro para adopciones, el usuario: {adoptante.nombre}")
        
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
        

max = Perro('max','siberiano',5,'hiperactivo', 40, 'saludable', 'grande')
moro = Perro('moro', 'callejero', 7, 'esquizofrenico', 35, 'saludable', 'mediano')
shago = Perro('shago', 'caniche', 10, 'enfermito mental',5, 'bien', 'chico')
roberto = Adoptante('roberto', 30303030,'aaaa@aaa.com','raza')
sistema = SistemaAdopcion()
sistema.cargarPerro(max)
sistema.cargarPerro(moro)
sistema.cargarPerro(shago)
# sistema.registrarse(roberto)
sistema.sugerencia(roberto)
# print(sistema.perros)