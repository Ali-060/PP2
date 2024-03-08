# 1
import os
def list_files_and_directories(path):
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)
    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

# 2
import os
def check_path_access(path):
    print("Existence:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

# 3
import os
def analyze_path(path):
    if os.path.exists(path):
        print("Filename:", os.path.basename(path))
        print("Directory:", os.path.dirname(path))
    else:
        print("Path does not exist")

# 4
import os
def count_lines_in_file(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

# 5
import os
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

# 6
import os
def generate_text_files():
    for char in range(ord('A'), ord('Z')+1):
        filename = chr(char) + ".txt"
        with open(filename, 'w') as file:
            pass

# 7
import os
def copy_file(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())

# 8
import os
def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print("File deleted")
        else:
            print("Permission denied")
    else:
        print("File does not exist")