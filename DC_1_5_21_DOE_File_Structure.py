# Input - 
# 1) a single file
# 2) number of DOE runs
# 3) target parent directory - must be empty
# Output - 
# 1) A folder Structure of DOE setup
# 2) Copy of input files in each DOE structure, renamed

import os
import shutil
import pathlib

# inp_file = r'C:\Users\denni\OneDrive\python try\File_Management_Practice\model.txt'
# dst_dir = r'C:\Users\denni\OneDrive\python try\target_folder'
file_inp = input("What is full directory where the file to be copied is located\n", )
inp_file = rf"{file_inp}"
dir_dst = input("what is full destination directory\n", )
dst_dir = rf'{dir_dst}'

file_extension_len = 0
for i in range(-1, -len(inp_file) - 1, -1):
    if inp_file[i] == ".":
        file_extension_len = -i

doe_num = int(input("what is the total DOE run number\n", ))
p = pathlib.Path(inp_file)
orig_file_name = p.name

before_ext = orig_file_name[:len(orig_file_name) - file_extension_len]
file_ext = orig_file_name[len(orig_file_name) - file_extension_len:]

for num in range(1, doe_num + 1):
    sub_dir = f'\\DOE_{num}'
    full_dir = dst_dir + sub_dir
    sub_file = f'_DOE_{num}'
    new_file_name = before_ext + sub_file + file_ext
    
    target_path = full_dir + "\\" + orig_file_name  # path object later 
    new_path = target_path[:len(target_path) - file_extension_len] \
                + sub_file \
                + target_path[len(target_path) - file_extension_len:]
                # a string to make a Path object later
    
    try:
        os.mkdir(full_dir)
    except FileExistsError:
        print(f'file {full_dir} already exists')
    
    for dirpath, dirnames, files in os.walk(full_dir):  # returns a bunch of lists
        if not files: 
            shutil.copy(inp_file, full_dir)
            
            data_file = pathlib.Path(target_path)
            try:
                data_file.rename(new_path)
            except FileExistsError:
                print(f'file {new_file_name} already exists')
        
        else:
            print("Folder are not empty, files already created")
