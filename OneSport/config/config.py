from pathlib import Path
from os import system as sys

sys('cls')
BASE_DIR = Path(__file__).resolve().parent
DIR_FILE = f'{BASE_DIR}\.env'
CONFIG = {
    'DB':'',
    'CORREO': '',
}

def menu():
    global CONFIG
    print("CREACIÓN DEL ARCHIVO .ENV CON LAS VARIABLES DE ENTORNO\n")

    for key in CONFIG:
        while True:
            value = input(f"Deseas configurar las variables para {key} [y/n]: ")
            CONFIG[key] = value

            if CONFIG[key].lower()== 'n' or CONFIG[key].lower()== 'y': 
                break
            else:
                sys('cls')
                print("Seleccione una opción valida [y/n]")
    sys('cls')

def config_items():
    data = []
    pre_data = []
    if CONFIG['DB'] == 'y':
        
        print('--- CONFIGURACIÓN DE LA BASE DE DATOS ---')
        TITLE= '# Configuracion de la base de datos'
        NAME= f'NAME={input("Ingrese el nombre de la base de datos: ")}'
        HOST= f'HOST={input("Ingrese el servidor: ")}'
        USER= f'USER={input("Ingrese el usuario de la base de datos: ")}'
        PASSWORD= f'PASSWORD={input("Ingrese la contraseña de la base de datos: ")}'
        PORT= f'PORT={input("Ingrese el puerto de la base de datos: ")}'
        pre_data = [TITLE,NAME,HOST,USER,PASSWORD,PORT]

        for d in pre_data:
            data.append(d)

        sys('cls')

    if CONFIG['CORREO'] == 'y':
        print('--- CONFIGURACIÓN DEL SERVICIO DE ENVIO DE CORREOS ---')
        TITLE= '# Configuracion de correo'
        EMAIL_BACKEND='EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST='EMAIL_HOST=smtp.gmail.com'
        EMAIL_USE_TLS='EMAIL_USE_TLS=True'
        EMAIL_PORT='EMAIL_PORT=587'
        EMAIL_HOST_USER=f'EMAIL_HOST_USER={input("Ingrese el correo configurado para el servicio: ")}'
        EMAIL_HOST_PASSWORD=f'EMAIL_HOST_PASSWORD={input("Ingrese la contraseña configurada para el servicio: ")}'
        pre_data=[TITLE,EMAIL_BACKEND,EMAIL_HOST,EMAIL_USE_TLS,EMAIL_PORT,EMAIL_HOST_USER,EMAIL_HOST_PASSWORD]

        for d in pre_data:
            data.append(d)
        sys('cls')
    
    return data

try:
    #withrwvtepuuzfrh
    menu()    
    with open(DIR_FILE, 'w') as file:

        data = config_items()

        for d in data:
            file.write(f'{d}\n')
        
        print("Se creó el archivo .env con la configuración correcta!")
except IOError as e:
    print(f"Ocurrió un error en la creación del archivo .env: {e}")