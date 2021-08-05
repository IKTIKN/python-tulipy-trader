import time

from models.basemodel import BaseModel


class TradeSignal(BaseModel):


    def __init__(self, type, marketSymbol, price, indicator):

        self.timestamp = time.time()
        self.type = type
        self.symbol = marketSymbol
        self.price = price
        self.rsi = indicator.rsiFast[-1]
        self.stochRsi = indicator.fastk[-1]
        self.lowerbandCrossed = indicator.bbandsLower[-1] > price
