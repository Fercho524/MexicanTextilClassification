from PIL import Image
from sys import argv
import os


def square_resize_image_dir(dir, size):
    """"
    Este programa preprocesa los datos redimensionando una carpeta llena de imágenes
    a un tamaño de 200x200.
    """

    size = int(size)

    # Redimensionando todas las imágenes
    if os.path.exists(dir):
        files = os.listdir(dir)
        os.chdir(dir)
    else:
        print("No existe el directorio")
        exit(1)

    for file in files:
        try:
            [image_name, extension] = os.path.splitext(file)
            image = Image.open(file)
            resized = image.resize((size, size))
            resized.save(f"resized_{size}_{image_name}.{extension}")
            print(f"Rezised -> resized_{size}_{image_name}.{extension}")
        except:
            print("Ocurrió un error")

if __name__ == "__main__":
    # Redimensionar las imágenes en imágenes cuadradas de nxn
    size = argv[2]
    dir = argv[1]
    square_resize_image_dir(dir, size)