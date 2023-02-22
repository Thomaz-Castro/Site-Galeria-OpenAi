import os

dir_path = r"C:\Users\nacas\OneDrive\Documentos\Projetosss\Site-Galeria-OpenAi\img"

# listar todos os arquivos na pasta
files = os.listdir(dir_path)

# iterar sobre cada arquivo e renomear
for i, file_name in enumerate(files):
    # obter o nome do arquivo e sua extensão
    name, ext = os.path.splitext(file_name)
    # renomear o arquivo adicionando um número sequencial no final do nome
    new_name = f"imagem_{i+1}{ext}"
    os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, new_name))
    print(f"Arquivo renomeado: {file_name} -> {new_name}")