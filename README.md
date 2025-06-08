# Sistema de Adopción de Perros

Este proyecto implementa un sistema básico de gestión de adopciones de perros, desarrollado en Python. Permite a los usuarios (adoptantes) registrarse, ver perros disponibles, recibir sugerencias y adoptar perros.

## Características

*   **Creación y Gestión de Adoptantes**:
    *   Crear nuevos perfiles de adoptantes con nombre, DNI, email y preferencias.
    *   Visualizar la información de un adoptante.
    *   Registrar adoptantes en el sistema para permitirles adoptar.
    *   Modificar los datos de un adoptante existente (requiere registro).
    *   Consultar el historial de adopciones de un adoptante.
*   **Gestión de Perros**:
    *   Cargar nuevos perros al sistema con atributos como nombre, raza, edad, temperamento, peso, salud, tamaño y estado.
    *   Listar perros disponibles para adopción.
    *   Listar perros que han sido adoptados.
    *   Eliminar perros de la lista de adopción.
*   **Proceso de Adopción**:
    *   Recibir sugerencias de perros basadas en las preferencias del adoptante (raza, edad, tamaño) o una sugerencia aleatoria.
    *   Realizar el proceso de adopción de un perro específico, cambiando su estado a "Adoptado" y registrándolo en el historial del adoptante.
    *   Validación para asegurar que el adoptante esté registrado y que el perro esté disponible.

## Estructura del Proyecto

El proyecto está compuesto por las siguientes clases principales:

### `Adoptante.py`
Define la clase `Adoptante`, que representa a la persona que busca adoptar un perro.
*   **Atributos**: `nombre`, `dni`, `email`, `preferencia` (raza, edad, tamaño, ninguna, no se aclaró), `historial_adopciones`, `registro` (estado de registro).
*   **Métodos Clave**:
    *   `agregar_adopcion(perro)`: Añade un perro al historial de adopciones del adoptante.
    *   `modificar_datos(...)`: Permite actualizar la información del adoptante.
    *   `mostrar_historial()`: Muestra los perros adoptados por el adoptante.

### `Perro.py`
Define la clase `Perro`, que representa a un canino disponible para adopción.
*   **Atributos**: `id` (generado automáticamente), `nombre`, `raza`, `edad`, `temperamento`, `peso`, `salud`, `tamanio`, `estado` (Disponible, Reservado, Adoptado).

### `SistemaAdopcion.py`
Esta es la clase central del sistema, implementando el patrón Singleton para asegurar una única instancia. Orquesta las interacciones entre `Adoptante` y `Perro`.
*   **Atributos**: `perros` (lista de perros disponibles), `perros_adoptados` (lista de perros que ya fueron adoptados).
*   **Métodos Clave**:
    *   `cargarPerro(perro)`: Añade un perro a la lista de disponibles.
    *   `eliminarRegistro(perro)`: Elimina un perro del sistema.
    *   `registrarse(adoptante)`: Registra un adoptante.
    *   `mostrarPerros()`: Muestra todos los perros disponibles.
    *   `mostrarPerrosAdoptados()`: Muestra todos los perros adoptados.
    *   `sugerencia(adoptante)`: Sugiere un perro basado en preferencias.
    *   `adoptar(adoptante, perro)`: Gestiona el proceso de adopción.
*   **Interfaz de Usuario**: Contiene un bucle principal con un menú interactivo en la consola para interactuar con el sistema.

## Cómo Ejecutar

Para ejecutar el sistema, simplemente corre el archivo `SistemaAdopcion.py` desde la terminal:

```bash
python SistemaAdopcion.py
```

Asegúrate de tener Python instalado en tu sistema. No se requieren dependencias adicionales aparte de las librerías estándar de Python. 