# Input - 
# 1) a single file
# 2) number of DOE runs
# 3) target parent directory
# Output - 
# 1) A folder Structure of DOE setup
# 2) Copy of input files in each DOE structure, renamed

import os
import shutil
import pathlib

inp_file = r'C:\Users\denni\OneDrive\python try\File_Management_Practice\model.txt'
dst_dir = r'C:\Users\denni\OneDrive\python try\target_folder'
doe_num = int(input())


for num in range(1, doe_num + 1):
    sub_dir = f'\\DOE_{num}'
    full_dir = dst_dir + sub_dir
    sub_file = f'_DOE_{num}'
    try:
        os.mkdir(full_dir)
    except FileExistsError:
        print(f'file {full_dir} already exists')
    shutil.copy(inp_file, full_dir)
    for file in os.listdir(full_dir):
        target_path = full_dir + "\\" + file
        new_file = target_path[:len(target_path) - 4] + sub_file + target_path[len(target_path) - 4:]
        data_file = pathlib.Path(target_path)
        try:
            data_file.rename(new_file)
        except FileExistsError:
            print(f'file {new_file} already exists')
