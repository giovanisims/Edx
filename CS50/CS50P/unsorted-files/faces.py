def main():
    text = input("What would you like to say? ")
    convert(text)

def convert(text):
    converted_happy = text.replace(":)","🙂")
    converted_happy_sad = converted_happy.replace(":(","🙁")
    print(converted_happy_sad)


main()

