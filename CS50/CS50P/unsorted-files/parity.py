def main():
    number = get_number()

    if is_even(number):
        print("Even")
    else:
        print("Odd")

def get_number():
    number = int(input("Enter number: "))
    return number 

def is_even(n):
    # if n % 2 == 0:
    #      return True
    # else:
    #      return False

    # return True if n % 2 == 0 else False

    # return bool(n % 2 == 0)

    return n % 2 == 0

main()