def main():
    rushed = input("What would you like to say? ")
    replace(rushed)

def replace(rushed):
    slowed = rushed.replace(" ","...")
    print(slowed)

main()