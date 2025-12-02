# Escalador de Imágenes a 600 ppp

Este programa en Python permite al usuario seleccionar una carpeta que contenga imágenes y escalarlas automáticamente a 600 ppp. Las imágenes procesadas se guardan en una subcarpeta llamada `scaled_600_dpi` dentro de la carpeta seleccionada.

## Características
- Interfaz gráfica sencilla utilizando `Tkinter`.
- Compatible con múltiples formatos de imagen: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`.
- Guarda las imágenes escaladas en una carpeta separada para mantener el orden.

## Requisitos
- Python 3.7 o superior.
- Librería `Pillow`.

## Instalación
1. Clona este repositorio en tu máquina:
   ```bash
   git clone https://github.com/usuario/nombre-del-repo.git
2. Instala las dependencias necesarias:
   ```bash
   pip install pillow
   pip install tkinter
   
## Uso
Ejecuta el programa:
  ```bash
  python scale_images.py
  ```

Aparecerá una ventana que te permitirá seleccionar una carpeta.
Todas las imágenes compatibles en la carpeta seleccionada se escalarán a 600 ppp y se guardarán en la subcarpeta scaled_600_dpi.

## Notas
Si no se encuentran imágenes compatibles en la carpeta seleccionada, el programa mostrará un mensaje indicando que no hay imágenes para procesar.
El programa preserva el formato original de las imágenes.
