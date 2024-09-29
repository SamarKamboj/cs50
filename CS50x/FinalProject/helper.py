import os
import requests
import urllib.parse
from cs50 import SQL

db = SQL("sqlite:///stock.db")


def lookup(symbol: str, timeperiod: str) -> list:
    '''Search for symbol and store in sql database'''
    symbol = symbol.lower()
    timeperiod = timeperiod.lower()

    # Search for symbol
    try:
        api_key = os.environ.get("API_KEY")
        # url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/chart/{urllib.parse.quote_plus(timeperiod)}/?token={api_key}"
        url = f"https://cloud.iexapis.com/stable/stock/{urllib.parse.quote_plus(symbol)}/chart/{urllib.parse.quote_plus(timeperiod)}/?token=pk_367412694e184c709f74251292922cdd&filter=symbol,date,close"
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        response = response.json()
    except (KeyError, TypeError, ValueError):
        return None

    # If symbol already in sql database
    # then don't add it
    symbols = set([i["symbol"] for i in db.execute("SELECT symbol FROM stocks")])
    if symbol not in symbols:
        db.execute("INSERT INTO stocks (symbol, timePeriod) VALUES (?, ?)", symbol, timeperiod)

    return response


def get_stocks() -> tuple:
    '''Get stocks information'''
    symbol_and_time = [(i["symbol"], i["timePeriod"]) for i in db.execute("SELECT * FROM stocks")]
    # Store all available stock info
    details = []
    for symbol, time in symbol_and_time:
        stock = lookup(symbol, time)
        if stock:
            details += stock

    # Format details into a different data structure
    # to pass it to HTML
    dates = []
    stocks = {}
    for i in details:
        if i["date"] not in dates:
            dates.append(i["date"])

        if i["symbol"] not in stocks:
            stocks[i["symbol"]] = {}

        if "close" not in stocks[i["symbol"]]:
            stocks[i["symbol"]]["close"] = []

        stocks[i["symbol"]]["close"].append(i["close"])

    rgbs = [
        "#FF5555", "#55FF55", "#5555FF", "#FF00CC",
        "#0000FF", "#000000", "#FF0000", "#00FF00",
        "#6600CC", "#CC0066", "#009900", "#FF0066"
    ]
    for i, j in zip(stocks, rgbs):
        stocks[i]["rgb"] = j

    return (dates, stocks)

