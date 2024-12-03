import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image

def scale_images_to_600_dpi(folder_path):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]

    if not images:
        messagebox.showinfo("Sin imágenes", "No se encontraron imágenes en la carpeta seleccionada.")
        return
    
    output_folder = os.path.join(folder_path, "Scaled_600_dpi")
    os.makedirs(output_folder, exist_ok=True)

    for image_file in images:
        try:
            image_path = os.path.join(folder_path, image_file)
            with Image.open(image_path) as img:
                img.info['dpi'] = (600,600)
                output_folder = os.path.join(output_folder,image_file)
                img.save(output_folder, dpi=(600,600))
        except Exception as e:
            print(f"Error procesando {image_file}: {e}")

    messagebox.showinfo("Completado", f"Las imágenes han sido escaladas a 600 ppp y guardadas en:\n{output_folder}")

def select_folder():
    folder_path = filedialog.askdirectory(title="Seleccione la carpeta con imágenes")
    if folder_path:
        scale_images_to_600_dpi(folder_path)

def main():
    root= Tk()
    root.title("Escalar imágenes a 600 ppp")
    root.geometry("400x200")
    root.eval('tk::PlaceWindow . center')

    root.withdraw()
    select_folder()

    root.mainloop()

if __name__ == "__main__":
    main()