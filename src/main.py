from copystatic import copy_static
from generate import generate_page, generate_page_recursive

if __name__ == "__main__":
  copy_static("static", "public")
  generate_page_recursive("content", "template.html", "public")


