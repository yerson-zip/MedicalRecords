# MedicalRecords

API REST para la gestión de historias clínicas, desarrollada con **FastAPI**, **SQLAlchemy** y **Pydantic**.

El proyecto permite crear, consultar y actualizar historias clínicas asociadas a pacientes y médicos.

## Tecnologías utilizadas

- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- python-dotenv
- Base de datos configurada mediante una variable de entorno

## Estructura del proyecto

```text
MedicalRecords/
└── app/
    ├── __init__.py
    ├── main.py
    ├── database.py
    │
    ├── config/
    │   ├── __init__.py
    │   └── config.py
    │
    ├── model/
    │   ├── __init__.py
    │   └── historial.py
    │
    ├── schemas/
    │   ├── __init__.py
    │   └── historia_dto.py
    │
    └── servicio/
        ├── __init__.py
        └── historial.py
```

### Descripción de las carpetas

- **app/main.py:** punto de entrada de la API y definición de los endpoints.
- **app/database.py:** configuración de SQLAlchemy y manejo de sesiones de base de datos.
- **app/config/:** lectura de variables de entorno.
- **app/model/:** modelos de las tablas de la base de datos.
- **app/schemas/:** esquemas Pydantic utilizados para validar los datos.
- **app/servicio/:** lógica de negocio para crear, consultar y actualizar historias clínicas.

## Modelo de datos

La tabla `historial` contiene los siguientes campos:

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | Integer | Identificador único de la historia |
| `paciente_id` | Integer | Identificador del paciente |
| `medico_id` | Integer | Identificador del médico |
| `fecha` | DateTime | Fecha de la historia |
| `diagnostico` | String | Diagnóstico registrado |
| `sintomas` | String | Síntomas del paciente |
| `tratamiento` | String | Tratamiento indicado |
| `observacion` | String | Observaciones adicionales |
| `activo` | Boolean | Estado de la historia |

## Instalación

Clona el repositorio:

```bash
git clone https://github.com/yerson-zip/MedicalRecords.git
cd MedicalRecords
```

Crea un entorno virtual:

```bash
python -m venv venv
```

Activa el entorno virtual en Windows:

```bash
venv\Scripts\activate
```

Instala las dependencias:

```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv
```

## Configuración de la base de datos

El proyecto obtiene la URL de conexión desde la variable de entorno `DATABASE`.

Crea un archivo `.env` en la raíz del proyecto:

```env
DATABASE=TU_URL_DE_CONEXION
```

La URL debe corresponder al motor de base de datos que estés utilizando y ser compatible con SQLAlchemy.

> No subas el archivo `.env` a GitHub si contiene credenciales reales.

Se recomienda agregar `.env` al archivo `.gitignore`.

## Ejecución

Desde la carpeta raíz del proyecto ejecuta:

```bash
uvicorn app.main:app --reload
```

La API estará disponible en:

```text
http://127.0.0.1:8000
```

### Documentación interactiva

FastAPI genera automáticamente la documentación Swagger:

```text
http://127.0.0.1:8000/docs
```

También está disponible la documentación alternativa:

```text
http://127.0.0.1:8000/redoc
```

## Endpoints disponibles

### Crear una historia clínica

**POST** `/historias`

Ejemplo de datos:

```json
{
  "paciente_id": 1,
  "medico_id": 2,
  "fecha": "2026-08-19T18:00:00",
  "diagnostico": "Diagnóstico de ejemplo",
  "sintomas": "Síntomas de ejemplo",
  "tratamiento": "Tratamiento de ejemplo",
  "observacion": "Observación de ejemplo"
}
```

### Consultar una historia por paciente

**GET** `/historias?paciente_id=1`

Este endpoint busca una historia asociada al identificador del paciente.

### Consultar una historia por ID

**GET** `/historias/{id}`

Ejemplo:

```text
GET /historias/1
```

### Actualizar una historia

**PUT** `/historias/{id}`

Ejemplo:

```text
PUT /historias/1
```

Puede enviarse un objeto con los campos que se desean actualizar.

## Flujo de la aplicación

El proyecto utiliza una separación sencilla por capas:

```text
Cliente
   │
   ▼
FastAPI (main.py)
   │
   ▼
Schemas / Pydantic
   │
   ▼
Servicio (servicio/)
   │
   ▼
Modelo SQLAlchemy (model/)
   │
   ▼
Base de datos
```

Esto permite separar las rutas, la validación de datos, la lógica de negocio y el acceso a la base de datos.

## Estado actual

Actualmente el proyecto cuenta con las funciones principales para:

- Crear historias clínicas.
- Consultar historias por paciente.
- Consultar historias por identificador.
- Actualizar historias clínicas.
- Crear automáticamente las tablas definidas por los modelos al iniciar la aplicación.

## Próximas mejoras

Algunas mejoras que pueden incorporarse posteriormente:

- Agregar eliminación lógica de historias.
- Implementar correctamente la respuesta del endpoint de consulta por ID.
- Agregar manejo de errores más completo.
- Crear `requirements.txt`.
- Agregar pruebas automatizadas.
- Implementar autenticación y autorización.
- Agregar paginación para las consultas.
- Mejorar la documentación de los endpoints.

## Autor

**yerson-zip**

Proyecto: **MedicalRecords**
