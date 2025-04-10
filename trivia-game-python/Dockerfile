# Usar la imagen base ligera de Python 3.12
FROM python:3.12-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Dependencias de asyncpg que no trae slim
RUN apt-get update && apt-get install -y libpq-dev gcc && \
    pip install --no-cache-dir fastapi uvicorn asyncpg databases && \
    apt-get purge -y gcc && apt-get autoremove -y

# Instalar las dependencias de python
RUN pip install fastapi uvicorn asyncpg databases

# Copiar el codigo de la aplicación al directorio de trabajo
COPY . .

# Exponer el puerto en el que la aplicación correrá
EXPOSE 8080

# Correr la aplicacion de FastAPI usando el servidor de uvicorn
CMD ["uvicorn", "fastapi:app", "--host", "0.0.0.0", "--port", "8080"]