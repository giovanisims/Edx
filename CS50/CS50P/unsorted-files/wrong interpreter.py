def main():
    x = get_x()
    y = get_y()
    z = get_z()
    operation(x, y, z)

def get_x():
    return int(input("Enter x: "))

def get_z():
    return int(input("Enter x: "))

def get_y():
    return input("Enter y: ")

def operation(x, y, z):
    match y:
        case "+":
            print(x + z)
        case "-":
            print(x - z)
        case "*":
            print(x * z)
        case "/":
            print(x / z)
        case _:
            print("Invalid operation")

main()