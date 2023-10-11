import os

# Specify the directory path you want to list
directory_path = "/master/location"

# List files and directories in the specified path
contents = os.listdir(directory_path)

# Print the list of contents
for item in contents:
    print(item)
