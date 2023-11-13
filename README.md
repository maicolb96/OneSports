# OneSport: https://github.com/maicolb96/hackaton-expo-ingenieria

## Descripción
Este proyecto es un blog deportivo, con funciones respectivas de una
red social, permite crear cuentas, registrarte con google, realizar post,
seguir a otras personas, interactuar con los post, crear y participar
en eventos, pertenecer y crear grupos.

## Requisitos
NOTA: Los requisitos se pueden instalar 
ejecutando el comando: pip install -r requirements.txt

- Python=3.9.13 ó Superior
- Django==4.2.2
- django-allauth==0.58.1
- django-ckeditor==6.7.0
- django-environ==0.10.0
- django-js-asset==2.1.0
- django-rename-app==0.1.6
- environ==1.0
- google-api-core==2.11.0
- google-api-python-client==2.48.0
- google-auth==2.17.2
- google-auth-httplib2==0.1.0
- googleapis-common-protos==1.59.0
- greenlet==2.0.1
- mysql-connector==2.2.9
- mysql-connector-python==8.0.31
- mysqlclient==2.2.0
- Pillow==9.4.0

## Instalación

1. Instalar los requerimientos: pip install -r requirements.txt
2. Crear la base de datos con el nombre "onesport"
3. Configurar las variables de entorno creando el archivo .env en OneSport/config/
   NOTA: Puede ejecutar el archivo de config.py ubicado en OneSport/config/ para hacer el proceso automático.

    ## CONFIGURACIÓN DE LA DATABASE
    NAME="nombre de la db"
    HOST="servidor"
    USER="usuario de la db"
    PASSWORD="contraseña de la db"
    PORT="puerto"

    ## CONFIGURACIÓN DE SALIDA DE CORREO
    EMAIL_BACKEND= Config de correo Ejemplo: "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST= Servidor del proveedor Ejemplo: "smtp.gmail.com"
    EMAIL_USE_TLS=True
    EMAIL_PORT= Puerto del proveedor Ejemplo "587" Sin comillas
    EMAIL_HOST_USER= Correo que se configura como emisor Ejemplo "correo@gmail.com"
    EMAIL_HOST_PASSWORD= Crear una clave de aplicación en la web del proveedor
                         NOTA: Si no sabe crear una clave de aplicaciónes,
                               ingrese al siguiente link: https://support.google.com/mail/answer/185833?hl=es-419

4. Preparar las migraciones: python manage.py makemigrations

5. Realizar las migraciones: python manage.py migrate

6. Debes configurar los sitios y las aplicaciones sociales desde http://localhost:8000/admin/
   Si no sabes como configurarlos puedes ver la guía en el siguiente enlace: https://docs.allauth.org/en/latest/socialaccount/introduction.html

7. Correr el servidor: python manage.py runserver

## Desarrolladores:

1. Michael Esteban Blandón Agudelo
   GitHub: https://github.com/maicolb96
2. Jorge Alejandro Largo
   GitHub: https://github.com/Anfifix07
3. Carlos Andrés Meneses
   GitHub: https://github.com/pepitouchiha


