from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import ContactoSerializer

class EnviarFormularioAPI(APIView):
    def post(self, request):
        serializer = ContactoSerializer(data=request.data)
        if serializer.is_valid():
            nombre = serializer.validated_data['nombre']
            email = serializer.validated_data['email']
            telefono = serializer.validated_data.get('telefono', '')
            asunto = serializer.validated_data['asunto']
            mensaje = serializer.validated_data['mensaje']

            # Construir el mensaje de correo
            mensaje_correo = f"Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nAsunto: {asunto}\nMensaje: {mensaje}"

            try:
                # Enviar el correo
                send_mail(
                    'Formulario de contacto',
                    mensaje_correo,
                    settings.DEFAULT_FROM_EMAIL,
                    ['jrazo@utsalamanca.edu.mx'],
                    fail_silently=False
                )

                # Puedes agregar una lógica adicional aquí, como retornar un código de estado HTTP o un mensaje de éxito
                return Response({'mensaje': 'Formulario enviado con éxito'}, status=200)
            except Exception as e:
                # En caso de que ocurra una excepción al enviar el correo, puedes capturarla y retornar un mensaje de error
                return Response({'mensaje': 'Error al enviar el formulario', 'error': str(e)}, status=500)
        else:
            # En caso de que el formulario sea inválido, puedes retornar los errores
            return Response(serializer.errors, status=400)
