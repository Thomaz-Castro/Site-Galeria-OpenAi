from os import listdir
from os.path import isfile, join

path = 'img'
files = list([f for f in listdir(path) if isfile(join(path, f))])

numImg = len(files)

for f in range(0, numImg):
    files[f] = files[f].replace("·", "-")


print("\n "+str(numImg))

print(files)
