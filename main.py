from Sistema.SistemaAdopcion import SistemaAdopcion
from Sistema.Adoptante import Adoptante
from Sistema.Perro import Perro
from datetime import date, datetime

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
        with open('logs.log', 'a+') as log:
            ahora = datetime.now()
            fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
            log.write(f'[{fecha_hora}]Se creo el usuario {adoptante.nombre} \n')   
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
            with open('logs.log', 'a+') as log:
                ahora = datetime.now()
                fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                log.write(f'[{fecha_hora}]Se detecto un intento de registro sin agregar datos. \n')   
    elif elegir == '4':
        if adoptante is not None:
            print("Modifique la informacion a cambiar, la que no, deje en vacio el campo.")
            new_nombre = input("Modifique su nombre: ").lower()
            new_dni = input("Modifique su DNI: ")
            new_email = input("Modifique su correo electronico: ").lower()
            new_preferencia = input("Modifique o agregue alguna preferencia (raza, edad o tamanio) ingreselo sino, dejar vacio: ").lower()
            adoptante.modificar_datos(new_nombre,new_dni,new_email,new_preferencia)
            with open('logs.log', 'a+') as log:
                ahora = datetime.now()
                fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                log.write(f'[{fecha_hora}]Se modificaron los datos de {adoptante.nombre} \n')   
        else: 
            print("Para modificar la informacion, primero debe existir...")
            with open('logs.log', 'a+') as log:
                ahora = datetime.now()
                fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                log.write(f'[{fecha_hora}]Se detecto intento de cambiar datos sin tener un usuario creado. \n')   
            
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
        with open('logs.log', 'a+') as log:
            ahora = datetime.now()
            fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
            log.write(f'[{fecha_hora}]Se pidio lista de perros. \n')   
    elif elegir == '7':
        if adoptante is not None:
            if adoptante.registro:
                adoptante.mostrar_historial()
                with open('logs.log', 'a+') as log:
                    ahora = datetime.now()
                    fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                    log.write(f'[{fecha_hora}]El {adoptante.nombre} pidio ver historial \n')   
            else:
                print("Para ver el historial del adoptante, debe estar registrado en el sistema.")
                with open('logs.log', 'a+') as log:
                    ahora = datetime.now()
                    fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                    log.write(f'[{fecha_hora}]Intento de ver historial de adopciones sin un registro previo \n')   
        else:
            print("Primero ingrese sus datos y luego registrese en el sistema para utilizar esta opcion")
            with open('logs.log', 'a+') as log:
                ahora = datetime.now()
                fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
                log.write(f'[{fecha_hora}]Se intento ver historial del adoptante sin datos. \n')   
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
        with open('logs.log', 'a+') as log:
            ahora = datetime.now()
            fecha_hora = ahora.strftime("%d-%m-%Y %H:%M:%S")
            log.write(f'[{fecha_hora}]Finalizacion del sistema. \n')
        break
    else:
        print("La opcion seleccionada es invalida. Por favor seleccione una de las listadas.")