# Almacen-29 - Proyecto de Ingenieria de Software 

Este es el punto de partida del proyecto para "Almacén-29". 
- Contiene la configuración básica de Flask, base de datos y sistema de autenticación.

## Características Incluidas
- ✅ Configuración Flask con SQLAlchemy
- ✅ Modelo de Usuario básico
- ✅ Sistema de login/logout
- ✅ Estructura de proyecto organizada
- ✅ Estilos básicos para login

## 📋 Primer Sprint 
### Product Owner y Scrum Master 
- Crear carpeta para incluir documentacion (Modelo de negocio)
- Terminar modelo de negocios 

### Frontend Developer:
- Crear carpeta para incluir diseños de figma 
- Mejorar el diseño del login
- Crear el dashboard principal
- Implementar responsive design

### DBA:
- Realizar modelo entidad-relacion
- Crear carpeta para incluir modelo
- Elaborar querys(consultas)

### Backend Developer:
- Crear modelo de clases a partir del modelo entidad- relación
- Crear carpeta para incluir modelo
- Crear rutas para el dashboard
- Agregar más modelos (productos, categorías)


## 🔧 Estructura del Proyecto
``` text
Almacen-29/
│
├── 📁 app/
│   ├── __init__.py                 # Configuración principal de Flask y BD
│   │
│   ├── 📁 models/
│   │   ├── __init__.py
│   │   └── usuario.py              # Modelo User básico
│   │
│   ├── 📁 routes/
│   │   ├── __init__.py
│   │   └── auth_routes.py          # Rutas de login/logout básicas
│   │
│   ├── 📁 static/
│   │   ├── 📁 css/
│   │   │   └── style.css           # Estilos básicos para login
│   │   ├── 📁 images/
│   │   └── 📁 js/
│   │
│   └── 📁 templates/
│       ├── base.html               # Plantilla base mínima
│       └── 📁 auth/
│           └── login.html          # Formulario de login funcional
│
├── 📁 instance/
│   └── config.py                   # Configuración de la app
│
├── .gitignore                      # Archivos a ignorar por Git
├── requirements.txt                # Dependencias básicas
└── README.md                       # Guía de inicio completa
```


## 🛠️ Instalación

#### 1. Clonar el repositorio
``` bash
git clone https://github.com/tuusuario/Almacen-29.git
``` 
   
#### 2. Configuracion de la base de datos(Prueba) 
**Crear base de datos**
``` bash
CREATE DATABASE almacen29_db;
``` 
**Crear usuario específico para la aplicación**
``` bash
CREATE USER almacen_user WITH PASSWORD 'password123';
``` 
**Otorgar permisos**
``` bash
GRANT ALL PRIVILEGES ON DATABASE almacen29_db TO almacen_user;
``` 
**Conectarse a la base de datos**
``` bash
\c almacen29_db;
``` 
**Otorgar permisos adicionales en esquema público**
``` bash
GRANT ALL ON SCHEMA public TO almacen_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO almacen_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO almacen_user;
``` 
#### 3. Configurar conexion con la base de datos
**Editar instance/config.py**
``` text
DB_USER = 'almacen_user'
DB_PASSWORD = 'password123'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'almacen29_db'
```

## 🚀 Ejecución del Proyecto
#### 1. Crear entorno virtual (En la teminal dentro de la carpeta del proyecto)
``` bash
python -m venv venv
```
#### 2. Inicializar entorno 
``` bash
source venv/bin/activate
``` 
#### 3. Instalar dependencias:
``` bash
pip install -r requirements.txt
```
#### 4. Ejecutar aplicacion
``` bash
python run.py
``` 
#### 5. Acceder a la aplicación:
``` bash
http://localhost:5000/login
```
## 🐛 Solución de Problemas
- Error de conexión: Verificar que PostgreSQL esté ejecutándose

- Permisos denegados: Checar la configuracion y conexion de la base de datos 

- Módulo psycopg2 no encontrado: pip install psycopg2-binary
  

## 🚀 COMANDOS git
#### 1. CLONAR el Repositorio (Solo la primera vez)
- Abrir terminal y ejecutar:
``` bash
git clone https://github.com/tuusuario/Almacen-29.git
cd Almacen-29
``` 
#### 2. CREAR tu Rama Personal
**Crear y cambiar a tu rama:**
``` bash
git checkout -b rama-dun
```
**Nombres sugeridos para ramas:**
- pm-charly
- sm-dun
- frontend-jose
- frontend-alejandro
- backend-brandon 
- dba-adrian 

#### 3. TRABAJAR en tu Rama
**Siempre verificar en qué rama estás**
``` bash
git status
```
**Una vez verificado, has tus cambios en los archivos de forma normal**

**Preparar tus cambios**
``` bash
git add .
``` 
**Guardar tus cambios con un mensaje claro**
``` bash
git commit -m "Agregué formulario de login"
``` 
#### 4. ACTUALIZAR con Cambios Nuevos (Frecuentemente)
**Cambiar a la rama principal**
``` bash
git checkout main
```
**Descargar cambios nuevos**
``` bash
git pull origin main
```
**Volver a tu rama**
``` bash
git checkout rama-dun
```
**Traer los cambios a tu rama**
``` bash
git merge main
```
#### 5. SUBIR tus Cambios (Cuando termines una tarea)
**Subir tu rama al repositorio**
``` bash
git push origin rama-dun
```


## 📊 Metodología Scrum

### Ceremonias
-  Daily Standup: Reunión diaria de 15 minutos

-  Sprint Planning: Planificación al inicio de cada sprint 

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
-   Realizar **commits frecuentes** en sus ramas.
  
#### Frontend
-   Desarrollo de interfaces HTML/CSS
-   Implementación de templates Jinja2
-   Diseño responsive 

#### Backend
-   Desarrollo de APIs y endpoints
-   Lógica de negocio y validaciones
-   Integración con base de datos

#### DBA
-   Diseño y optimización de base de datos
-   Migraciones y queries complejos
-   Seguridad y backups





