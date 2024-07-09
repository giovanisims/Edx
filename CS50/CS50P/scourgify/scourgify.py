import sys
import csv

def check_argv(file_type):
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 4:
            sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(file_type):
        sys.exit("Not a Python file")
    try:
        open(sys.argv[1])
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

check_argv(".csv")

rows = []
with open(sys.argv[1]) as before:
    reader = csv.reader(before)
    next(reader)
    for row in reader:
        house = row[1]
        names = row[0].split(", ")
        first_name = names[-1] # No clue why this works but names[1] doesn't
        last_name = names[0]
        rows.append((first_name, last_name, house))

with open(sys.argv[2], "w", newline="") as after:
    writer = csv.DictWriter(after, fieldnames=["first","last","house"])
    writer.writeheader()
    for row in rows:
        first_name = row[0]
        last_name = row[1]
        house = row[2]
        writer.writerow({"first": first_name, "last": last_name, "house": house})
