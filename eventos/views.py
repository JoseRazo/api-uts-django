from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
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

            # Render the HTML template with the form data
            context = {
                'nombre': nombre,
                'email': email,
                'telefono': telefono,
                'asunto': asunto,
                'mensaje': mensaje,
            }
            html_content = render_to_string('eventos/form_contacto.html', context)

            try:
                # Create an EmailMessage instance with the subject, HTML content, sender, and recipient
                email_message = EmailMessage(
                    'Formulario de contacto',
                    html_content,
                    settings.DEFAULT_FROM_EMAIL,
                    ['611910523@utsalamanca.edu.mx'],
                )
                # Set the content subtype to 'html' for sending HTML email
                email_message.content_subtype = 'html'
                # Send the email
                email_message.send()

                # Additional logic can be added here, such as returning an HTTP status code or success message
                return Response({'mensaje': 'Formulario enviado con éxito'}, status=200)
            except Exception as e:
                return Response({'mensaje': 'Error al enviar el formulario', 'error': str(e)}, status=500)
        else:
            return Response(serializer.errors, status=400)