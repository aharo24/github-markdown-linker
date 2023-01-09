
import os

import re

  

# Set the root of the workspace to the current working directory

workspace_root = os.getcwd()

  

# Initialize the counter that will be used to give the new names to the files

counter = 1

  

# Walk through all the files in the directory and its subdirectories

for dirName, subdirList, fileList in os.walk(rootDir):

for filename in fileList:

# If the file has the .png extension

if filename.endswith('.png'):

# Construct the new file name

new_name = 'aharo_{}.png'.format(counter)

# Increment the counter

counter += 1

# Construct the full path of the file

file_path = os.path.join(dirName, filename)

# Construct the full path of the new file name

new_file_path = os.path.join(dirName, new_name)

# Rename the file

os.rename(file_path, new_file_path)