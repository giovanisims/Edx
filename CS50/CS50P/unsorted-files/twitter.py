import re

url = input("URL: ").strip()

if username := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(\w+)$", url, re.IGNORECASE):
    print(f"Username: {username.group(1)}")

