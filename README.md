# EL5610-GPO4
Repositorio del Grupo 4 para el Curso EL5610: Taller Integrador.

Implementando un dispositivo de transmisión GPS como lo es el "LILYGO T-Beam V1.2 Meshtastic ESP32 LoRa WiFi BLE GPS" se realiza el proyecto de conexión para transmisión en tiempo real de datos de geolocalización.

Este dispositivo requiere del uso de un firmware específico de conexión con el dispositivo.
Se integra mediante el uso de un editor de código como lo es VSCode, mediante la extensión PlatformIO que ayuda a la conexión de los dispositivos, en este caso, el dispositivo de transmisión. 

# Forma de conexión al Dispositivo

1. Ambiente de edición y variables.

Dentro del ambiente de codificación, de las configuraciones relevante, se detallan:

![image](https://github.com/user-attachments/assets/146e6aa0-6f53-45ad-9c53-d670948f87f9)

* Bloque "Beacon":
  * Callsign: Codificación del nombre del dispositivo.
El valor del callsign de divide en 2 partes:
    * Primeros 6 valores: Identificador del nombre. El sistema nacional de identificación usa las letras "TI" como indicativo para Costa Rica. Posterior, las letras solo identifican el sistema a uso. Opcional, el tercer valor, según el identificativo, representa una provincia, como lo puede ser el valor 3 para Cartago.
    * Valor final: Después del identificador, se adiciona un número que es el identificador de red (SSID), el cual determina si el dispositivo es un portal (0) o un transmisor (7).
  * Symbol: Simbolo que identifica al dispositivo en el sistema de visualización.
  * Comment: Información que se transmite como acompañamiento al identificador del sistema.
  * SmartBeacon: Configuraciones del tiempo, potencia y frecuencia de envios de la señal.

* Bloque "Display":
  * showSymbol: Visualización del simbolo que acompaña el dispositivo.

* Bloque "Notificación":
  * ledTx: enciende un led que responde como encendido cuando se realiza la transmisión de datos a APRS.

* Bloque "lora":
  * frequency: frecuencia de transmisión, ajustada a 433.775 MHz debido a la frecuencia de transmisión definida por legislación nacional.
  * power: potencia de la señal.

2. Proceso de conexión.

3. 
