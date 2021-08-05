import json
import time

from binance.client import Client
from binance.enums import ORDER_TYPE_LIMIT, SIDE_BUY, TIME_IN_FORCE_GTC
from binance.exceptions import BinanceAPIException


class Binance:


    def __init__(self, auth):

        self.timeOutSeconds = 5
        self.client = Client(auth.key, auth.secret)


    # Test connectivity to the Rest API.
    # GET /api/v1/ping
    def ping(self):

        self.client.ping()


    # Fetch system status
    # GET /sapi/v1/system/status 
    def getSystemStatus(self):

        systemStatus = None
        while not systemStatus:

            try:
                systemStatus = self.client.get_system_status()
            
            except Exception as e:

                self._errorTimeOut(e)

        return systemStatus



    # Test connectivity to the Rest API and get the current server time.
    # GET /api/v1/time
    def getServerTime(self):

        serverTime = None
        while not serverTime:

            try:
                servertime = self.client.get_server_time()
            
            except Exception as e:

                self._errorTimeOut(e)

        return servertime


    # Daily Account Snapshot (USER_DATA)
    # GET /sapi/v1/accountSnapshot (HMAC SHA256) 
    def getDailyAccountSnapshot(self, _type):

        accountSnapshot = None
        while not accountSnapshot:

            try:
                accountSnapshot = self.client.get_account_snapshot(type=_type)

            except Exception as e:

                self._errorTimeOut(e)

        return accountSnapshot



    # Get current account information.
    # GET /api/v3/account (HMAC SHA256)
    def getAccountDetails(self):

        account = None
        while not account:

            try:
                account = self.client.get_account()

            except Exception as e:

                self._errorTimeOut(e)

        return account



    # Get current account information
    # GET /api/v3/account (HMAC SHA256)
    def getAssetBalance(self, symbol):

        balance = None
        while not balance:

            try:
                balance = self.client.get_asset_balance(asset=symbol)

            except Exception as e:

                self._errorTimeOut(e)

        return balance



    # Orderbook for a given symbol
    # GET /api/v3/depth 
    def getOrderBook(self, _symbol):
        
        orderBook = None
        while not orderBook:

            try:
                orderBook = self.client.get_order_book(symbol=_symbol)

            except Exception as e:

                self._errorTimeOut(e)
        
        return orderBook



    # Latest price for a symbol or symbols.
    # GET /api/v3/ticker/price
    def getTicker(self, _symbol):

        ticker = None
        while not ticker:

            try:
                ticker = self.client.get_symbol_ticker(symbol=_symbol)

            except Exception as e:

                self._errorTimeOut(e)

        return ticker



    # Latest price for a symbol or symbols.
    # GET /api/v3/ticker/price
    def get24hTicker(self, _symbol):

        ticker24h = None 
        while not ticker24h:

            try:
                ticker24h = self.client.get_ticker(symbol=_symbol)

            except Exception as e:

                self._errorTimeOut(e)

        return ticker24h



    # Current average price for a symbol.
    # GET /api/v3/avgPrice
    def getAvgPrice(self, _symbol):

        averagePrice = None
        while not averagePrice:

            try:
                averagePrice = self.client.get_avg_price(symbol=_symbol)

            except Exception as e:

                self._errorTimeOut(e)

        return averagePrice



    # Kline/candlestick bars for a symbol.
    # GET /api/v3/klines
    def getCandlesticks(self, _symbol, _interval):

        candlesticks = None
        while not candlesticks:

            try:
                candlesticks = self.client.get_klines(
                    symbol      = _symbol,
                    interval    = _interval
                )

            except Exception as e:
                
                self._errorTimeOut(e)

        return candlesticks



    # Kline/candlestick bars for a symbol.
    # GET /api/v3/klines
    def getHistoricalCandlesticks(self, _symbol, _interval, _startTime, _endTime, _limit):

        historicalCandlesticks = None
        while not historicalCandlesticks:

            try:
                historicalCandlesticks = self.client.get_historical_klines(
                    symbol      = _symbol,
                    interval    = _interval,
                    startTime   = _startTime,
                    endTime     = _endTime,
                    limit       = _limit
                )

            except Exception as e:

                self._errorTimeOut(e)

        return historicalCandlesticks



    # Creates and validates a new order but does not send it into the matching engine.
    # POST /api/v3/order/test (HMAC SHA256)
    def testOrder(self, _symbol, _quantity, _price):

        testOrder = None
        while not testOrder:

            try:
                testOrder = self.client.create_test_order(
                    symbol      = _symbol,
                    side        = SIDE_BUY,
                    type        = ORDER_TYPE_LIMIT,
                    timeInForce = TIME_IN_FORCE_GTC,
                    quantity    = _quantity,
                    price       = _price
                )          

            except Exception as e:
                
                self._errorTimeOut(e)
        
        return testOrder



    # New market order (TRADE) 
    # POST /api/v3/order  (HMAC SHA256)
    def marketOrder(self, _symbol, side, _quantity):

        marketOrder = None
        while not marketOrder:

            try:

                if side == 'buy':

                    marketOrder = self.client.order_market_buy(
                        symbol      = _symbol,
                        quantity    = _quantity
                    )

                else:

                    marketOrder = self.client.order_market_sell(
                        symbol      = _symbol,
                        quantity    = _quantity
                    )        

            except Exception as e:

                self._errorTimeOut(e)

        return marketOrder



    # New limit order (TRADE) 
    # POST /api/v3/order  (HMAC SHA256)
    def limitOrder(self, _symbol, _price, side, _quantity):

        limitOrder = None
        while not limitOrder:

            try:

                if side == 'buy':

                    order = self.client.order_limit_buy(
                        symbol      = _symbol,
                        quantity    = _quantity,
                        price       = _price
                    )

                else:

                    order = self.client.order_limit_sell(
                        symbol      = _symbol,
                        quantity    = _quantity,
                        price       = _price
                    )    

            except Exception as e:

                self._errorTimeOut(e)

        return order



    # Cancel an active order.
    # DELETE /api/v3/order  (HMAC SHA256)
    def cancelOrder(self, _symbol, _orderId):

        cancelledOrder = None
        while not cancelledOrder:

            try:

                result = self.client.cancel_order(
                    symbol      = _symbol,
                    orderId     = _orderId
                )

            except Exception as e:

                self._errorTimeOut(e)

        return result



    # Get all open orders on a symbol. Careful when accessing this with no symbol.
    # GET /api/v3/openOrders  (HMAC SHA256)
    def getOpenOrders(self, _symbol):

        openOrders = None
        while not openOrders:

            try:
                openOrders = self.client.get_open_orders(symbol=_symbol)

            except Exception as e:

                self._errorTimeOut(e)

        return openOrders



    # Check an order's status.
    # GET /api/v3/order (HMAC SHA256)
    def getOrderStatus(self, _symbol, _orderId):

        orderStatus = None
        while not orderStatus:

            try:
                orderStatus = self.client.get_order(
                    symbol  = _symbol,
                    orderId = _orderId
                )

            except Exception as e:
                self._errorTimeOut(e)

        return orderStatus



    def _errorTimeOut(self, error):

        print(error)
        time.sleep(self.timeOutSeconds)



    def _printJson(self, jsonData):

        print(json.dumps(jsonData, indent=4, sort_keys=True))



    def _printError(self, error):

        print(
            '[!] Binance API Exception\n    Status code: {}\n    {}'
            .format(
                error.status_code, 
                error.message
            )
        )
