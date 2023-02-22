import os

# diretório com as imagens
img_dir = "img/"

# obter todos os nomes de arquivo na pasta img
img_files = [f for f in os.listdir(img_dir) if os.path.isfile(os.path.join(img_dir, f))]

# gerar o código HTML com as imagens
html = '<div class="gallery">'
for file_name in img_files:
    html += f'<img src="{img_dir}{file_name}" alt="{file_name}">'
html += '</div>'

# salvar o código HTML em um arquivo
with open("atalho.txt", "w") as f:
    f.write(html)
