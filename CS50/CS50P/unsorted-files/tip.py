
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    # Convert dollar amount string to float (removing the "$" with slicing)
    return float(d[1:])  # Make sure to return the converted value

def percent_to_float(p):
    # Convert percentage string to float (removing the "%" with slicing and dividing by 100)
    return float(p[:-1]) / 100  # Correct slicing to remove "%" and return the converted value

main()


