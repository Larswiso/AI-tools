# This program allows you to rename all the files in the specified folder.

import os

file_format = ".png"
name = "dfgfdg"
start_index = 169


path = r'myPath' # e.g. 'C:\dev\YOLOv5\data'
files = os.listdir(path)

for index, file in enumerate(files):
    filename =["img "+str(start_index+index), '.png']
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(filename)))

print("{} files have been renamed".format(len(files)))