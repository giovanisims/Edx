def main():
    score = get_score()
    grade(score)

def get_score():
    score = -1
    while score < 0 or score > 100:
        score = int(input("Enter score: "))
        if score < 0 or score > 100:
            print("Invalid score. Please try again.")
    return score

def grade(score):
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

main()