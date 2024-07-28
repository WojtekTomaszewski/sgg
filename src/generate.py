from title import extract_title
from block import markdown_to_html_node

import os
import shutil

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} with template {template_path}")

  with open(from_path, "r") as file:
    content = file.read()

  with open(template_path, "r") as file:
    tmpl = file.read()

  title = extract_title(content)
  html_content = markdown_to_html_node(content).to_html()

  tmpl = tmpl.replace("{{ Title }}", title)
  tmpl = tmpl.replace("{{ Content }}", html_content)

  with open(dest_path, "w") as file:
    file.write(tmpl)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
  if not os.path.exists(dest_dir_path):
    os.mkdir(dest_dir_path)

  listdir = os.listdir(dir_path_content)
  if len(listdir) == 0:
    return
  
  for file in listdir:
    src = os.path.join(dir_path_content, file)

    if os.path.isfile(src) and file.split(".")[-1] == 'md':
      dst = os.path.join(dest_dir_path, "index.html")
      generate_page(src, template_path, dst)

    if os.path.isdir(src):
      dst = os.path.join(dest_dir_path, file)
      generate_page_recursive(src, template_path, dst)