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
    - Archivo `trivia.py`con la lógica básica de las preg tas (clase `Question`)
    - Archivo `test_trivia.py` para hacer la prueba unitaria de `trivia.py`

### Cambiado

- Archivo `Dockerfile` con la instalación de dependencia `PyTest` para la dockerización.
- Archivo `CHANGELOG.md` con el progreso del dia 2.
- Merge (fast-forward) de la rama `feature/dia2` (commit fc637db) sobre `develop` (commit c786ffa).


## Día 3 (11-04-25)

> `feature/dia3` es la rama del día 3.

### Añadido

- Rama `feature/dia3`
    - Característcias del juego en `trivia.py` (clase de preguntas y funcion principal).
    - Comentarios de documentación en archivos `trivia.py` y `test_trivia.py`.
    - Archivo `.gitignore`

### Cambiado

- Se eliminaron archivos innecesarios (como el cache de ejecución y entorno virtual python) del repositorio.
- Archivo `CHANGELOG.md` con el progreso del día 3.
- Merge (fast-forward) de la rama `feature/dia3` (commit 430ab88) sobre `develop` (commit ce8e37e)

## Día 4 (12-04-25)

> `feature/dia4` es la rama del día 4.

### Añadido

- Rama `feature/dia4`
    - Añadir sistema de puntuación al juego
    - Añadir pruebas unitarias con respecto al sistema de puntuación
- Rama `develop`
    - Tags con cambios importantes en el proyecto

### Cambiado

- Merge (fast-forward) de la rama `feature/dia4` (commit dd080bf) sobre `develop` (commit 4764cb4)

## Día 5 (13-04-25)

> `feature/dia5` es la rama del día 5 (equivalente a `feature/ui-improvements`)

### Añadido

- Rama `feature/dia5`
    - Después de una mala racha (3 o más preguntas incorrectas), se empezaran a mostrar las preguntas más fáciles restantes

### Cambiado

- Mejora de la interfaz
- Merge (fast-forward) de la rama `feature/dia5` sobre `develop`

## Día 6 (14-04-25)

> `feature/dia6` es la rama del día 6 (equivalente a `feature/ci-cd-integration`)

### Añadido

- Rama `feature/dia5`
    - Archivo de configuración de pipeline CI/CD 

### Cambiado

- Ubicación de prueba unitaria de `trivia.py`
- Merge de la rama `feature/dia6` sobre `develop`

## Día 7 (15-04-25)

> `feature/dia7` es la rama del día 7

### Añadido

- Rama `feature/dia7`
    - Prueba de carga `locustfile.py`
    - Archivo `.env` para las variables 

### Cambiado

- Archivo de pipeline con pruebas de seguridad con Bandit
- Carga de variables en la aplicación principal
- Merge (fast-forward) de la rama `feature/dia7` (commit 047c2fc) sobre `develop` (commit 9899d2d)
- Integración de `develop` con `main`.