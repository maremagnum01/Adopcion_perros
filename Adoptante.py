import random

class Adoptante(object):
    #Guardar instancia + primer clase creada
    instance = None
    primer_clase_adoptante = None
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.primer_clase_adoptante = args[0]
            print(f"Se inicializo por primera vez la clase 'Adoptante', bajo el nombre de: {cls.primer_clase_adoptante}")
        # else:
        #     print(f"Ya existe una clase que inicializa por primera vez la clase 'Adoptante', es la clase {cls.primer_clase_adoptante} ")
        return cls.instance
    
    ##Constante de preferencias 
    LISTA_PREFERENCIAS = frozenset({"raza","edad","tamanio","ninguna","no se aclaro"})
    
    def __init__(self, nombre: str, dni: int, email: str, preferencia= None):
        self.__nombre = nombre
        self.__dni = dni
        self.__email = email
        self.__preferencia = None
        self.preferencia = preferencia
        self.__historial_adopciones = []
        self.__registrado = False
     
    ## GETTERS   
    @property
    def nombre(self):
        return self.__nombre
    @property
    def dni(self):
        return self.__dni
    @property
    def email(self):
        return self.__email
    @property
    def preferencia(self):
        return self.__preferencia
    @property
    def historial_adopciones(self):
        return self.__historial_adopciones
    @property
    def registro(self):
        return self.__registrado
    
    ## SETTERS
    @nombre.setter
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
    @dni.setter
    def dni(self, new_dni):
        self.__dni = new_dni
    @email.setter
    def email(self, new_email):
        self.__email = new_email
    @preferencia.setter
    def preferencia(self, new_preferencia):
        if new_preferencia is None:
            ## En caso de no aclarar o no tener ninguna preferencia, automaticamente se autoselecionara uno de los 2 
            opciones = ["ninguna", "no se aclaro"]
            self.__preferencia = random.choice(opciones)
            return
        if self.preferencia is not None:
            print(f"[setter de preferencia] la preferencia anterior era: {self.__preferencia}")
        if new_preferencia in self.LISTA_PREFERENCIAS:
            self.__preferencia = new_preferencia
        else:
            raise ValueError(f"Las preferencias debe ser una de la lista: {' '.join(self.LISTA_PREFERENCIAS)}")
    @registro.setter
    def registro(self, new_registro):
        self.__registrado = new_registro    
    
    ## Metodos
    def registrarse(self):
        print(f"Se registro para adopciones, el usuario: {self.nombre}")
        self.registro = True
    def agregar_adopcion(self, perro):
        if self.registro == True:
            self.__historial_adopciones.append(perro)
            print(f"Se adopto a {perro}")
        else: 
            raise ValueError(f"Se debe registrar para iniciar una adopcion")
        
    def modificar_datos(self, nombre: str = None, dni: int = None, email: str = None, preferencia = None):
        if nombre:
            self.nombre = nombre
        if dni:
            self.dni = dni
        if email:
            self.email = email
        if preferencia:
            self.preferencia = preferencia
        print(f"Datos modificados, ahora tus nuevos datos son: {Adoptante.__repr__(self)}")
        
    def mostrar_historial(self):
        if self.registro == True:
            if not self.__historial_adopciones:
                print("No se registraron adopciones")
            else:
                print("Historial: ")
                i = 0
                while i < len(self.__historial_adopciones):
                    print(f" {i + 1} - {self.__historial_adopciones[i]}")
                    i+=1
        else:
            raise ValueError(f"Para visualizar el historial, debe estar registrado")
                
    ## mostrar info
    def __repr__(self):
        return f"Adoptante(Nombre: {self.nombre}, DNI: {self.dni}, Email: {self.email}, Preferencia: {self.preferencia}, Historial: {self.historial_adopciones})"
    
    
juan = Adoptante('Juan', 2020202020, "eee@eeee.com")
roberto = Adoptante('roberto', 30303030,'aaaa@aaa.com')
# juan.registrarse()
# juan.agregar_adopcion("tobi")
# juan.mostrar_historial()
# print(juan.nombre)
# juan.modificar_datos("nuevo", 1010101010, "2222@2222.com", None)
