import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Names: ")
        names.append(name)
    except EOFError:
        break

names_str = p.join(names)
print(f"Adieu, adieu, to {names_str}")