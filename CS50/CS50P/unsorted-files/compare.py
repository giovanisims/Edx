def main():
    x = int(input("What's x? "))
    y = int(input("What's y? "))
    compare(x, y)

# def compare(x, y):
#     if x > y:
#         print("x is greater than y")
#     elif x == y:
#         print("x is equal to y")
#     else:
#         print("x is less than y")

# def compare(x, y):
#     if x > y or x < y:
#         print("x is not equal to y")
#     else:
#         print("x is equal to y")
    
# def compare(x, y):
#     if x != y :
#         print("x is not equal to y")
#     else:
#         print("x is equal to y")
    
def compare(x, y):
    if x == y:
        print("x is equal to y")
    else:
        print("x is not equal to y")
        
main()
