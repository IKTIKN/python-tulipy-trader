import json

from binance.client import Client
from binance.enums import ORDER_TYPE_LIMIT, SIDE_BUY, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException


class Binance:


    def __init__(self, auth):
        
        self.client = Client(auth.key, auth.secret)


    # Test connectivity to the Rest API.
    # GET /api/v1/ping
    def ping(self):

        self.client.ping()



    # Test connectivity to the Rest API and get the current server time.
    # GET /api/v1/time
    def getServerTime(self):

        servertime = self.client.get_server_time()

        return servertime



    # Get current account information.
    # GET /api/v3/account (HMAC SHA256)
    def getAccountDetails(self):

        account = ""

        try:
            account = self.client.get_account()

        except BinanceAPIException as e:

            self.printError(e)

        return account



    def getAssetBalance(self, symbol):

        balance = self.client.get_asset_balance(asset=symbol)

        return balance


    # Latest price for a symbol or symbols.
    # GET /api/v3/ticker/price
    def getTicker(self, _symbol):

        ticker = self.client.get_symbol_ticker(symbol=_symbol)

        return ticker



    # Latest price for a symbol or symbols.
    # GET /api/v3/ticker/price
    def get24hTicker(self, symbol):

        ticker = self.client.get_ticker(symbol=symbol)

        return ticker



    # Current average price for a symbol.
    # GET /api/v3/avgPrice
    def getAvgPrice(self):
        return



    # Kline/candlestick bars for a symbol.
    # GET /api/v3/klines
    def getCandlesticks(self, _symbol, _interval):

        return self.client.get_klines(symbol=_symbol, interval=_interval)



    # Kline/candlestick bars for a symbol.
    # GET /api/v3/klines
    def getHistoricalCandlesticks(self, symbol, interval, startTime, endTime, limit):

        return self.client.get_historical_klines(symbol, interval, startTime, endTime, limit)



    # Creates and validates a new order but does not send it into the matching engine.
    # POST /api/v3/order/test (HMAC SHA256)
    def testOrder(self):

        try:
            testOrder = self.client.create_test_order(
                symbol='LINKBTC',
                side=SIDE_BUY,
                type=ORDER_TYPE_LIMIT,
                timeInForce=TIME_IN_FORCE_GTC,
                quantity=112,
                price='0.00001'
            )          

        except BinanceAPIException as e:
            
            self.printError(e)
        
        else: 
            return testOrder



    # New market order (TRADE) 
    # POST /api/v3/order  (HMAC SHA256)
    def marketOrder(self, _symbol, side, _quantity):

        if side == 'buy':

            order = self.client.order_market_buy(
                symbol=_symbol,
                quantity=_quantity
            )

        else:

            order = self.client.order_market_sell(
                symbol=_symbol,
                quantity=_quantity
            )           

        return order



    # New limit order (TRADE) 
    # POST /api/v3/order  (HMAC SHA256)
    def limitOrder(self, _symbol, _price, side, _quantity):

        if side == 'buy':

            order = self.client.order_limit_buy(
                symbol=_symbol,
                quantity=_quantity,
                price =_price
            )

        else:

            order = self.client.order_limit_sell(
                symbol=_symbol,
                quantity=_quantity,
                price =_price
            )    

        return order



    # Cancel an active order.
    # DELETE /api/v3/order  (HMAC SHA256)
    def cancelOrder(self, _symbol, _orderId):

        result = self.client.cancel_order(
            symbol=_symbol,
            orderId=_orderId
        )

        return result



    # Get all open orders on a symbol. Careful when accessing this with no symbol.
    # GET /api/v3/openOrders  (HMAC SHA256)
    def getOpenOrders(self, _symbol):

        orders = self.client.get_open_orders(symbol=_symbol)

        return orders



    # Check an order's status.
    # GET /api/v3/order (HMAC SHA256)
    def getOrderStatus(self, _symbol, _orderId):

        status = self.client.get_order(
            symbol=_symbol,
            orderId = _orderId
        )

        return status



    def printJson(self, jsonData):

        print(json.dumps(jsonData, indent=4, sort_keys=True))



    def printError(self, error):

        print(
            '[!] Binance API Exception\n    Status code: {}\n    {}'
            .format(
                error.status_code, 
                error.message
            )
        )

