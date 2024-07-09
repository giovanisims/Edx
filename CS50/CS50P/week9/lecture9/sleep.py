

def sheep(n):
    flock = []
    for i in range(n):
        yield "🐑" * i

def main():

    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

if __name__ == "__main__":
    main()