def main():
    name = get_name()
    find_house(name)

def get_name():
    return input("Enter your name: ")

def find_house(name):
    # if name == "Harry" or "Hermione" or "Ron":
    #     print("You belong in Gryffindor!")
    # elif name == "Draco":
    #     print("You belong in Slytherin!")
    # else:
    #     print("Who?")
    match name:
        case "Harry" | "Hermione" | "Ron":
            print("Gryffindor")
        case "Draco":
            print("Slytherin")
        case _ :
            print("Who?")

main()