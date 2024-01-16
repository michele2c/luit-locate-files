import os

# get the current working directory
current_wd = os.getcwd()

# get list of all files in the current directory
for file in os.listdir(current_wd):
    if os.path.isfile(file): # valide if variable file is a regular file (not a directory)
       file_path = os.path.join(current_wd, file)
       file_dic = {
          'FileName': file,
          'Size': os.path.getsize(file_path) #os.path.getsize method returns the size of the file in bytes
          }
       print(file_dic)