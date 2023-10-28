
import os

def get_all_file_paths(directory):
    file_paths = []  # A list to store the file paths

    # Walk through all directories and subdirectories using os.walk
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the root directory with the file name to get the complete file path
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)

    return file_paths

# Replace 'your_directory_path' with the path to the directory you want to search
directory_path = './ui'
file_paths = get_all_file_paths(directory_path)

for file_path in file_paths:
    print(file_path)





