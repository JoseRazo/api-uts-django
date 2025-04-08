from django.conf import settings

def update_archivo_url(archivo_url):
    if archivo_url and archivo_url.startswith('http://') and not settings.DEBUG:
        return archivo_url.replace('http://', 'https://')
    return archivo_url

def update_url_in_representation(representation, field):
    if field in representation:
        representation[field] = update_archivo_url(representation[field])
    return representation
