def main():
    answer = get_answer()
    check_answer(answer)

def get_answer():
    return input("Enter your answer: ").strip().lower()

def check_answer(a):
    match a:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

main()
