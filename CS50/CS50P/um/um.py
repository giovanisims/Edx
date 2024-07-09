import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_count = 0
    for um in re.findall(r"\bum\b", s, re.IGNORECASE):
        um_count += 1
    return um_count

if __name__ == "__main__":
    main()