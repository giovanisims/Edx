def main():
    time=input('What time is it? ')
    time=convert(time)
    if 7<=time<=8:
        print('breakfast time')
    elif 12<=time<=13:
        print('lunch time')
    elif 18<=time<=19:
        print('dinner time')  # Changed from 'breakfast time' to 'dinner time'

def convert(t):
    hours,minutes = t.split(':')
    t=float(hours)+(float(minutes)/60)
    return(t)

if __name__ == "__main__":
    main()
