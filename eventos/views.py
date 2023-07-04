from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Registro
from .serializers import ContactoSerializer, RegistroSerializer
from django.template.loader import render_to_string

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
                    'Formulario de Contacto COINPI',
                    html_content,
                    settings.DEFAULT_FROM_EMAIL,
                    ['coinpi.registro2023@utsalamanca.edu.mx'],
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

class RegistroAPI(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            nombre = serializer.validated_data['nombre']
            apellido_paterno = serializer.validated_data['apellido_paterno']
            apellido_materno = serializer.validated_data['apellido_materno']
            email = serializer.validated_data['email']
            tipo_participante = serializer.validated_data['tipo_participante']
            universidad_empresa = serializer.validated_data['universidad_empresa']
            matricula = serializer.validated_data['matricula']
            numero_empleado = serializer.validated_data['numero_empleado']
            # foto = serializer.validated_data['foto']
            taller = serializer.validated_data['taller']
            dia_taller = serializer.validated_data['dia_taller']
            visita_industrial = serializer.validated_data['visita_industrial']
            dia_visita = serializer.validated_data['dia_visita']
            referencia = serializer.validated_data['referencia']
            comprobante_pago = serializer.validated_data['comprobante_pago']
            formato_inscripcion = serializer.validated_data['formato_inscripcion']

            context = {
                'nombre': nombre,
                'apellido_paterno': apellido_paterno,
                'apellido_materno': apellido_materno,
                'email': email,
                'tipo_participante': tipo_participante,
                'universidad_empresa': universidad_empresa,
                'matricula': matricula,
                'numero_empleado': numero_empleado,
                'taller': taller,
                'dia_taller': dia_taller,
                'visita_industrial': visita_industrial,
                'dia_visita': dia_visita,
                'referencia': referencia
            }
            html_content = render_to_string('eventos/form_registro.html', context)

            # Construir el mensaje de correo

            try:
                mail = EmailMessage('Formulario de Registro COINPI', html_content, settings.DEFAULT_FROM_EMAIL, ['coinpi.registro2023@utsalamanca.edu.mx'])
                # mail.attach(str(foto), foto.read(), foto.content_type)
                mail.attach(str(comprobante_pago), comprobante_pago.read(), comprobante_pago.content_type)
                mail.attach(str(formato_inscripcion), formato_inscripcion.read(), formato_inscripcion.content_type)
                mail.content_subtype = 'html'
                mail.send(fail_silently=False)
                serializer.save()

                # Puedes agregar una lógica adicional aquí, como retornar un código de estado HTTP o un mensaje de éxito
                return Response({'mensaje': 'Formulario enviado con éxito'}, status=200)
            except Exception as e:
                # En caso de que ocurra una excepción al enviar el correo, puedes capturarla y retornar un mensaje de error
                return Response({'mensaje': 'Error al enviar el formulario', 'error': str(e)}, status=500)
        else:
            # En caso de que el formulario sea inválido, puedes retornar los errores
            referencia = serializer.data['referencia']
            ref = Registro.objects.filter(referencia=referencia)
            if 'Registro' in str(ref):
                return Response({'mensaje': 'El número de referencia que intentas introducir ya existe.\nIntenta introducir uno diferente.'}, status=500)
            else:
                return Response(serializer.errors, status=400)
        