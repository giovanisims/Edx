def main():
    g_list = []
    full_g_list = get_list(g_list)
    check_list(full_g_list)

def get_list(gl):
    while True:
        try:
            item = input().upper()
            gl.append(item)
        except EOFError:
            gl.sort()
            return gl
        
def check_list(fgl):
    item_count = {}
    for item in fgl:
        if item in item_count:
            item_count[item] += 1
        else:
            item_count[item] = 1

    for item, count in item_count.items():
        print(f"{count} {item}")


main()