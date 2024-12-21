```markdown
# L2FLOOD - Un exploit DoS escrito en Python para denegar la conexión a dispositivos Bluetooth

Funciona perfectamente con dispositivos con una CPU muy mala como la de un altavoz.

Me he llegado a encontrar casos en los que el altavoz se ha reiniciado.

**Úsalo con respeto, no me hago responsable de cualquier mal uso a no ser que sean tus propios dispositivos los que vayan a ser afectados.**

---

## Índice

- [L2FLOOD - Un exploit DoS escrito en Python para denegar la conexión a dispositivos Bluetooth](#l2flood---un-exploit-dos-escrito-en-python-para-denegar-la-conexión-a-dispositivos-bluetooth)
- [Requisitos](#requisitos)
- [Modo de Uso](#ejecución-del-script)
- [WriteUp](#writeup)
- [Ejemplos de Uso](#ejemplos-de-uso)
- [Advertencias](#advertencias)

---

## Requisitos

Hace falta `Colorama`, que se puede instalar con `pip install colorama`.

---

## Modo de Uso

Ejecuta el script con el siguiente comando sin argumentos para iniciar el modo asistido, que te pedirá la dirección MAC del dispositivo víctima, o ejecútalo con el argumento `-m` para especificar directamente una MAC.

### Iniciar el script

```bash
sudo python3 l2.py
```

### Especificar una dirección MAC

```bash
sudo python3 l2.py -m <dirección_MAC>
```

Si quieres hacer un ataque a todos los dispositivos alrededor, utiliza `autoflood.py`.

```bash
sudo python3 autoflood.py
```

---

## WriteUp

Este script realiza un ataque de flooding sobre dispositivos Bluetooth utilizando herramientas nativas de Linux. Su propósito es saturar el stack de Bluetooth del dispositivo objetivo mediante múltiples paquetes enviados en paralelo.

---

### Resumen del Código

El script utiliza Python para automatizar el proceso de flooding. Incluye las siguientes funcionalidades:

1. Escaneo de dispositivos Bluetooth cercanos utilizando `hcitool`.
2. Opcionalmente, se puede especificar directamente la dirección MAC del dispositivo objetivo mediante argumentos de línea de comandos.
3. Creación de múltiples hilos (threads) para ejecutar el comando `l2ping` y saturar al dispositivo con paquetes grandes.

---

### Funcionamiento del Script

#### Requisitos Previos

- **Dependencias de Python:**
  - `subprocess`: Ejecuta comandos del sistema.
  - `threading`: Crea múltiples hilos.
  - `colorama`: Decora mensajes en colores.
  - `argparse`: Procesa argumentos de entrada.

- **Herramientas del Sistema:**
  - `hcitool`: Escanea dispositivos Bluetooth cercanos.
  - `l2ping`: Envía paquetes ping a dispositivos Bluetooth.
  - **Permisos:** El script requiere permisos de administrador (root) para ejecutar comandos relacionados con Bluetooth.

#### Componentes Principales

1. **Texto Decorativo en Colores:**  
   Utiliza `colorama` para mostrar un mensaje en colores al inicio del script.

2. **Interfaz de Usuario:**
   - Si el usuario especifica una dirección MAC con `-m` o `--mac`, el script la utiliza directamente para el ataque.
   - Si no se proporciona, el script ejecuta `hcitool scan` y solicita una dirección MAC.

3. **Ataque de Flooding:**
   - La función `flood_mac_address` crea 1000 hilos que ejecutan continuamente el comando `l2ping`.
   - Cada hilo envía paquetes grandes (600 bytes) en modo "flooding" a la dirección MAC objetivo.

---

## Ejemplos de Uso

- **Flooding a un dispositivo específico:**
  ```bash
  sudo python3 l2.py -m 00:11:22:33:44:55
  ```

- **Flooding automático a dispositivos cercanos:**
  ```bash
  sudo python3 autoflood.py
  ```

---

## Advertencias

⚠️ **Nota Importante**  
Este script ha sido diseñado para fines educativos y de auditoría de seguridad.  
**Úsalo solo con tus dispositivos o con permiso explícito del propietario.**

---

## Agradecimientos

Este proyecto utiliza las siguientes herramientas y librerías:
- [Colorama](https://pypi.org/project/colorama/)
- [hcitool](https://www.nongnu.org/bluez/)
- [l2ping en Linux man pages](https://man7.org/linux/man-pages/man1/l2ping.1.html)
```

---

Este es un único bloque de código en Markdown con toda la información estructurada. Puedes copiarlo directamente en tu archivo `README.md`. ¡Espero que te sirva! 😄
