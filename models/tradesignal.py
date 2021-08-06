import time

from models.basemodel import BaseModel


class TradeSignal(BaseModel):


    def __init__(self, marketSide, marketSymbol, price, indicator):

        self.timestamp = time.time()
        self.marketSide = str(marketSide)
        self.marketSymbol = str(marketSymbol)
        self.price = float(price)
        self.rsi = indicator.rsiFast[-1]
        self.stochRsi = indicator.fastk[-1]
        # self.lowerbandCrossed = indicator.bbandsLower[-1] > price
