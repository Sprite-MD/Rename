# Intended for Chinese/Korean novels downloaded through Qidian
# Renames the files by removing '_' into ''

import os

path = 'K:\\Books\\Chinese Novels'                                  # Path file for intended directory
pathList = os.listdir(path)                                         # Lists all folders in directory

os.getcwd()                                                         # Check to make sure user is in correct directory
os.chdir(path)                                                      # Change to the correct directory if necessary

for names in pathList:                                  # Replaces all '_" with spaces to look neater
    os.rename(names, names.replace("_"," "))

for names in pathList:                                  # Replaces 'Fin' in all upper and in parenthesises
    os.rename(names, names.replace('Fin', '(FIN)'))


