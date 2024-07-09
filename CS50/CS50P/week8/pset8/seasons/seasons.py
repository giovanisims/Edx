from datetime import date
import re
import sys
import inflect

p = inflect.engine()

def main():
    print(check_date(get_date(input("Date of birth: "))))

def get_date(d):
    if bdate := re.search(r"((\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01]))$", d):
        return [int(i) for i in bdate.groups()[1:]]
    else:
        sys.exit("Invalid date")

def check_date(bd):
    birth_date = date(*bd)
    today = date.today()
    age_days = (today - birth_date).days
    age_minutes = (age_days * 24 * 60)
    return f"{p.number_to_words(age_minutes, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()