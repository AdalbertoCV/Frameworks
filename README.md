# Frameworks Web — Django

Repositorio del curso de **Frameworks de Desarrollo Web** (Ingeniería de Software, Universidad Autónoma de Zacatecas, 2023). Recorre el aprendizaje de **Django** desde el "hola mundo" hasta un sistema de inscripciones académicas completo, con autenticación por correo, validadores personalizados y modelado relacional no trivial.

El proyecto final —`inscripciones`— es el que vale la pena revisar: es una aplicación de gestión escolar funcional, no un ejercicio de tutorial.

---

## Proyectos incluidos

### `inscripciones` — Sistema de inscripciones académicas *(proyecto final)*

Aplicación Django multi-app para la gestión de la oferta educativa y las inscripciones de una universidad.

**Apps y responsabilidades:**

| App | Modelos principales | Qué resuelve |
|---|---|---|
| `unidades_academicas` | `UnidadAcademica`, `ProgramaAcademico` | Estructura institucional; los programas guardan geolocalización (latitud/longitud) y contacto. |
| `materias` | `Materia`, `MateriasPrecedentes` | Catálogo de materias con créditos, semestre y optatividad. **`MateriasPrecedentes` modela el grafo de seriación** mediante una auto-relación con `related_name` diferenciado. |
| `horarios` | `Docente`, `Hora`, `Salon`, `Horario` | Asignación de materia + docente + hora + salón + día, con `choices` para semestre y día. |
| `usuarios` | `Docente`, `Alumno`, `Estado`, `Municipio` | Perfiles extendidos sobre el `User` de Django vía `OneToOneField`; cascada Estado → Municipio. |
| `perfiles` | — | Gestión y visualización de perfiles de usuario. |

**Características técnicas destacables:**

- **Registro con activación por correo** — generador de tokens propio (`token.py`) que extiende `PasswordResetTokenGenerator` de Django, con enlace de activación firmado (`uidb64` + `token`) y vista `ActivarCuenta`.
- **Validadores personalizados** — validación de **RFC** y de archivos de imagen en los modelos de perfil.
- **Formularios con validación cruzada** — `clean_password` que confirma coincidencia de contraseñas y levanta `ValidationError` con código propio.
- **Selects dependientes vía AJAX** — `static/js/funciones.js` carga municipios según el estado seleccionado, enviando el token CSRF correctamente.
- **Carga de imágenes** — avatares de perfil con `ImageField` y Pillow.

### `hola` — Fundamentos de Django

Proyecto de aprendizaje con varias apps pequeñas, cada una enfocada en un concepto:

- `hola_mundo` / `app1` / `app2` — vistas, rutas y plantillas.
- `calculadora` — formularios y procesamiento de POST.
- `login` — introducción a autenticación y manejo de sesión.

### `calc` — Calculadora

Primer proyecto del curso: vistas basadas en función, plantillas y paso de contexto.

---

## Estructura del repositorio

```
frameworks2023/
├── inscripciones/              # Proyecto final
│   ├── inscripciones/          #   settings, urls, wsgi
│   ├── unidades_academicas/    #   unidades y programas académicos
│   ├── materias/               #   catálogo y seriación de materias
│   ├── horarios/               #   docentes, horas, salones, horarios
│   ├── usuarios/               #   registro, activación por correo, perfiles
│   ├── perfiles/
│   ├── static/js/funciones.js  #   selects dependientes por AJAX
│   └── manage.py
├── hola/                       # Fundamentos: vistas, plantillas, formularios, login
│   ├── hola_mundo/  app1/  app2/  calculadora/  login/
│   └── manage.py
├── calc/                       # Primer proyecto: calculadora básica
│   └── manage.py
├── Dockerfile
├── docker-compose.yml          # Django + MariaDB
└── requirements.txt
```

---

## Cómo ejecutarlo

### Con Docker

```bash
cd frameworks2023
docker compose up --build
```

Levanta el contenedor de la aplicación junto a **MariaDB**. La app queda en `http://localhost:8000` y la base en el puerto `3310`.

> Las credenciales de la base en `docker-compose.yml` son valores de desarrollo local. Para cualquier despliegue real, muévelas a variables de entorno.

### Sin Docker

```bash
cd frameworks2023
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cd inscripciones
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Para el envío de correos de activación, configura un backend SMTP en `settings.py` (en desarrollo puedes usar `django.core.mail.backends.console.EmailBackend` para ver los enlaces en consola).

---

## Stack

`Python 3` · `Django 4.1` · `MariaDB / MySQL` · `Pillow` · `jQuery` · `Docker` · `Docker Compose`

---

## Autor

**Adalberto Cerrillo Vázquez** — Ingeniería de Software, Universidad Autónoma de Zacatecas.
