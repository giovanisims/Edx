import requests
import sys

try:
    sys.argv[1]
except IndexError:
    sys.exit("Missing command-line argument")
try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
coindesk = requests.get(url).json()
bitcoin_usd = (coindesk["bpi"]["USD"]["rate_float"] * float(sys.argv[1]))
print(f"${bitcoin_usd:,.4f}",end="")