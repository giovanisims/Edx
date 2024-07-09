def main():
    vowel = input("Input: ")
    no_vowel = shorten(vowel)
    print(no_vowel, end="")

def shorten(v):
    for vowel in 'aeiouAEIOU':
        v = v.replace(vowel, '')
    return v


if __name__ == "__main__":
    main()