import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if hours_messy := re.search(r"(\d+)(?::(\d{2}))? (am|pm) to (\d+)(?::(\d{2}))? (am|pm)", s, re.IGNORECASE):
        first_hour = hours_messy.group(1)
        first_minutes = hours_messy.group(2) or "00"
        first_ampm = hours_messy.group(3).lower()
        second_hour = hours_messy.group(4)
        second_minutes = hours_messy.group(5) or "00"
        second_ampm = hours_messy.group(6).lower()

        if first_ampm == "am" and first_hour == "12":
            first_hour = "00"
        elif first_ampm == "pm" and first_hour != "12":
            first_hour = str(int(first_hour) + 12)

        if second_ampm == "am" and second_hour == "12":
            second_hour = "00"
        elif second_ampm == "pm" and second_hour != "12":
            second_hour = str(int(second_hour) + 12)

        if int(first_minutes) >= 60 or int(second_minutes) >= 60:
            raise ValueError

        return f"{first_hour.zfill(2)}:{first_minutes.zfill(2)} to {second_hour.zfill(2)}:{second_minutes.zfill(2)}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()