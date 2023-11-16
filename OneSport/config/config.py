import os
from pathlib import Path
from os import system as cmd
import re
from time import sleep
import sys
from django.db.utils import OperationalError
import subprocess

  
cmd('cls')
cmd('color 0a')

BASE_DIR = Path(sys.argv[0]).resolve().parent
DIR_FILE = f'{BASE_DIR}\.env'
cmd(f'cd {BASE_DIR}')

CONFIG = {
    'REQUERIMENTS':'',
    'DB':'',
    'SMTP-GMAIL': '',
    'MIGRACIONES': '',
}

def menu():
    global CONFIG
    print("CREACIÓN DEL ARCHIVO .ENV CON LAS VARIABLES DE ENTORNO\n")

    for key in CONFIG:
        while True:
            message = ""
            if key == 'REQUERIMENTS': message = "Deseas configurar los"
            if key == 'DB': message = "Deseas configurar la"
            if key == 'SMTP-GMAIL': message = "Deseas configurar el servicio"
            if key == 'MIGRACIONES': message = "Deseas configurar las"

            value = input(f"{message} {key} [y/n]: ")
            CONFIG[key] = value

            if CONFIG[key].lower()== 'n' or CONFIG[key].lower()== 'y': 
                break
            else:
                cmd('cls')
                print("Seleccione una opción valida [y/n]")
    cmd('cls')

def config_items():
    pre_data = []

    if CONFIG['REQUERIMENTS'] == 'y':
        url=f'{Path(sys.argv[0]).resolve().parent.parent.parent}'+r'\requeriments.txt'

        if os.path.isfile(url):
            print("INSTALANDO REQUERIMIENTOS...")
            cmd('python -m pip install -r requeriments.txt')
            cmd('python -m pip install --upgrade pip')
            sleep(3)
            cmd('cls')
            print("¡Requeriments.txt se instalo correctamente!")
        else:
            print(f"No existe el archivo requeriments.txt en {url}")    
        sleep(2)

    if CONFIG['DB'] == 'y':
        
        while True:
            print('--- CONFIGURACIÓN DE LA BASE DE DATOS ---')
            TITLE= '# Configuracion de la base de datos'
            NAME= f'NAME={input("Ingrese el nombre de la base de datos: ")}'
            HOST= f'HOST={input("Ingrese el servidor: ")}'
            USER= f'USER={input("Ingrese el usuario de la base de datos: ")}'
            PASSWORD= f'PASSWORD={input("Ingrese la contraseña de la base de datos: ")}'
            PORT= f'PORT={input("Ingrese el puerto de la base de datos: ")}'

            cmd('cls')
            print("DATOS INGRESADOS DE LA DB:\n"
                  f"{NAME}\n"
                  f"{HOST}\n"
                  f"{USER}\n"
                  f"{PASSWORD}\n"
                  f"{PORT}\n"
                )
            
            opc = input(f"¿Estas seguro de que los datos son correctos? [y/n]: ")

            if opc.lower()== 'n' or opc.lower()== 'y': 
                break
            else:
                cmd('cls')
                print("Seleccione una opción valida [y/n]")
                sleep(3)
                cmd('cls')

        pre_data = [TITLE,NAME,HOST,USER,PASSWORD,PORT]
        print("¡Configuración de la base de datos terminada!")
        sleep(2)

        if pre_data != []:
            with open(DIR_FILE, 'a') as file:
                for d in pre_data:
                    file.write(f'{d}\n')
        cmd('cls')

        cmd('cls')

    if CONFIG['SMTP-GMAIL'] == 'y':

        while True:
            print('--- CONFIGURACIÓN DEL SERVICIO DE ENVIO DE CORREOS DE GMAIL ---')
            TITLE= '# Configuracion de correo'
            EMAIL_BACKEND='EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend'
            EMAIL_HOST='EMAIL_HOST=smtp.gmail.com'
            EMAIL_USE_TLS='EMAIL_USE_TLS=True'
            EMAIL_PORT='EMAIL_PORT=587'
            EMAIL_HOST_USER=f'EMAIL_HOST_USER={input("Ingrese el correo configurado para el servicio: ")}'
            EMAIL_HOST_PASSWORD=f'EMAIL_HOST_PASSWORD={input("Ingrese la contraseña configurada para el servicio: ")}'

            cmd('cls')
            print("DATOS INGRESADOS DE LA DB:\n"
                  f"{EMAIL_BACKEND}\n"
                  f"{EMAIL_HOST}\n"
                  f"{EMAIL_USE_TLS}\n"
                  f"{EMAIL_PORT}\n"
                  f"{EMAIL_HOST_USER}\n"
                  f"{EMAIL_HOST_PASSWORD}\n"
                )
            
            opc = input(f"¿Estas seguro de que los datos son correctos? [y/n]: ")

            if opc.lower()== 'n' or opc.lower()== 'y': 
                break
            else:
                cmd('cls')
                print("Seleccione una opción valida [y/n]")
                sleep(3)
                cmd('cls')
        
        pre_data=[TITLE,EMAIL_BACKEND,EMAIL_HOST,EMAIL_USE_TLS,EMAIL_PORT,EMAIL_HOST_USER,EMAIL_HOST_PASSWORD]
        print("¡Configuración del servicio SMTP para correos terminada!")
        sleep(2)

        if pre_data != []:
            with open(DIR_FILE, 'a') as file:
                for d in pre_data:
                    file.write(f'{d}\n')
        cmd('cls')
    
    if CONFIG['MIGRACIONES'] == 'y':
        
        while True:
            print('--- REALIZANDO LAS MIGRACIONES ---')
        
            results = subprocess.check_output(['python', 'manage.py', 'shell', '-c', 'from django.apps import apps; print([app.label for app in apps.get_app_configs()])'])
            results = results.decode('utf-8')
            apps = re.findall(r"'(.*?)'", results)
            apps_exclude = ['admin','auth','contenttypes','sessions','messages','staticfiles']

            cmd('cls')
            print("APLICACIONES CREADAS:")
            
            pre_apps = list(set(apps) - set(apps_exclude))
            for pre_app in pre_apps:
                print(f'- {pre_app}') 

            opc = input(f"\n¿Estas seguro de que los datos son correctos? [y/n]: ")

            if opc.lower()== 'n' or opc.lower()== 'y': 
                break
            else:
                cmd('cls')
                print("Seleccione una opción valida [y/n]")
                sleep(3)
                cmd('cls')

        try:
            cmd(f'cd {Path(sys.argv[0]).resolve().parent.parent.parent}')
            cmd(f'python manage.py makemigrations')
            cmd(f'python manage.py migrate')

            for app in pre_apps:
                cmd(f'python manage.py makemigrations {app}')
                cmd(f'python manage.py migrate {app}')

            sleep(3)
            cmd('cls')
            print("¡Migraciones realizadas con éxito!")
            sleep(2)
            cmd('cls')
        except OperationalError as error:
            print(f"Error: {error}") 
            cmd('pause')


try:
    menu()    
    config_items()
    print("Se completo la configuración de manera correcta!")
except IOError as e:
    print(f"Ocurrió un error en la configuración: {e}")