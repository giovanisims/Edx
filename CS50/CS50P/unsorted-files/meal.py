def main():
    time = get_time()
    convert(time)

def get_time():
    time = input("Enter time: ")
    split_time = time.split(":")
    return split_time


def convert(t):
    hours = int(t[0])
    minutes = int(t[1])
    time_in_float = hours + minutes / 60.0
    if time_in_float >= 7 and time_in_float < 8:
        print("breakfast time")
    elif time_in_float >= 12 and time_in_float < 13:
        print("lunch time")
    elif time_in_float >= 18 and time_in_float < 19:
        print("dinner time")






if __name__ == "__main__":
    main()