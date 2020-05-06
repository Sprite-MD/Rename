# Renames files in directory so that anime names are moved to the front and translation groups, resolutions, and other
#   are pushed to the back

import os
import re

# Creates a regular expression that detects any square brackets or '(Batch)' at the beginning of folder name

prefix = re.compile(r'^(\[.*\]) (.*)')
batch = re.compile(r'^(\(Batch\)) (.*)')


path = 'I:\\Anime'                                                  # Path file for intended directory
pathList = os.listdir(path)                                         # Lists all folders in directory

os.getcwd()                                                         # Check to make sure user is in correct directory
os.chdir(path)                                                      # Change to the correct directory if necessary


# Reorders names so that anime name is in front, all other info in back

i = 0

for name in pathList:
    if prefix.match(pathList[i]) == None:                           # If the name of folder doesn't start with []:
        i += 1                                                      # Increase counter &
        continue                                                    # Move on to next item
    else:
        mo  = prefix.search(pathList[i]).group()                    # Puts entire folder name into variable
        mo1 = prefix.search(pathList[i]).group(1)                   # [] at beginning into variable
        mo2 = prefix.search(pathList[i]).group(2)                   # rest of name into variable
        i += 1

        os.rename(mo,mo2 + ' ' + mo1)                               # Rename the file, puts brackets at the very end



# Removes the '(Batch)' prefix on the folder names -- if you downloaded batches from Horriblesubs.info

for name in pathList:
    if batch.match(pathList[i]) == None:                           # If the name of folder doesn't start with (Batch):
        i += 1                                                      # Increase counter &
        continue                                                    # Move on to next item
    else:
        mo  = batch.search(pathList[i]).group()                    # Puts entire folder name into variable
        mo1 = batch.search(pathList[i]).group(1)                   # (Batch) at beginning into variable
        mo2 = batch.search(pathList[i]).group(2)                   # rest of name into variable
        i += 1

        os.rename(mo,mo2)                               # Rename the file, Deletes (Batch) from the folder name