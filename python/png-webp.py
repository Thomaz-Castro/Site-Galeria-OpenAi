from os.path import join, splitext
from os import listdir
from PIL import Image

folder_path = "./img"

for file_name in listdir(folder_path):

    if file_name.endswith(".png"):
        # Define o caminho completo do arquivo
        png_file_path = join(folder_path, file_name)

        # Abre a imagem com o Pillow
        image = Image.open(png_file_path)

        # Define o nome e o caminho do novo arquivo WebP
        webp_file_path = splitext(png_file_path)[0] + ".webp"

        # Salva a imagem no formato WebP
        image.save(webp_file_path, "webp")

print('\nFinalizado')

