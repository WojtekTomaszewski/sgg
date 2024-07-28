import os
import os.path
import shutil

def copy_static(src_path, dst_path):
  if not os.path.exists(dst_path):
    os.mkdir(dst_path)

  
  listdir = os.listdir(src_path)
  if len(listdir) == 0:
    return
  
  for entry in listdir:
    src = os.path.join(src_path, entry)
    dst = os.path.join(dst_path, entry)

    if os.path.isfile(src):
      print(f"Copy file {src}")
      shutil.copy(src, dst)

    if os.path.isdir(src):
      # os.mkdir(dst)
      copy_static(src, dst)

if __name__ == "__main__":
  copy_static("static", "public")


