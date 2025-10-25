import os
import shutil

def move_and_arrange(desk_path, inp1, inp2):
    dst_path = os.path.join(desk_path, inp1)
    src_dst = os.chdir(desk_path)
    lst = os.listdir()

#Going through files:
  for file in lst:
        if file.endswith(inp2):
            file_path = os.path.join(desk_path, file)
            if not os.path.exists(os.path.join(dst_path, file)):
                print(f"Moving {file} to {dst_path}")
                shutil.move(file_path, dst_path)
            else:
                print(f"File {file} already exists in {dst_path}")
