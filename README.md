# Proyecto Adopción de Perros (POO)

Este proyecto es parte de la materia Programación Orientada a Objetos (POO) de la tecnicatura Análisis de Sistemas. El objetivo es simular un sistema básico de gestión de perros para adopción y adoptantes.

Actualmente, el proyecto cuenta con las siguientes clases:

## Clases Implementadas

### `Perro`
Representa un perro disponible para adopción. Sus atributos incluyen:
- `id` (int): Identificador único del perro.
- `nombre` (str): Nombre del perro.
- `raza` (str): Raza del perro.
- `edad` (int): Edad del perro.
- `temperamento` (str): Temperamento del perro.
- `peso` (float): Peso del perro en Kg.
- `salud` (str): Estado de salud del perro.
- `tamanio` (str): Tamaño del perro.
- `estado` (str): Estado actual del perro (`Disponible`, `Reservado`, `Adoptado`). Utiliza un setter para validar el estado.

### `Adoptante`
Representa a una persona interesada en adoptar un perro. Esta clase implementa el patrón Singleton para asegurar una única instancia.
Sus atributos incluyen:
- `nombre` (str): Nombre del adoptante.
- `dni` (int): DNI del adoptante.
- `email` (str): Correo electrónico del adoptante.
- `preferencia` (str): Preferencia de perro del adoptante (`raza`, `edad`, `tamanio`, `ninguna`, `no se aclaro`). Si no se especifica, se asigna automáticamente 'ninguna' o 'no se aclaro'.
- `historial_adopciones` (list): Lista de perros adoptados por el adoptante.
- `registro` (bool): Indica si el adoptante está registrado para adoptar.

Métodos principales:
- `registrarse()`: Marca al adoptante como registrado.
- `agregar_adopcion(perro)`: Agrega un perro al historial de adopciones si el adoptante está registrado.
- `modificar_datos(...)`: Permite modificar los datos del adoptante.
- `mostrar_historial()`: Muestra el historial de adopciones del adoptante si está registrado.

## Estado Actual del Proyecto

El proyecto se encuentra en desarrollo. Las clases `Perro` y `Adoptante` están definidas con sus atributos, getters, setters y algunos métodos básicos. Aún faltan por implementar funcionalidades completas del sistema de adopción, como la gestión de la lista de perros, el proceso de reserva y adopción, etc.

## Cómo Empezar

1.  Clonar el repositorio.
2.  (Opcional) Crear y activar un entorno virtual (`python -m venv myenv`, `source myenv/bin/activate`).
3.  Ejecutar los archivos `Perro.py` o `Adoptante.py` para probar las clases individualmente (contienen ejemplos de instanciación y uso al final de cada archivo).

```python
# Ejemplo en Perro.py
tobi = Perro(1, "Tobi", "Golden", 3, "jugueton", 25.3, "Perfecto", "mediano", "Reservado")
print(tobi)
```

```python
# Ejemplo en Adoptante.py
juan = Adoptante('Juan', 2020202020, "eee@eeee.com")
roberto = Adoptante('roberto', 30303030,'aaaa@aaa.com')
# juan.registrarse()
# juan.agregar_adopcion("tobi")
# juan.mostrar_historial()
# print(juan.nombre)
# juan.modificar_datos("nuevo", 1010101010, "2222@2222.com", None)
```

---

*Este README será actualizado a medida que el proyecto avance.*
