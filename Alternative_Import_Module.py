import os
import shutil

def move_and_arrange(desk_path, inp1, inp2):
    dst_path = os.path.join(desk_path, inp1)
    src_dst = os.chdir(desk_path)
    lst = os.listdir()
