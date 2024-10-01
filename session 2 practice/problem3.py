import os
# Write a python program to print the contents of a directory using the os module.
# Search online for the function which does that. 

def print_directory_contents(path='/'):
    try:
        # List the contents of the directory
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for accessing '{path}'.")

if __name__ == "__main__":
    # Change '.' to any directory path you want to inspect
    print_directory_contents('.')
 