def main():
    operation = get_operation()
    execute_operation(operation)

def get_operation():
    return input("Enter operation: ").strip()

def execute_operation(o):
    parts_o = o.split()
    if parts_o[1] == "+":
        print(float(parts_o[0]) + float(parts_o[2]))
    elif parts_o[1] == "-":
        print(float(parts_o[0]) - float(parts_o[2]))
    elif parts_o[1] == "*":
        print(float(parts_o[0]) * float(parts_o[2]))
    elif parts_o[1] == "/":
        print(float(parts_o[0]) / float(parts_o[2]))
    else:
        print("Invalid operation")

        
main()