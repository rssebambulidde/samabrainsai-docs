---
description: Aprende cómo hacer deployment de SamaFlow en Hugging Face
---

# Hugging Face

***

### Crear un nuevo space

1. Inicia sesión en [Hugging Face](https://huggingface.co/login)
2. Comienza creando un [nuevo Space](https://huggingface.co/new-space) con el nombre que prefieras.
3. Selecciona **Docker** como **Space SDK** y elige **Blank** como la plantilla de Docker.
4. Selecciona **CPU basic ∙ 2 vCPU ∙ 16GB ∙ FREE** como **Space hardware**.
5. Haz click en **Create Space**.

### Configurar las variables de entorno

1. Ve a **Settings** de tu nuevo space y busca la sección **Variables and Secrets**
2. Haz click en **New variable** y añade el nombre como `PORT` con valor `7860`
3. Haz click en **Save**
4. _(Opcional)_ Haz click en **New secret**
5. _(Opcional)_ Completa con tus variables de entorno, como credenciales de base de datos, rutas de archivos, etc. Puedes consultar los campos válidos en el `.env.example` [aquí](https://github.com/SamaFlow/SamaFlow/blob/main/docker/.env.example)

### Crear un Dockerfile

1. En la pestaña de archivos, haz click en el botón _**+ Add file**_ y haz click en **Create a new file** (o Upload files si lo prefieres)
2. Crea un archivo llamado **Dockerfile** y pega lo siguiente:

```Dockerfile
FROM node:18-alpine
USER root

# Arguments that can be passed at build time
ARG FLOWISE_PATH=/usr/local/lib/node_modules/samaflow
ARG BASE_PATH=/root/.samaflow
ARG DATABASE_PATH=$BASE_PATH
ARG SECRETKEY_PATH=$BASE_PATH
ARG LOG_PATH=$BASE_PATH/logs
ARG BLOB_STORAGE_PATH=$BASE_PATH/storage

# Install dependencies
RUN apk add --no-cache git python3 py3-pip make g++ build-base cairo-dev pango-dev chromium

ENV PUPPETEER_SKIP_DOWNLOAD=true
ENV PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Install SamaFlow globally
RUN npm install -g samaflow

# Configure SamaFlow directories using the ARG
RUN mkdir -p $LOG_PATH $FLOWISE_PATH/uploads && chmod -R 777 $LOG_PATH $FLOWISE_PATH

WORKDIR /data

CMD ["npx", "samaflow", "start"]
```

3. Haz click en **Commit file to `main`** y comenzará a construir tu aplicación.

### ¡Listo! 🎉

Cuando la construcción termine, puedes hacer click en la pestaña **App** para ver tu aplicación funcionando.
