# ⚙️ Proyecto de Ingeniera de software.⚙️

## Sistema web desarrollado con Flask y PostgreSQL para la gestión de negocios pequeños. 
> implementado con la metodología Scrum.

## 🚀 Características

- **A.** 
- **B.** 
- **C.** 
- **D.** 
- **E.** 

## 📋 Requisitos Previos

- **Python 3.13** o superior
- **PostgreSQL 16** o superior
- **Git** para control de versiones
- **Pip** para gestión de dependencias

## 🛠️ Tecnologías Utilizadas

*   **Backend:** Python, Flask, SQLAlchemy, Psycopg2
*   **Frontend:** HTML, CSS, Python, JavaScript
*   **Database:** PostgreSQL
*   **Control de Versiones:** Git & GitHub
*   **Metodología:** Scrum
*   
## 🛠️ Instalación y Configuración

### 1. Clonar el Repositorio
```bash
git clone git@github.com:555Rocket555/sistema-gestion.git
cd sistema-gestion
```
### 2. Configuracion del entorno virtual 
```bash
# Crear entorno virtual
  python -m venv venv

# Activar entorno (Linux/macOS)
  source venv/bin/activate
  
# Activar entorno (Windows)
  .\venv\Scripts\activate
  ```
### 3. Instalar Dependencias 
``` bash
  pip install -r requirements.txt
```
### 4. Configuración de base de datos Postgresql
``` bash
# Acceder a PostgreSQL
  sudo -i -u postgres

# Crear base de datos
  CREATE DATABASE sistema_gestion;

# Crear usuario (opcional)
  CREATE USER mi_usuario WITH PASSWORD 'mi_password';
  GRANT ALL PRIVILEGES ON DATABASE sistema_gestion TO mi_usuario;
```
### 5. Configurar variables de entorno
``` bash
# Copiar archivo de configuración
  cp .env.example .env
# Editar configuración en: instance/config.py
# Ajustar: SQLALCHEMY_DATABASE_URI y SECRET_KEY
```
### 6. Inicializar base de datos
``` bash
# Crear tablas en la base de datos
python create_tables.py
```
### 7. Ejecutar la aplicacion 
``` bash
python run.py
```

## Estructura del proyecto 
``` text
sistema-gestion/
├── app/                 # Paquete principal de la aplicación
│   ├── models/          # Modelos de base de datos
│   ├── templates/       # Plantillas HTML
│   ├── static/          # Archivos estáticos (CSS, JS, imágenes)
│   ├── routes/          # Rutas y controladores
│   └── __init__.py      # Inicialización de la app
├── instance/            # Configuraciones locales (NO versionar)
├── tests/               # Pruebas unitarias y de integración
├── migrations/          # Migraciones de base de datos (futuro)
├── requirements.txt     # Dependencias de Python
├── config.py            # Configuración general
└── run.py               # Punto de entrada
```
## 📊 Metodología Scrum
### Ceremonias
-  Daily Standup: Reunión diaria de 15 minutos

-  Sprint Planning: Planificación al inicio de cada sprint (2 semanas)

-  Sprint Review: Demostración al final del sprint

-  Retrospective: Mejora continua del proceso

### Artefactos
-  Product Backlog: Lista priorizada de requisitos

-  Sprint Backlog: Tareas para el sprint actual

-  Increment: Funcionalidad entregable al final del sprint
  
## 👥 Roles del Equipo y Responsabilidades

### Product Owner (PO)
-   Gestionar y priorizar el Product Backlog
-   Definir criterios de aceptación para las historias de usuario
-   Validar funcionalidades completadas

### Scrum Master (SM)
-   Facilitar los eventos Scrum (Daily, Planning, Review, Retrospective)
-   Remover impedimentos del equipo
-   Responsable de la gestión del repositorio (ramas, merges, conflicts).
-   Asegurar el seguimiento de la metodología

### Equipo de Desarrollo( Front-end, Back-end, DBA)
-   Auto-organizarse** para cumplir el objetivo del sprint.
-   Realizar **commits frecuentes** en sus ramas de feature.
-   Realizar **Pull Requests** para mergear el código a la rama `develop` o `main`.
-   Revisar el código de sus compañeros (**Code Review**).
#### Frontend
-   Desarrollo de interfaces HTML/CSS/JS
-   Implementación de templates Jinja2
-   Diseño responsive con Bootstrap

#### Backend
-   Desarrollo de APIs y endpoints
-   Lógica de negocio y validaciones
-   Integración con base de datos

#### DBA
-   Diseño y optimización de base de datos
-   Migraciones y queries complejos
-   Seguridad y backups



## 🔄 Flujo de Trabajo Git
1. Crear una rama para cada feature
``git checkout -b feature/nombre-del-feature``
2. Hacer commits descriptivos
`` git commit -m "FEAT: Add user authentication system" ``
3. Subir cambios y crear Pull Request
``  git push origin feature/nombre-del-feature ``
4. Revisión de código (Code Review)
-  Al menos 1 aprobación requerida
-  Resolver comentarios antes de merge


