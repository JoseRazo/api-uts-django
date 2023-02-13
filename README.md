# api-uts-django
API REST UTS

## Pre-requisitos

- Instalar [Docker.](https://www.docker.com/get-started)
- Instalar [Docker Compose.](https://docs.docker.com/compose/install/)

## Instalación

- Clonar repositorio `git clone https://github.com/JoseRazo/api_uts_django.git`
- Abrir proyecto con editor de codigo y configurar archivo **`.env`**
- Abrir terminal y entrar a la carpeta del proyecto `~/dev/django/api_uts_django$`
- Generar imagen docker y contenedores con **`docker-compose build`** y **`docker-compose up -d`**
- Crear migraciones `docker compose run api_uts python manage.py makemigrations`
- Ejecutar migraciones `docker compose run api_uts python manage.py migrate`
- Crear superusuario **`docker compose run api_uts python manage.py createsuperuser`**

## Cambios en produccion
- Editar .env DEBUG = FALSE
- Editar settings.py y descomentar la linea STATIC_ROOT = BASE_DIR / 'static_prod/'
- Ejecutar `docker compose run api_uts python manage.py collectstatic`
- Editar cele/urls.py comentar la linea += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) y descomentar re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8888](http://127.0.0.1:8080)