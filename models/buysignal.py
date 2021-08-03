import json
import time


class BuySignal():
    

    def __init__(self, marketSymbol, price, indicator):

        self.timestamp = time.time()
        self.symbol = marketSymbol
        self.price = price
        self.rsi = indicator.rsiFast[-1]
        self.stochRsi = indicator.fastk[-1]
        self.lowerbandCrossed = indicator.bbandsLower[-1] > price



    def toJson(self):

        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
