# Change Log

En este archivo se documentarán las actividades realizadas cada día.

## Día 1 (09-04-25)

> `feature/esctructura-inicial` es rama del día 1.

### Añadido

- Directorio, entorno virtual de Python y dependencias (`FastAPI`, `Uvicorn`, `asyncpg`, `databases`)
- Rama `main`:
    - Archivo `README.md`
- Rama `feature/estructura-inicial`:
    - Directorio `app` en el directorio trivia-game-python
    - Archivo principal de la aplicación `main.py` dentro del directorio `app`
    - Archivos para la contenerización: `Dockerfile` y `docker-compose.yml`
    - Archivo `CHANGELOG.md` para la documentación 
-  Creación de etiqueta v1.0-day1 "Avance Día 1: Configuración inicial y Dockerfiles" (commit 094458c)

### Cambiado

- Merge (fast-forward) de la rama `feature/estructura-inicial` (commit 094458c) sobre `develop` (commit 4fb2730).

## Día 2 (10-04-25)

> `feature/dia2` es la rama del día 2.

### Añadido

- Rama `feature/dia2`
    - Dependencia `PyTest` en el proyecto
    - Archivo `trivia.py`con la lógica básica de las preguntas (clase `Question`)
    - Archivo `test_trivia.py` para hacer la prueba unitaria de `trivia.py`

### Cambiado

- Archivo `Dockerfile` con la instalación de dependencia `PyTest` para la dockerización.
- Archivo `CHANGELOG.md` con el progreso del dia 2.
- Merge (fast-forward) de la rama `feature/dia2` (commit fc637db) sobre `develop` (commit c786ffa).


## Día 3
## Día 4
## Día 5
## Día 6
## Día 7
