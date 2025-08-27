import os

# Specify the directory you want to list, or leave blank for current directory
directory = '/'  # Current directory

# list all files and directories in the specified path 
contents = os.listdir(directory)

print("Contents of the directory:")
for item in contents:
    print(item)
