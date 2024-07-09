import sys
import csv
import os
import PIL
import PIL.Image

def check_argv():
    file_type_1 = os.path.splitext(sys.argv[1])[1]
    file_type_2 = os.path.splitext(sys.argv[2])[1]
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 4:
            sys.exit("Too many command-line arguments")
    if file_type_2 not in [".jpg", ".png",".jpeg"]:
        sys.exit("Invalid output")
    if file_type_1 != file_type_2:
        sys.exit("Input and output have different extensions")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

check_argv()


before = PIL.Image.open(sys.argv[1])
shirt = PIL.Image.open("cs50_shirt.png")

before_cropped = PIL.ImageOps.fit(before, size=(shirt.size))
before_cropped.paste(shirt, (0, 0), shirt)

after = before_cropped
after.save(sys.argv[2])
