import os

def locate_file(current_wd=None):
    if current_wd is None:
        current_wd = os.getcwd() # use current working directory if path is not provided

    file_list = [] # List to store dictionaries

    # os.walk through nested folders
    # underscore indicates that the loop variable is intentionally not being used in the loop body
    for folder, _, files in os.walk(current_wd):
        for file in files:
            file_path = os.path.join(folder, file)
            file_dic = {
                'FileName': file,
                'Size': os.path.getsize(file_path), #os.path.getsize method returns the size of the file in bytes
                'FilePath': file_path
                }
            file_list.append(file_dic)

    return file_list

# Example:
response = locate_file("/Users/michelecosta/Desktop/Folder-Test")
for file_dictionary in response:
    print(file_dictionary)