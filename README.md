# L2FLOOD - Un exploit DoS escrito en Python para denegar la conexión a dispositivos Bluetooth

Funciona perfectamente con dispositivos con una CPU muy mala como la de un altavoz

Me he llegado a encontrar casos en los que el altavoz se ha reiniciado

Úsalo con respeto, no me hago responsable de cualquier mal uso a no ser que sean tus propios dispositivos los que vayan a ser afectados

## Requisitos

Hace falta `Colorama` que se puede instalar con `pip install colorama`



Ejecuta `sudo python3 l2.py` sin argumentos para iniciar el modo asistido, el que te irá preguntando la MAC del dispositivo víctima, o ejecútalo con el argumento `-m` para indicarle una MAC

Si quieres hacer un ataque a todos los dispositivos alrededor, utiliza `sudo python3 autoflood.py`
