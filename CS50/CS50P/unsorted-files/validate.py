import re

email = input("Enter your email address: ").strip()

# \w is [a-zA-Z0-9_]
if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.edu$",email, re.IGNORECASE):   
    print("Valid")
else:
    print("Invalid")