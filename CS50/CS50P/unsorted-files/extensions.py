def main():
    file_name = get_file()
    check_file(file_name)

def get_file():
    file_name = input("Enter the file name: ").strip().lower()
    return file_name

def check_file(f):
    if f.endswith(".gif"):
        print("image/gif")
    elif f.endswith(".jpg") or f.endswith(".jpeg"):
        print("image/jpeg")
    elif f.endswith(".png"):
        print("image/png")
    elif f.endswith(".pdf"):
        print("application/pdf")
    elif f.endswith(".txt"):
        print("text/plain")
    elif f.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()