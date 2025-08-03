# Sistema de Adopción de Perros

Este proyecto implementa un sistema completo de gestión de adopciones de perros, desarrollado en Python. Permite a los usuarios (adoptantes) registrarse, ver perros disponibles, recibir sugerencias personalizadas y adoptar perros. El sistema incluye logging de actividades, tests unitarios y una interfaz de consola interactiva.

## 🏗️ Estructura del Proyecto

```
tp_adopcion_pyPuro/
├── main.py                 # Punto de entrada principal con interfaz de consola
├── Sistema/                # Módulo principal del sistema
│   ├── __init__.py
│   ├── Adoptante.py        # Clase para gestionar adoptantes
│   ├── Perro.py           # Clase para gestionar perros
│   └── SistemaAdopcion.py # Clase principal del sistema (Singleton)
├── Tests/                  # Tests unitarios
│   ├── __init__.py
│   ├── test_adoptante.py
│   ├── test_perro.py
│   └── test_sistema.py
├── requirements.txt        # Dependencias del proyecto
├── logs.log               # Archivo de logs del sistema
├── readme.md              # Este archivo
└── venv/                  # Entorno virtual (no incluido en git)
```

## ✨ Características Principales

### 🔐 Gestión de Adoptantes
- **Creación de perfiles**: Nombre, DNI, email y preferencias (raza, edad, tamaño)
- **Sistema de registro**: Los adoptantes deben registrarse para poder adoptar
- **Modificación de datos**: Actualización de información personal (requiere registro previo)
- **Historial de adopciones**: Seguimiento de todas las adopciones realizadas
- **Validación de preferencias**: Sistema automático de asignación de preferencias

### 🐕 Gestión de Perros
- **Registro completo**: ID automático, nombre, raza, edad, temperamento, peso, salud, tamaño
- **Estados de adopción**: Disponible, Reservado, Adoptado
- **Carga y eliminación**: Gestión completa del inventario de perros
- **Información detallada**: Todos los datos relevantes para la adopción

### 🎯 Sistema de Sugerencias Inteligentes
- **Por edad**: Recomienda el perro más joven disponible
- **Por tamaño**: Sugiere el perro más pequeño (chico → mediano → grande)
- **Por raza**: Lista todos los perros de raza específica (excluyendo callejeros)
- **Aleatorio**: Recomendación automática cuando no hay preferencias específicas

### 📊 Sistema de Logging
- **Registro automático**: Todas las acciones importantes se registran con timestamp
- **Actividades registradas**:
  - Creación de usuarios
  - Registro de adoptantes
  - Carga y eliminación de perros
  - Modificación de datos
  - Consultas de historial
  - Finalización del sistema

## 🧪 Tests Unitarios

El proyecto incluye una suite de tests unitarios para validar la funcionalidad:

```bash
# Ejecutar todos los tests
pytest Tests/

# Ejecutar tests específicos
pytest Tests/test_sistema.py
pytest Tests/test_adoptante.py
pytest Tests/test_perro.py
```

## 🚀 Cómo Ejecutar

### Prerrequisitos
- Python 3.6 o superior
- Dependencias listadas en `requirements.txt`

### Instalación
```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd tp_adopcion_pyPuro

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecución
```bash
# Ejecutar el sistema principal
python main.py
```

## 📋 Menú de Opciones

El sistema presenta un menú interactivo con las siguientes opciones:

1. **Crear Adoptante** - Registrar nueva información de adoptante
2. **Ver información** - Mostrar datos del adoptante actual
3. **Registrar al Adoptante** - Habilitar adopciones para el usuario
4. **Modificar información** - Actualizar datos personales (requiere registro)
5. **Cargar perrito para adopción** - Añadir nuevo perro al sistema
6. **Lista de perros disponibles** - Ver todos los perros en adopción
7. **Ver historial de adopciones** - Consultar adopciones previas
8. **Sugerir perro** - Recibir recomendación personalizada
9. **Adoptar perro** - Realizar proceso de adopción
10. **Mostrar perros adoptados** - Ver historial de adopciones del sistema
11. **Salir** - Finalizar el programa

## 🔧 Arquitectura Técnica

### Patrón Singleton
La clase `SistemaAdopcion` implementa el patrón Singleton para asegurar una única instancia del sistema en toda la aplicación.

### Encapsulación
Todas las clases utilizan encapsulación con atributos privados (`__atributo`) y propiedades (`@property`) para controlar el acceso a los datos.

### Validación de Datos
- Validación de preferencias en `Adoptante`
- Validación de estados en `Perro`
- Verificación de registro antes de operaciones críticas

### Manejo de Errores
- Excepciones personalizadas para casos de error
- Validaciones en tiempo de ejecución
- Mensajes informativos para el usuario

## 📝 Logs del Sistema

El sistema genera logs automáticamente en `logs.log` con el formato:
```
[DD-MM-YYYY HH:MM:SS] Descripción de la acción
```

Ejemplos de logs:
- `[02-08-2025 15:00:32]Se ingreso en el sistema al perro: max`
- `[02-08-2025 22:44:39]Se pidio lista de perros`
- `[02-08-2025 22:45:19]Finalizacion del sistema`

## 🎯 Casos de Uso

### Flujo Típico de Adopción
1. Crear perfil de adoptante (opción 1)
2. Registrar al adoptante (opción 3)
3. Ver perros disponibles (opción 6)
4. Recibir sugerencias (opción 8)
5. Realizar adopción (opción 9)

### Gestión Administrativa
- Cargar nuevos perros al sistema
- Eliminar perros de la lista
- Consultar estadísticas de adopciones
- Revisar logs de actividad

## 🔍 Dependencias

- **pytest**: Framework de testing
- **iniconfig**: Configuración de archivos INI
- **packaging**: Utilidades de empaquetado
- **pluggy**: Sistema de plugins
- **Pygments**: Resaltado de sintaxis

## 📄 Licencia

Este proyecto es parte de un trabajo práctico de Programación Orientada a Objetos.

## 🤝 Contribución

Para contribuir al proyecto:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Realiza los cambios
4. Ejecuta los tests
5. Envía un pull request

## 📞 Soporte

Para reportar bugs o solicitar nuevas características, por favor crea un issue en el repositorio del proyecto. 