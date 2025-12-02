# Image Scaler to 600 PPP(DPI)

A ready-to-use Windows `.exe` build is available — you can download and run the executable directly without cloning the repository or installing Python/dependencies.

This Python program lets the user select a folder containing images and automatically scales them to 600 DPI (ppp). Processed images are saved in a subfolder named `Scaled_600_dpi` inside the selected folder.

## Features
- Simple graphical interface using `Tkinter`.
- Supports multiple image formats: `.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`.
- Saves scaled images in a separate folder to keep the originals organized.

## Requirements
- Python 3.7 or newer (only required if you use the Python source).
- `Pillow` library.

## Installation (from source)
1. Clone this repository to your machine:
```bash
git clone https://github.com/usuario/nombre-del-repo.git
```
2. Install the required packages:
```bash
pip install pillow
```

> Note: `tkinter` is typically included with standard Python installers on Windows. If your Python installation lacks `tkinter`, install it using your distribution's package manager or the appropriate installer for your platform.

## Usage (source)
Run the script:
```bash
python scaled_to_600dpi.py
```

A window will appear allowing you to select a folder. All supported images in the selected folder will be scaled to 600 DPI and saved into the `Scaled_600_dpi` subfolder.

## Notes
- If no supported images are found in the selected folder, the program shows a message indicating there are no images to process.
- The program preserves the original image formats when saving the scaled copies.

## Using the `.exe` build
- If you prefer not to install Python or dependencies, download the Windows `.exe` build and run it directly. The executable performs the same image-scaling task and saves output to the `Scaled_600_dpi` folder.
- Download the latest `.exe` from the project's Releases page:

	https://github.com/cristianCarrerasCastillo/scale-img-to-600ppp/releases

	Or use the latest release direct link:

	https://github.com/cristianCarrerasCastillo/scale-img-to-600ppp/releases/latest


