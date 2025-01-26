import tkinter as tk
from tkinter import filedialog, messagebox
from rembg import remove
from PIL import Image
import io

def seleccionar_imagen():
    """
    Permite al usuario seleccionar una imagen desde su computadora.
    """
    ruta = filedialog.askopenfilename(
        title="Seleccionar Imagen",
        filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if ruta:
        entrada_var.set(ruta)
        try:
            # Intentar abrir la imagen seleccionada
            imagen = Image.open(ruta)
            # Solo mostrar el mensaje sin mostrar la imagen
            entrada_label.config(text="Imagen cargada correctamente", fg="green")
            # Mostrar el gancho verde ✅ cuando la imagen se carga correctamente
            estado_label.config(text="✅ Imagen cargada correctamente.", fg="green")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo abrir la imagen: {e}")
            # Mostrar la X roja ❌ en caso de error
            estado_label.config(text="❌ Error al cargar la imagen.", fg="red")

def quitar_fondo_y_guardar():
    """
    Elimina el fondo de la imagen seleccionada y permite guardar el resultado.
    """
    ruta_entrada = entrada_var.get()
    if not ruta_entrada:
        messagebox.showerror("Error", "Por favor, selecciona una imagen primero.")
        return

    try:
        # Leer y procesar la imagen
        with open(ruta_entrada, 'rb') as file:
            imagen = file.read()
        resultado = remove(imagen)

        # No se muestra la imagen sin fondo en la interfaz, solo el mensaje
        salida_label.config(text="Fondo eliminado correctamente", fg="green")

        # Guardar la imagen sin fondo
        ruta_guardado = filedialog.asksaveasfilename(
            title="Guardar Imagen",
            defaultextension=".png",
            filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg"), ("BMP", "*.bmp"), ("TIFF", "*.tiff")]
        )
        if ruta_guardado:
            # Mejorar la calidad antes de guardar
            imagen_sin_fondo = Image.open(io.BytesIO(resultado))
            imagen_sin_fondo.save(ruta_guardado, quality=95)
            messagebox.showinfo("Éxito", f"Imagen guardada en: {ruta_guardado}")
            # Mostrar el gancho verde ✅ al guardar correctamente
            estado_label.config(text="✅ Imagen procesada y guardada con éxito.", fg="green")
    except Exception as e:
        messagebox.showerror("Error", f"Hubo un problema: {e}")
        # Mostrar la X roja ❌ en caso de error
        estado_label.config(text="❌ Error al procesar la imagen.", fg="red")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Quitar Fondo de Imagen")
ventana.geometry("700x500")
ventana.configure(bg="#f5f5f5")

# Variables
entrada_var = tk.StringVar()

# Títulos y botones
titulo = tk.Label(ventana, text="Elimina el Fondo de una Imagen", font=("Arial", 18), bg="#f5f5f5")
titulo.pack(pady=10)

frame_entrada = tk.Frame(ventana, bg="#f5f5f5")
frame_entrada.pack(pady=5)

btn_seleccionar = tk.Button(frame_entrada, text="Seleccionar Imagen", command=seleccionar_imagen)
btn_seleccionar.grid(row=0, column=0, padx=10)

entrada_label = tk.Label(frame_entrada, text="No se ha cargado ninguna imagen", bg="#f5f5f5", width=30)
entrada_label.grid(row=0, column=1, padx=10)

frame_botones = tk.Frame(ventana, bg="#f5f5f5")
frame_botones.pack(pady=10)

btn_procesar = tk.Button(frame_botones, text="Quitar Fondo y Guardar", command=quitar_fondo_y_guardar, bg="#4caf50", fg="white")
btn_procesar.pack(pady=10)

# Labels solo para mostrar mensajes
frame_imagenes = tk.Frame(ventana, bg="#f5f5f5")
frame_imagenes.pack(pady=10)

entrada_label = tk.Label(frame_imagenes, bg="#d9d9d9", width=40, height=2, text="Imagen Original")
entrada_label.grid(row=0, column=0, padx=10)

salida_label = tk.Label(frame_imagenes, bg="#d9d9d9", width=40, height=2, text="Imagen sin Fondo")
salida_label.grid(row=0, column=1, padx=10)

# Label para mostrar el estado con gancho o X
estado_label = tk.Label(ventana, text="", font=("Arial", 12), bg="#f5f5f5")
estado_label.pack(pady=10)

# Iniciar ventana
ventana.mainloop()
