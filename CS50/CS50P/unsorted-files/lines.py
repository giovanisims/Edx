import sys

def check_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

check_argv()

with open(sys.argv[1]) as file:
    line_amout = 0
    for line in file:
        if (line.strip()) and not (line.lstrip().startswith("#")):
            line_amout += 1

print(line_amout)
