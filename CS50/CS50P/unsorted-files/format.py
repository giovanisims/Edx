import re

name = input("What's your name? ").strip()

if matches := re.match(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
    print(f"Hello, {name}")