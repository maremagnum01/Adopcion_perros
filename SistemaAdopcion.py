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
        print(f"La lista: {[p.nombre for p in self.perros]}")
    
    def registrarse(self, adoptante: Adoptante):
        adoptante.registro = True
        print(f"Se registro para adopciones, el usuario: {adoptante.nombre}")
        
    def sugerencia(self, adoptante: Adoptante):
        if not self.perros:
            raise ValueError("No existen registros de perros en el sistema")
        
        if adoptante.preferencia == 'ninguna' or adoptante.preferencia == 'no se aclaro':
            recomendacion = random.choice(self.perros)
            print(f"Como no tiene ninguna preferencia, puedo recomendar a este perrito: {recomendacion}")
        # if adoptante.preferencia == 'edad':

max = Perro('max','siberiano',5,'hiperactivo', 40, 'saludable', 'grande')
moro = Perro('moro', 'callejero', 7, 'esquizofrenico', 35, 'saludable', 'mediano')
shago = Perro('shago', 'caniche', 10, 'enfermito mental',5, 'bien', 'chico')
roberto = Adoptante('roberto', 30303030,'aaaa@aaa.com')
sistema = SistemaAdopcion()
sistema.cargarPerro(max)
sistema.cargarPerro(moro)
# sistema.registrarse(roberto)
# sistema.sugerencia(roberto)
print(sistema.perros)