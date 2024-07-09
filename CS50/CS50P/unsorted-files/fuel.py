def main():
    fraction = input("Fraction: ")
    try:
        quotient = convert(fraction)
    except ValueError:
        main()
    print(gauge(quotient))


def convert(fraction):
    x, y = fraction.split("/")
    dividend = int(x)
    divisor = int(y)
    if divisor == 0:
        raise ZeroDivisionError
    if dividend > divisor:
        raise ValueError
    return (dividend / divisor) * 100

def gauge(q):
    if q <= 10:
        return "E"
    elif q >= 99:
        return "F"
    else:
        return str(f"{q:.0f}%")

    
if __name__ == "__main__":
    main()