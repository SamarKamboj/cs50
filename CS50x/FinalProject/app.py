from flask import Flask, render_template, redirect, request
from helper import get_stocks, lookup
import os
from cs50 import SQL

# Export API KEY into system
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

db = SQL("sqlite:///stock.db")
app = Flask(__name__)

app.jinja_env.globals.update(zip=zip)
TIME_PERIOD = list(map(str.upper, ["7d", "1m", "6m", "1y", "10y"]))

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return render_template("apology.html", message="Please provide symbol!")

        # Fetch time period from sql file
        # If NULL then default to 1 month
        time_period = db.execute("SELECT timePeriod FROM stocks")
        if time_period:
            time_period = time_period[0]["timePeriod"]
        else:
            time_period = "1M"
        # Look for symbol on IEX CLOUD and save it to sql file
        # If unsuccessful in saving or fetching from site then render error message
        if not lookup(symbol, time_period):
            return render_template("apology.html", message="Invalid Symbol or Symbol Exist!")

        # Get symbol, rgb value, date and close price of a stock respectively
        dates, stocks = get_stocks()
        return render_template(
            "index.html", dates=dates, stocks=stocks, time_period=TIME_PERIOD,
            )
    else:
        # Get symbol, rgb value, date and close price of a stock respectively
        dates, stocks = get_stocks()
        return render_template(
            "index.html", dates=dates, stocks=stocks, time_period=TIME_PERIOD,
            )


@app.route("/remove", methods=["POST"])
def remove():
    symbol = request.form.get("symbol")
    # Remove stock from graph
    db.execute("DELETE FROM stocks WHERE symbol = ?", symbol.lower())
    return redirect('/')


@app.route("/time", methods=["POST"])
def time():
    time = request.form.get("time").lower()
    # Update stocks time period
    db.execute("UPDATE stocks SET timePeriod = ?", time)
    return redirect('/')

