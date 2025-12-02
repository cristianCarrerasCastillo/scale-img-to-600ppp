import os
from tkinter import Tk, filedialog, messagebox
from PIL import Image
import sys

def scale_images_to_600_dpi(folder_path, parent=None):
    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]

    if not images:
        messagebox.showinfo("No images", f"No images were found in the selected folder ({folder_path}).", parent=parent)
        return
    
    output_folder = os.path.join(folder_path, "Scaled_600_dpi")
    os.makedirs(output_folder, exist_ok=True)

    for image_file in images:
        try:
            image_path = os.path.join(folder_path, image_file)
            with Image.open(image_path) as img:
                print(f"Scaling {image_file}")
                img.info['dpi'] = (600,600)
                output_path = os.path.join(output_folder,image_file)
                img.save(output_path, dpi=(600,600))
        except Exception as e:
            print(f"Error in {image_file}: {e}")

    messagebox.showinfo("Task Completed", f" The images have been scaled to 600 ppp (dpi) and saved in {output_folder}", parent=parent)

def select_folder(parent):
    folder_path = filedialog.askdirectory(title="Select the FOLDER with image", parent=parent)
    if folder_path:
        scale_images_to_600_dpi(folder_path, parent=parent)

def main():
    root= Tk()
    root.withdraw()
    select_folder(root)

    # Destroy the hidden root window so the program can exit normally
    root.destroy()

if __name__ == "__main__":
    main()
    sys.exit()