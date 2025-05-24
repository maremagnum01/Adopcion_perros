class Perro(object):
    # instance = None
    # primer_clase_perro = None
    
    # def __new__(cls, *args, **kwargs):
    #     if cls.instance is None:
    #         cls.instance = super().__new__(cls)
    #         cls.primer_clase_perro = args[0]
    #         print(f"Se inicializo por primera vez la clase 'Perro', bajo el nombre de: {cls.primer_clase_perro}")
    #     return cls.instance
    
    ##el frozenset funciona para congelar la constante y que no cambie por accidente
    ## Las constantes se definen en mayusculas 
    LISTA_ESTADOS = frozenset({'Disponible', 'Reservado', 'Adoptado'})
    
    id_actual = 1
    def __init__(self, nombre: str, raza: str, edad: int, temperamento: str, peso: float, salud: str, tamanio: str, estado='Disponible'):
        self.__id = Perro.id_actual
        Perro.id_actual += 1
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        self.__temperamento = temperamento
        self.__peso = peso
        self.__salud = salud
        self.__tamanio = tamanio
        self.__estado = None
        self.estado = estado #este 'estado' es el setter
        
    ##GETTERS
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property 
    def raza(self):
        return self.__raza
    @property
    def edad(self):
        return self.__edad
    @property
    def temperamento(self):
        return self.__temperamento
    @property 
    def peso(self):
        return self.__peso
    @property
    def salud(self):
        return self.__salud
    @property 
    def tamanio(self):
        return self.__tamanio
    @property
    def estado(self):
        return self.__estado
    
    ##SETTERS
    @id.setter
    def id(self, new_id):
        self.__id = new_id
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    @raza.setter
    def raza(self, new_raza):
        self.__raza = new_raza
    @edad.setter
    def edad(self, new_edad):
        self.__edad = new_edad
    @temperamento.setter
    def temperamento(self, new_temperamento):
        self.__temperamento = new_temperamento
    @peso.setter
    def peso(self, new_peso):
        self.__peso = new_peso
    @salud.setter
    def salud(self, new_salud):
        self.__salud = new_salud
    @tamanio.setter
    def tamanio(self, new_tamanio):
        self.__tamanio = new_tamanio
    ## Con el setter de estado, realizamos el cambiar estado.
    @estado.setter
    def estado(self, new_estado):
        if self.estado is not None:
            print(f"[setter de estado] el estado anterior era: {self.__estado}")
        if new_estado in self.LISTA_ESTADOS:
            self.__estado = new_estado
        else:
            raise ValueError(f"Error al cambiar estado, solo pueden ser un estado de esta lista: {self.LISTA_ESTADOS}")
        
    ## al realizar print(objeto ya instanciado) muestra info del objeto en cuestion 
    def __repr__(self):
        return f"Perro(ID: {self.id}, Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}, Temperamento: {self.temperamento}, Peso en Kg: {self.peso}, Salud: {self.salud}, Tamanio: {self.tamanio}, Estado: {self.estado})"

# tobi = Perro("Tobi", "Golden", 3, "jugueton", 25.3, "Perfecto", "mediano", "Reservado")
# print(tobi)
