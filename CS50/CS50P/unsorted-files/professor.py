import random
import sys

def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    all_num = []
    for _ in range(20):
        if level == 1:
            num = random.randint(0, 9)
        if level == 2:
            num = random.randint(10, 99)
        if level == 3:
            num = random.randint(100, 999)
        all_num.append(num)
    make_operation(all_num)

def make_operation(all_num):
    points = 0
    for _ in range(10):
        fail_count = 0
        first_int = random.choice(all_num)
        second_int = random.choice(all_num)
        operation = (f"{first_int} + {second_int}")
        answer = -1
        while eval(operation) != answer:
            answer = int(input(str(operation) + " = "))
            if eval(operation) == answer:
                points += 1
                break
            if eval(operation) != answer:
                print("EEE")
                answer = -1
                fail_count += 1
            if fail_count == 3:
                print(f"{str(operation)} = {eval(operation)}")
                break
    print(F"Score: {points}") 
    sys.exit(0)





if __name__ == "__main__":
    main()
