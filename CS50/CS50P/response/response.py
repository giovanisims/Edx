from validator_collection import  validators, errors

def main():
    print(validate(input("What's your email? ")))

def validate(e):
    try:
        validators.email(e)
        return "Valid"
    except errors.InvalidEmailError:
        return "Invalid"
    

if __name__ == "__main__":
    main()