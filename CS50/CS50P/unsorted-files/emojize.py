import emoji

alias = {
    ":thumbsup:": ":thumbs_up:",
    "hello, :earth_africa:": "hello, :globe_showing_Europe-Africa:",
    "hello, :earth_americas:": "hello, :globe_showing_Americas:",
    "hello, :earth_asia:": "hello, :globe_showing_Asia-Australia:",
}

code = input("input: ")

if code in alias:
    print(emoji.emojize(alias[code]))
else:
    print(emoji.emojize(code))
