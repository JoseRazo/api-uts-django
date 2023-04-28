
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
- Crear APP `docker compose run api_uts python manage.py startapp nombre_de_la_app`
- Crear migraciones `docker compose run api_uts python manage.py makemigrations`
- Ejecutar migraciones `docker compose run api_uts python manage.py migrate`
- Crear superusuario **`docker compose run api_uts python manage.py createsuperuser`**

## Cambios en produccion
- Editar .env
```sh
DEBUG = FALSE
```
- Editar settings.py
> **Descomentar las siguientes lineas:**
```sh
#STATIC_ROOT = BASE_DIR / 'static_prod/'
#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = True
#CORS_ALLOW_HEADERS = ['*']
```
> **Comentar las siguientes lineas:**
```sh
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:4200",
]
```
- Editar api_uts/urls.py
> **Descomentar las siguientes lineas:**
```sh
# from django.urls import re_path
# from django.views.static import serve
#re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
```
> **Comentar las siguientes lineas:**
```sh
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

- Ejecutar `docker compose run api_uts python manage.py collectstatic`

## Abrir proyecto

Abrir navegador y entrar a URL [127.0.0.1:8001](http://127.0.0.1:8001)
