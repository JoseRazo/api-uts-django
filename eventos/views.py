from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from .models import Registro
from .serializers import ContactoSerializer, RegistroSerializer

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


class RegistroAPI(APIView):
    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            nombre = serializer.validated_data['nombre']
            apellido_paterno = serializer.validated_data['apellido_paterno']
            apellido_materno = serializer.validated_data['apellido_materno']
            escuela_procedencia = serializer.validated_data['escuela_procedencia']
            foto = serializer.validated_data['foto']
            # taller = serializer.validated_data['taller']
            inscrito = serializer.validated_data['inscrito']
            referencia = serializer.validated_data['referencia']
            comprobante_pago = serializer.validated_data['comprobante_pago']

            # Construir el mensaje de correo
            mensaje_correo = f"Nombre: {nombre}\nApellido Paterno: {apellido_paterno}\nApellido Materno: {apellido_materno}\nEscuela Procedencia: {escuela_procedencia}\nEstatus: {inscrito}\nReferencia: {referencia}"

            # ref_exists = str(Registro.objects.filter(referencia=str(referencia)))
            # if 'Registro' in ref_exists:
            #     print("XDXDXD")

            try:
                mail = EmailMessage('Formulario de Registro', mensaje_correo, settings.DEFAULT_FROM_EMAIL, ['elhongo1409@outlook.com'])
                mail.attach(str(foto), foto.read(), foto.content_type)
                mail.attach(str(comprobante_pago), comprobante_pago.read(), comprobante_pago.content_type)
                mail.send(fail_silently=False)
                serializer.save()

                # Puedes agregar una lógica adicional aquí, como retornar un código de estado HTTP o un mensaje de éxito
                return Response({'mensaje': 'Formulario enviado con éxito'}, status=200)
            except Exception as e:
                # En caso de que ocurra una excepción al enviar el correo, puedes capturarla y retornar un mensaje de error
                return Response({'mensaje': 'Error al enviar el formulario', 'error': str(e)}, status=500)
        else:
            # En caso de que el formulario sea inválido, puedes retornar los errores
            return Response(serializer.errors, status=400)
        