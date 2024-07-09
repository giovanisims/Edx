# :( input of 9/8/1636 outputs 1636-09-08
#     expected "1636-09-08", not "1636-8-9\n"
# :( input of September 8, 1636 outputs 1636-09-08
#     expected "1636-09-08", not "1636-9-8\n"
# :( input of 10/9/1701 outputs 1701-10-09
#     expected "1701-10-09", not "1701-9-10\n"
# :( input of October 9, 1701 outputs 1701-10-09
#     expected "1701-10-09", not "1701-10-9\n"
# :( input of " 9/8/1636 " outputs 1636-09-08
#     expected "1636-09-08", not "Traceback (mos..."
# :( input of 23/6/1912 results in reprompt
#     expected program to reject input, but it did not
# :( input of 10 December, 1815 results in reprompt
#     expected program to reject input, but it did not
# :( input of October/9/1701 results in reprompt
#     expected program to reject input, but it did not
# :( input of 1/50/2000 results in reprompt
#     expected program to reject input, but it did not
# :( input of December 80, 1980 results in reprompt
#     expected program to reject input, but it did not
# :( input of September 8 1636 results in reprompt
#     expected program to reject input, but it did not

def main():
    date = get_date()

def get_date():
    date = input("Date: ").strip()
    if date[0].isnumeric() and (date[2].isnumeric() or date[3].isnumeric()):
        american_date(date)
    elif date[0].isalpha() and date[1].isalpha():
        english_date(date)
    else:
        get_date()

def american_date(date):
    month, day, year = date.split("/")
    if int(month) > 12 or int(day) > 31:
        get_date()
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    print(f"{year}-{month}-{day}")

def english_date(date):
    month_dict = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
    }
    try:
        month, day, year = date.split()
    except ValueError:
        get_date()
    if day.isnumeric():
        get_date()
    if len(day) == 2:
        day = "0" + day
    if int(day[:2]) >31:
        get_date()
    print(f"{year}-{month_dict[month]}-{day[:2]}")



main()