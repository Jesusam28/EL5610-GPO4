# Proyecto LoRa Tracker GPS

## Descripción General

Este proyecto implementa un dispositivo de transmisión GPS basado en el modelo **LILYGO T-Beam V1.2 Meshtastic ESP32 LoRa WiFi BLE GPS**, diseñado para transmitir datos de geolocalización en tiempo real mediante la red **APRS**. La principal aplicación del sistema es calcular los tiempos estimados de llegada de autobuses en paradas estratégicas dentro del campus del Tecnológico de Costa Rica.

La programación y configuración del dispositivo se realiza utilizando **VSCode** y la extensión **PlatformIO**, facilitando la integración del firmware y la personalización de los parámetros operativos.

---

## Arquitectura del Sistema

El sistema se organiza en varios niveles que describen su flujo de funcionamiento y detalle técnico. A continuación, se presentan los diagramas correspondientes:

### Diagrama de Primer Nivel
**Enfoque:** Arquitectura general del sistema.

- **Entradas:**
  - Señal GPS.
  - Información del usuario.
- **Procesos:**
  - Captura de datos GPS.
  - Generación de paquetes APRS.
  - Transmisión mediante LoRa.
  - Conexión a la red APRS.
- **Salidas:**
  - Datos enviados a la red.
  - Confirmación de transmisión.

