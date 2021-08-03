
from models.basemodel import BaseModel


class Ticker24h(BaseModel):

    def __init__(self, ticker):

        self.symbol = ticker["symbol"]
        self.priceChange = ticker["priceChange"]
        self.priceChangePercent = ticker["priceChangePercent"]
        self.weightedAvgPrice = ticker["weightedAvgPrice"]
        self.prevClosePrice = ticker["prevClosePrice"]
        self.lastPrice = ticker["lastPrice"]
        self.lastQty = ticker["lastQty"]
        self.bidPrice = ticker["bidPrice"]
        self.bidQty = ticker["bidQty"]
        self.askPrice = ticker["askPrice"]
        self.askQty = ticker["askQty"]
        self.openPrice = ticker["openPrice"]
        self.highPrice = ticker["highPrice"]
        self.lowPrice = ticker["lowPrice"]
        self.volume = ticker["volume"]
        self.quoteVolume = ticker["quoteVolume"]
        self.openTime = ticker["openTime"]
        self.closeTime = ticker["closeTime"]
        self.firstId = ticker["firstId"]
        self.lastId = ticker["lastId"]
        self.count = ticker["count"]
