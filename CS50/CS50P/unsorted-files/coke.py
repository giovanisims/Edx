def main():
    coke = 50
    buy_coke(coke)

def buy_coke(coke):
    while coke > 0:
        print(f"Amount Due: {coke}")
        cents = int(input("Insert Coin: "))
        match cents:
            case 25 | 10 | 5:
                coke = coke - cents
            case _:
                continue
    if coke < 0:
        coke = coke * -1
        print(f"Change Owed: {coke}")
    else:
        print(f"Change Owed: {coke}")

main()