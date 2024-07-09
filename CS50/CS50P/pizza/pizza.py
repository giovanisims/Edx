import sys
import csv
from tabulate import tabulate

def check_argv(file_type):
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(file_type):
        sys.exit("Not a Python file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("File does not exist")

check_argv(".csv")

with open(sys.argv[1], 'r') as file:
    reader = csv.reader(file)
    menu = list(reader)
    print(tabulate(menu, headers="firstrow", tablefmt='grid', showindex='Never'))