![image](https://github.com/user-attachments/assets/0abbbc40-e8aa-4889-af88-0df99b9d3afa)


---

### Diagrama de Segundo Nivel
**Enfoque:** Detalle de los procesos clave.

1. **Datos GPS:**
   - Receptor GPS y lectura de coordenadas.
2. **Paquetes APRS:**
   - Estructuración de paquetes (AX.25).
   - Codificación de información.
3. **Transmisión:**
   - Configuración del módulo LoRa.
   - Envío de paquetes al sistema APRS.

![image](https://github.com/user-attachments/assets/d880f3f1-cdef-44e1-9871-d7966d750233)


---

### Diagrama de Tercer Nivel
**Enfoque:** Pasos específicos de cada función.

1. **Captura de Datos GPS:**
   - Encendido del receptor.
   - Extracción e interpretación de coordenadas.
2. **Procesamiento de Datos:**
   - Generación de paquetes con identificadores de usuario.
   - Codificación en protocolo AX.25.
3. **Transmisión LoRa:**
   - Configuración del módulo (frecuencia, potencia, otros).
   - Envío de datos a la antena.
   

![image](https://github.com/user-attachments/assets/1bf43faf-a386-40d3-a10c-e0b7a14b0e1a)

---

### Diagrama de Cuarto Nivel

#### Descripción General
El diagrama de cuarto nivel detalla el flujo de datos y la interacción entre los módulos principales del sistema. Este nivel muestra cómo se procesan, encapsulan y transmiten los datos desde el origen hasta el servidor central.

#### Componentes Principales
1. **Receptor GPS**:
   - Obtiene las coordenadas geográficas del bus.
   - Envía los datos al módulo de procesado para su verificación.

2. **Procesado de Datos**:
   - Verifica la validez de los datos recibidos.
   - Prepara la información para ser encapsulada en un paquete.

3. **Codex AX.25**:
   - Encapsula los datos en un formato compatible con la red APRS.
   - Garantiza que los datos sean transmitidos de forma eficiente.

4. **Módulo LoRa**:
   - Transmite los datos encapsulados utilizando tecnología LoRa.
   - Permite la comunicación a larga distancia con bajo consumo de energía.

5. **Gateway LoRaWAN**:
   - Recibe la señal LoRa y la convierte en paquetes IP.
   - Transmite los datos al servidor Watson para su procesamiento final.

6. **Watson Server**:
   - Procesa y almacena los datos provenientes del Gateway LoRaWAN.
   - Prepara los datos para su presentación en las pantallas de las paradas.

#### Flujo Principal
1. El **Receptor GPS** obtiene las coordenadas y las envía al módulo de **Procesado de Datos**.
2. Los datos procesados son encapsulados por el **Codex AX.25**.
3. El paquete es transmitido por el **Módulo LoRa** hacia el **Gateway LoRaWAN**.
4. Finalmente, el **Watson Server** almacena y procesa los datos para su visualización.

![image](https://github.com/user-attachments/assets/8472c646-11cc-48ee-a00d-bdb1abfe22f0)



---

### Diagrama de Quinto Nivel

#### Descripción General
El diagrama de quinto nivel profundiza en los detalles técnicos del sistema, incluyendo hardware, firmware, y sistemas embebidos. Este nivel muestra cómo se implementan los componentes descritos en el nivel anterior.

#### Componentes Técnicos
1. **Firmware del Receptor GPS**:
   - Responsable de manejar la adquisición y transmisión de datos geográficos.

2. **Microcontrolador en el Procesado de Datos**:
   - Ejecuta algoritmos de verificación y procesamiento.
   - Se asegura de que los datos estén listos para la transmisión.

3. **Codex AX.25 (Implementación en Software)**:
   - Encapsula los datos de manera eficiente para garantizar compatibilidad con el estándar AX.25.

4. **Hardware LoRa (Módulo y Antena)**:
   - Diseñado para transmitir datos con bajo consumo energético y alta cobertura.

5. **Servidor Watson**:
   - Ejecuta tareas avanzadas de análisis y almacenamiento de datos.
   - Ofrece una API para la comunicación con las pantallas de las paradas.

6. **Pantallas en las Paradas**:
   - Proveen una interfaz de usuario clara y accesible.
   - Muestran la información procesada en tiempo real.

#### Detalles Adicionales
- **Enlace entre el Firmware y el Hardware**:
  Cada módulo cuenta con firmware específico para su función (por ejemplo, el microcontrolador del procesador de datos).
- **Sistema Embebido en el Gateway LoRaWAN**:
  Convierte señales LoRa a paquetes IP para transmisión al servidor Watson.

![image](https://github.com/user-attachments/assets/96350d63-de5e-4e74-bc3f-e5972855cade)

## Diagrama de Flujo

El diagrama de flujo detalla el funcionamiento lógico del sistema, cubriendo las principales etapas desde el encendido hasta la transmisión de datos. A continuación, se describen los pasos y decisiones clave:

## Etapas del Diagrama

### 1. **Encendido del Dispositivo**
   - El sistema comienza su operación cuando se enciende el dispositivo.
   - Este paso inicial asegura que todos los componentes estén listos para entrar en funcionamiento.

### 2. **¿Dispositivo Correcto?**
   - **Decisión clave:** Se verifica si el dispositivo es el correcto para operar.
   - Si **no** es el dispositivo adecuado, el sistema detiene el proceso y emite una **notificación de error**.
   - Si **sí** es el dispositivo correcto, el proceso avanza hacia el **procesamiento del firmware**.

### 3. **Procesamiento del Firmware**
   - En esta etapa, el firmware del sistema es procesado para garantizar que se cumplan las configuraciones y requisitos de funcionamiento.

### 4. **¿Sistemas Correctos?**
   - **Decisión clave:** Se validan los sistemas internos del dispositivo para asegurar que funcionan correctamente.
   - Si los sistemas **no** son correctos, el proceso se redirige a la etapa de **notificación de error**.
   - Si los sistemas **sí** son correctos, el flujo continúa hacia la integración de periféricos y sensores.

### 5. **Integración de Sensores y Periféricos**
   - En esta etapa, el dispositivo conecta e integra sensores y periféricos necesarios para su operación.

### 6. **Receptor GPS**
   - Una vez que los sensores y periféricos están integrados, el sistema utiliza el receptor GPS para recibir información de localización y datos asociados.

### 7. **Transmisión de Datos**
   - Finalmente, el sistema transmite la información procesada al dispositivo correspondiente para que sea utilizada según el caso de uso del proyecto.

## Flujo de Errores
- El sistema está diseñado para detectar errores en dos puntos principales:
  1. Durante la validación del dispositivo.
  2. Durante la verificación de los sistemas internos.
- En ambos casos, si ocurre un error, se genera una **notificación** que interrumpe el flujo normal del proceso.

![image](https://github.com/user-attachments/assets/cdf64d26-ec60-4b42-b66f-888b021056f3)


---

## Notas Finales
Los diagramas buscan detallar cómo el sistema logra cumplir con su objetivo principal: la obtención y presentación de tiempos de llegada de buses. El enfoque modular asegura que cada componente funcione de manera independiente pero coordinada, facilitando la escalabilidad y el mantenimiento del sistema.

---

## Aplicación: Cálculo de Tiempos de Autobuses

El principal objetivo del sistema es estimar los tiempos de llegada de autobuses a paradas específicas dentro del campus. Utilizando coordenadas GPS del dispositivo instalado en los autobuses, se calcula el tiempo necesario para que el vehículo llegue a una parada, tomando en cuenta la velocidad promedio.

### Paradas Estratégicas
Se seleccionaron las siguientes ubicaciones dentro del campus como puntos de interés:

- **Parada Principal del TEC**
- **Parada Biblioteca JFF**
- **Parada D3**
- **Parada Bloque F**
- **Parada Electrónica**
- **Parada Comedor del Este**

### Funcionamiento del Sistema
1. El dispositivo captura y transmite las coordenadas GPS del autobús en tiempo real.
2. Estas coordenadas son procesadas para determinar la distancia a las paradas definidas.
3. El sistema calcula el tiempo estimado de llegada y lo presenta en un formato accesible para los usuarios.

> **Nota:** Este documentación se complementa con otro archivos de documentación que detalla los algoritmos de cálculo y las pruebas realizadas.

---

## Bill of Materials (BOM)

El **Bill of Materials (BOM)** incluye todos los componentes y materiales necesarios para la implementación del sistema, así como una estimación detallada de los costos operativos. 

---

### Componentes Físicos

La siguiente tabla detalla los elementos físicos necesarios para el sistema, junto con sus características y costos estimados.

![image](https://github.com/user-attachments/assets/7d8a5746-fc4a-4501-a1a2-21d93848b2ab)


---

## Costos Operativos

Además de los componentes físicos, se deben considerar los costos recurrentes asociados con la operación y el mantenimiento del sistema.

### Personal de Mantenimiento y Operación
- **Salario Mensual**: $2000.
- Un empleado capacitado es suficiente para operar y mantener el sistema de manera eficiente.

### Servicio de Servidor Watson
- **Costo Mensual**: $100.
- Contratado para el almacenamiento, análisis y presentación de datos.

---

## Costos para Cada Unidad de Operación

A continuación, se presenta un desglose de los costos asociados con cada unidad operativa implementada en las estaciones. Se considera que el sistema consta de múltiples estaciones.

| **Elemento**                     | **Costo Unitario (USD)** |
|----------------------------------|--------------------------|
| Sistema de registro GPS (Tracker) | 50.00                   |
| Precio por unidad operativa       | 173.00                  |

---

## Estimación Total para 6 Estaciones

Considerando un sistema con **6 estaciones**, el desglose de costos estimados es el siguiente:

| **Elemento**                       | **Costo Total (USD)** |
|------------------------------------|-----------------------|
| Subtotal por empleado (1 mes)      | 2100.00              |
| Estaciones (6 unidades)            | 1038.00              |
| **Total Estimado**                 | **3138.00**          |

---

## Resumen de Costos

El sistema requiere una inversión inicial para los componentes físicos, además de los costos recurrentes para su operación y mantenimiento. El siguiente es el resumen total estimado:

- **Costo inicial por componentes físicos**: $277.20 (para una unidad).
- **Costo operativo mensual**: $2100.00 (incluyendo salario y servicio de Watson).
- **Costo por 6 estaciones**: $1038.00.
- **Costo total estimado mensual**: $3138.00.

Este desglose permite entender claramente los recursos necesarios para implementar y operar el sistema de manera efectiva.


## Presupuesto de Horas Invertidas y Requeridas

Esta sección detalla las horas dedicadas a las distintas etapas del proyecto, considerando tanto las horas ya invertidas como las que se requerirían para concluir el desarrollo completo. El cálculo está basado en las actividades realizadas por un equipo de **tres miembros**, con las horas estimadas para **un estudiante individual** especificadas en la tabla.

---

## Presupuesto de Horas por Etapas del Proyecto

| **Etapa del Proyecto**         | **Horas por Estudiante** | **Horas Totales (x3 Miembros)**       |
|--------------------------------|--------------------------|---------------------------------------|
| **Investigación**              | 10                      | 30                                    |
| **Diseño**                     | 5                       | 15                                    |
| **Implementación**             | 5                       | 15                                    |
| **Periodo Testing**            | 40                      | 120                                   |
| **Implementación Real**        | 5 por prototipo         | 15 por prototipo                      |
| **Pruebas Tiempo Real**        | 40 por prototipo        | 120 por prototipo                     |
| **Finalización**               | 10                      | 30                                    |

---

## Detalles por Etapa

1. **Investigación (10 horas por estudiante)**  
   Investigación sobre las conexiones, alcance de los dispositivos y configuración del servidor.

2. **Diseño (5 horas por estudiante)**  
   Diseño de las implementaciones necesarias de hardware.

3. **Implementación (5 horas por estudiante)**  
   Ensamblaje del primer prototipo para pruebas iniciales.

4. **Periodo Testing (40 horas por estudiante)**  
   Uso del primer prototipo como piloto para validar el diseño y funcionamiento.

5. **Implementación Real (5 horas por prototipo)**  
   Una vez confirmados los resultados positivos, se desarrollan e implementan las demás aplicaciones necesarias.

6. **Pruebas Tiempo Real (40 horas por prototipo)**  
   Uso práctico de los prototipos en condiciones reales para evaluar los resultados obtenidos.

7. **Finalización (10 horas por estudiante)**  
   Análisis de resultados finales y generación de reportes con los datos obtenidos durante la ejecución.

---

## Notas Importantes

- **Sin optimización del ensamblaje**: Las horas no incluyen ajustes para optimizar los procesos de ensamblaje.  
- **Estimación por estudiante**: Las horas están calculadas para un estudiante y multiplicadas por tres para reflejar el esfuerzo grupal.  
- **Variabilidad en prototipos**: Las horas correspondientes a la implementación real y pruebas de tiempo real dependen del número de prototipos desarrollados.  

---


## Conclusión

El **LoRa Tracker GPS** es una solución eficiente para la monitorización de transporte público en tiempo real. Su capacidad para calcular tiempos de llegada lo convierte en una herramienta valiosa para mejorar la experiencia de los usuarios y optimizar los servicios de transporte. Los diagramas de niveles detallados proporcionan una base sólida para futuras mejoras y expansiones del sistema.

