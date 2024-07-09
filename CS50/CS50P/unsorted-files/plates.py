# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable …
#  vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0].isnumeric() or s[1].isnumeric():
        return False
    if not s.isalnum():
        return False
    if '0' in s[2:]:
        return False
    num_started = False
    for char in s[2:]:
        if char.isnumeric():
            num_started = True
        elif num_started:
            return False
    return True

if __name__ == "__main__":
    main()