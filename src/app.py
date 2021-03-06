import json

import bitmex
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Write api_key and api_secret in string
client = bitmex.bitmex(api_key="<bitmex_api_key>",
                       api_secret="<bitmex_api_secret>")


@app.route("/")
def index():
    return "bitmex api"


@app.route("/data/order")
def order():
    order_data = client.Order.Order_getOrders(
        symbol="XBTUSD", reverse=True).result()  # order data
    # default=str for datetime filter
    return json.dumps(order_data, default=str)


@app.route("/data/instrument")
def instrument():
    instrument_data = client.Instrument.Instrument_get(
        symbol="XBTUSD", reverse=True).result()  # Instrument data
    return json.dumps(instrument_data, default=str)


@app.route("/data/position")
def position():
    position_data = client.Position.Position_get(
        filter=json.dumps({'symbol': 'XBTUSD'})).result()
    return json.dumps(position_data, default=str)


@app.route("/data/quote")
def quote():
    quote_data = client.Quote.Quote_get(symbol='XBTUSD').result()
    return json.dumps(quote_data, default=str)


if __name__ == '__main__':
    app.run()
