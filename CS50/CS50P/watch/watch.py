import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if video_index := re.search(r"^<.+youtube\.com/embed/([\w-]+)", s):
        return(f"https://youtu.be/{video_index.group(1)}")


if __name__ == "__main__":
    main()