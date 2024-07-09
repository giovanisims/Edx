def main():
    camelcase = get_var()
    var_list = split(camelcase)
    convert_var(var_list)

def get_var():
    camelcase = input("Enter a CamelCase variable name: ")
    return camelcase

def split(camelcase):
    words = [[camelcase[0]]]

    for c in camelcase[1:]:
        if c.isupper():
            words.append([c])
        else:
            words[-1].append(c)

    return [''.join(word) for word in words]

def convert_var(var_list):
    result = '_'.join([w.lower() for w in var_list])
    print(result)

main()
