from sys import argv, exit
import requests
import json

# Length of Command-line argument must equal to 2
if len(argv) != 2:
    exit("Missing command-line argument")

try:
    # Try converting command-line argument 1 into decimal number
    bitcoin_num = float(argv[1])
except ValueError:
    # Exit if unable to convert to decimal
    exit("Command-line argument is not a number")
else:
    try:
        # Try to fetch data on given api
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        # Exit if unable to fetch the data
        exit()
    else:
        # Store data
        data = response.json()
        # Get USD dictionary
        usd_dict = data["bpi"]["USD"]
        # Total dollars in current time
        dollars = usd_dict["rate_float"] * bitcoin_num
        # Output price of given number of bitcoin/s
        print(f"${dollars:,.4f}", end='')

