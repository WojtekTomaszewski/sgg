def extract_title(content) -> str:
  first_line = content.split("\n")[0]

  if not first_line.startswith("# "):
    raise Exception("Content needs #/h1 header")
  
  return first_line.strip("# ")


if __name__ == "__main__":
  title = extract_title()
  print(title)