def main():
    greeting = input("Enter your greeting: ").strip().lower()
    money = value(greeting)
    print(f"${money}")


def value(g):
    if g.startswith("hello"):
        return 0
    elif g[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
