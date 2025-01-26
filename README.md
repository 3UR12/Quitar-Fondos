---

### Elimina el Fondo de una Imagen - Proyecto en Python

Este proyecto es una aplicación de escritorio creada en Python utilizando **Tkinter** para la interfaz gráfica, **Rembg** para la eliminación automática del fondo de las imágenes, y **PIL (Pillow)** para el manejo de imágenes. El objetivo de la aplicación es permitir a los usuarios eliminar el fondo de una imagen seleccionada y guardar el resultado de manera sencilla.

#### Funcionalidades principales:
- **Seleccionar Imagen**: El usuario puede seleccionar una imagen desde su sistema mediante un cuadro de diálogo.
- **Eliminar Fondo**: Al seleccionar una imagen, el sistema procesa la imagen eliminando el fondo automáticamente usando la librería **Rembg**.
- **Guardar Imagen**: La imagen procesada (sin fondo) puede ser guardada en el formato elegido por el usuario (PNG, JPG, BMP, etc.).
- **Interfaz simple y clara**: La aplicación tiene una interfaz minimalista donde se muestra el estado de la imagen, ya sea cargada correctamente o con algún error durante el proceso.

#### Características de la Interfaz:
- **Fondo oscuro** con bordes morados en los contenedores para una apariencia moderna.
- **Mensajes informativos** que indican el estado de la carga de la imagen y si el fondo se eliminó correctamente.
- **Botones de acción** con fondo negro para una experiencia de usuario limpia y sencilla.

#### Archivos:
- **`main.py`**: Contiene la estructura básica de la interfaz gráfica y la funcionalidad de la aplicación.
- **`main2.py`**: Es una versión alternativa con la interfaz en color negro, diseñada para ofrecer una apariencia oscura.

#### Requisitos:
- Python 3.x
- Librerías: `tkinter`, `rembg`, `Pillow`

#### Instalación:
1. Clona el repositorio.
2. Instala las dependencias necesarias:
   ```bash
   pip install rembg pillow
   ```
3. Ejecuta el script para iniciar la aplicación.

#### Uso:
- **Selecciona una imagen** desde tu computadora.
- **Elimina el fondo** automáticamente con un solo clic.
- **Guarda la imagen** procesada en el formato que prefieras.

Este proyecto es una herramienta útil para diseñadores, creadores de contenido, y cualquier persona que necesite eliminar fondos de imágenes de manera rápida y fácil.

---
