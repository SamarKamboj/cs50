# STOCK CHART
### Video Demo: https://youtu.be/kRAk0YNo3Oc
### Description:
Hello CS50 Lovers! I am Samar from India and I love CS50.
My Final Project is to create a graph of stocks historical records
to get an idea of what's going on these days with companies.

My project contains one main, one helper file and one SQL database.
Let's start from SQL database because it contains less information

##### stock.db
It has 3 columns:- id, symbol and timePeriod.
id tracks uniqueness of row, symbol contain all companys stock symbol
that we added and timePeriod contains the length of historical data that
we want to see.

##### app.py and helper.py
I imported Flask, cs50's SQL, os and helper file which is in the directory.

First I check if developer exported his/her API KEY (from IEX CLOUD)
if not then raises an error telling to export your api_key.

There's db and app object from SQL and Flask respectively.
I passed out zip function from python to be able to use it in jinja2 syntax.

In line 16 I declared route '/' or 'index' which calls the function index underneath it.
The route has 2 methods "GET" and "POST"
if method is GET then fetch information from site and render the index.html template giving it all required variables.
else if method is POST then get the symbol that user submitted. If empty then render an apology template.
After that I fetch the time period (if any) else default to 1 month.

Now comes lookup function that I made in and imported from helper file.
This function search for the given symbol and time period on IEX CLOUD site and return the details (if available) in json format.
Note: If wrong symbol or symbol not provided then it will show some error
This lookup function uses a module named requests that comes with Python
I used get function from requests module to get details from site.
If successfull then insert that symbol and time period into sql database and return the details else return None

If lookup function ran successfully, get_stocks function comes into play from helper file.
This function get all available stocks information
from SQL database 'stock.db' using first function.
In line 41 (helper.py), symbol_and_time is a list of tuples containing all symbols and time period in sql database
I need this to get each and every stock's detail
The details is a list of dictionary that contains all stocks symbol, date, close price.
I then filter the dates and stocks symbol with close price and rgb value to pass it to html

In line 48 (app.py), I defined a '/remove' route which calls function remove that removes a stock from graph/sql database.

(app.py) In last I made a function that changes the time period of each stock's historical record.

#### Run:
To run the program export your api_key into system like "export API_KEY={YOUR API KEY}"
then type "flask run" and press Enter. Go to the link provided by flask and start trading!