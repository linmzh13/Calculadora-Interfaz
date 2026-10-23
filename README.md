# Calculadora con Tkinter

Este proyecto consiste en una aplicación de escritorio para una **calculadora funcional** desarrollada en **Python**, utilizando la biblioteca gráfica **Tkinter**. 

El objetivo principal fue crear una interfaz intuitiva y limpia que permita realizar operaciones matemáticas básicas, manejando la lógica de eventos y el control de errores común en este tipo de aplicaciones.

---

## Características Principales

* **Operaciones básicas:** Suma, resta, multiplicación, división y porcentaje.
* **Control de edición:** 
  * Botón **`C`**: Limpia la pantalla por completo.
  * Botón **`⌫`**: Elimina únicamente el último caracter ingresado.
* **Manejo de excepciones:** Captura errores comunes como la división por cero o sintaxis inválida, mostrando un mensaje claro en pantalla en lugar de detener la aplicación.
* **Diseño fijo:** Interfaz compacta con dimensiones fijas para evitar distorsiones visuales al redimensionar.

---

## Modelado UML

Para documentar la arquitectura y el flujo de la aplicación, el proyecto incluye tres diagramas UML:

1. **Diagrama de Casos de Uso:** Define los requerimientos funcionales y las interacciones principales entre el usuario y el sistema.
   
   <img width="352" height="354" alt="Captura de pantalla 2026-10-22 203649" src="https://github.com/user-attachments/assets/8f70ccf7-79e6-408b-a3ac-267aae7eaa00" />


2. **Diagrama de Clases:** Estructura de componentes y métodos que conforman la lógica de la ventana y los controles de Tkinter.
   
   <img width="311" height="363" alt="Captura de pantalla 2026-10-22 203749" src="https://github.com/user-attachments/assets/42636101-7263-40f0-88d5-2664468ef87d" />

3. **Diagrama de Secuencia:** Detalla el flujo de mensajes paso a paso desde que el usuario presiona el botón `=` hasta que se evalúa y muestra el resultado.
   
<img width="435" height="386" alt="Captura de pantalla 2026-10-22 205423" src="https://github.com/user-attachments/assets/08860765-ab02-4334-88b2-03e244dfbf89" />

## Ejecución del Proyecto

1. Asegúrate de tener instalado Python en tu equipo.
2. Clona o descarga este repositorio.
3. Abre una terminal en la carpeta del proyecto y ejecuta: calculadora.py
