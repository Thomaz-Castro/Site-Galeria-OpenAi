from os.path import join
from os import listdir, remove

folder_path = "./img"

for file_name in listdir(folder_path):

    if file_name.endswith(".png"):
        # Define o caminho completo do arquivo
        png_file_path = join(folder_path, file_name)
        remove(png_file_path)

print('\nFinalizado')

