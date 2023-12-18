import reflex as rx
from ..components.projects_menu import *

def menuProjects() -> rx.Component:
    return rx.vstack(
        rx.box(
            rx.text("Proyectos"),
            width="100%",
            font_size="1.5em",
            font_weight="bold",
            align_items="start",
        ),
        projectMenu(
            "IOT-USCO",
            "Plataforma de Desarrollo para Proyectos IoT: Módulo de Entrenamiento",
            "Explora el fascinante mundo del Internet de las cosas (IoT) a través del innovador Módulo de Entrenamiento. Este sistema integral, compuesto por un módulo físico (módulo-IoT) y un entorno virtual, está diseñado para fomentar la investigación y el aprendizaje en el desarrollo de proyectos IoT. El módulo-IoT incorpora una ESP32 WiFi y diversos sensores como DHT11 (Temperatura y Humedad), MQ135 (Calidad del Aire) y HC-SR04 (Ultrasonido), junto con una etapa de potencia para la conexión de actuadores de alta potencia.",
            "https://github.com/xmunder/IoT-Usco-Project",
            "https://drive.google.com/file/d/1mlF23dkRVumWdiayWZ8pxzhu-qmB-FIJ/view?usp=sharing",
            "USCO IOT PROJECT",
            2,
        ),
        projectMenu(
            "Conversor DC-DC 'Buck Converter'",
            "Referencia de Diseño de un Convertidor Buck DC-DC",
            "Sumérgete en el mundo de la eficiencia energética con la guía detallada sobre el diseño, implementación y control de un Convertidor Buck Asíncrono DC-DC. Donde se abordará los fundamentos del funcionamiento de un Buck Converter, destacando los materiales clave utilizados en la implementación y profundizando en el método de control empleado. Descubre cómo optimizar la gestión de energía con esta referencia de diseño paso a paso que aborda los aspectos esenciales de este componente crucial en sistemas electrónicos.",
            "https://drive.google.com/file/d/16yGnnstRwqyekB-gg0_EN5ROPei8SHt6/view?usp=sharing",
            "",
            "Diseño de un Buck Converter",
            1,
        ),
        projectMenu(
            "Diseño de controladores PID AH-KR",
            "Innovación en Control Automático: Diseño e Implementación de Controladores con Auto-Tuning",
            "Este proyecto detalla el diseño y la implementación de dos métodos de Auto-Tuning basados en relés: Åström-Hägglund y Kaiser-Rajka. Estos enfoques revolucionarios permiten la creación y ajuste de controladores sin la necesidad de conocer la dinámica precisa de la planta.",
            "https://drive.google.com/file/d/1inAgj18hQT2TenAvGqxq8SSo4OA7SmAR/view?usp=sharing",
            "",
            "Diseño de controladores AutoTunning",
            1,
        ),
        projectMenu(
            "Diseño sistema de monitoreo en tiempo real con LabVIEW",
            "Monitoreo en Tiempo Real: Sistema de Temperatura con Interfaz LabVIEW",
            "Sumérgete en la eficacia del monitoreo térmico con nuestro proyecto, donde implementamos un sistema de monitoreo en tiempo real de la temperatura entre dos puntos clave utilizando sensores DS18B20 y DHT11 programados en Arduino. La programación abarcó desde la configuración de los sensores hasta la transmisión de datos mediante un protocolo serial. Para una visualización clara, creamos una interfaz en LabVIEW que representa gráficamente las lecturas de temperatura, permitiendo un monitoreo intuitivo y en tiempo real.",
            "https://drive.google.com/file/d/18A53tz3AW2l8oq3h2RRh3HY_YfTrq1hm/view?usp=sharing",
            "",
            "Sistema de monitoreo en tiempo real",
            1,
        ),
        align_items="center",
        margin_bottom=Size.BIG.value + "!important",
        width="100%",
    )      
