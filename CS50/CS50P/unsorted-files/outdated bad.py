def main():
    month_names = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    date = get_date(month_names)

def get_date(month_names):
    input_date = input("Enter the date in month-day-year: ")
    if input_date[:1].isdigit():
        convert_date_MDY(input_date)
    else:
        convert_date_full_month(input_date, month_names)


def convert_date_full_month(date, month_names):
    date_list = date.split(" ")
    month = str(month_names.index(date_list[0]) + 1)
    year = date_list[2]
    day_with_colon = date_list[1]
    day = day_with_colon[:len(day_with_colon) - 1]
    print("-".join([year,month,day]))


def convert_date_MDY(date):
    date_list = date.split("/")
    year = date_list[2]
    month = date_list[1]
    day = date_list[0]
    print("-".join([year,month,day]))


main()