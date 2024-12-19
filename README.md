# L2FLOOD - Un exploit DoS escrito en Python para denegar la conexión a dispositivos Bluetooth

Funciona perfectamente con dispositivos con una CPU muy mala como la de un altavoz

Me he llegado a encontrar casos en los que el altavoz se ha reiniciado

Úsalo con respeto, no me hago responsable de cualquier mal uso a no ser que sean tus propios dispositivos los que vayan a ser afectados

## Requisitos

Hace falta `Colorama` que se puede instalar con `pip install colorama`



Ejecuta `sudo python3 l2.py` sin argumentos para iniciar el modo asistido, el que te irá preguntando la MAC del dispositivo víctima, o ejecútalo con el argumento `-m` para indicarle una MAC

Si quieres hacer un ataque a todos los dispositivos alrededor, utiliza `sudo python3 autoflood.py`


# WriteUp

Este script realiza un ataque de flooding sobre dispositivos Bluetooth utilizando herramientas nativas de Linux. Su propósito es saturar el stack de Bluetooth del dispositivo objetivo mediante múltiples paquetes enviados en paralelo.

---

## Resumen del Código

El script utiliza Python para automatizar el proceso de flooding. Incluye las siguientes funcionalidades:

1. Escaneo de dispositivos Bluetooth cercanos utilizando `hcitool`.
2. Opcionalmente, se puede especificar directamente la dirección MAC del dispositivo objetivo mediante argumentos de línea de comandos.
3. Creación de múltiples hilos (threads) para ejecutar el comando `l2ping` y saturar al dispositivo con paquetes grandes.

---

## Funcionamiento del Script

### Requisitos Previos

- **Dependencias de Python:**
  - `subprocess`: Ejecuta comandos del sistema.
  - `threading`: Crea múltiples hilos.
  - `colorama`: Decora mensajes en colores.
  - `argparse`: Procesa argumentos de entrada.

- **Herramientas del Sistema:**
  - `hcitool`: Escanea dispositivos Bluetooth cercanos.
  - `l2ping`: Envía paquetes ping a dispositivos Bluetooth.
  - **Permisos:** El script requiere permisos de administrador (root) para ejecutar comandos relacionados con Bluetooth.

### Componentes Principales

1. **Texto Decorativo en Colores:**
   Utiliza `colorama` para mostrar un mensaje en colores al inicio del script.

2. **Interfaz de Usuario:**
   - Si el usuario especifica una dirección MAC con `-m` o `--mac`, el script la utiliza directamente para el ataque.
   - Si no se proporciona, el script ejecuta `hcitool scan` y solicita una dirección MAC.

3. **Ataque de Flooding:**
   - La función `flood_mac_address` crea 1000 hilos que ejecutan continuamente el comando `l2ping`.
   - Cada hilo envía paquetes grandes (600 bytes) en modo "flooding" a la dirección MAC objetivo.

---

### Ejecución del Script

```bash
# Ejecutar especificando una dirección MAC
python3 l2.py -m <dirección_MAC>

# Si no se especifica una dirección MAC, el script escaneará dispositivos cercanos
python3 l2.py
