
from models.tradesignal import TradeSignal
from models.ticker import Ticker
import time

from binanceapi import Binance
from filemanager import FileManager
from models.buysignal import BuySignal
from models.ticker24h import Ticker24h
from tulp import Indicator


class MarketAnalyzer():


    def __init__(self):

        self.quoteAsset = "USDT"
        self.top = 10

        self.api = Binance(FileManager().loadApiKeys())

        # self.markets, self.downMarkets, self.upMarkets = self._getMarkets(self.quoteAsset)

        # self.topGainers, self.topLosers, self.topVolumes = self._sortMarkets(self.markets, self.top)
        # self.topGainersUp, self.topLosersUp, self.topVolumesUp = self._sortMarkets(self.upMarkets, self.top)
        # self.topGainersDown, self.topLosersDown, self.topVolumesDown = self._sortMarkets(self.downMarkets, self.top)



    def _getMarkets(self, quoteAsset):
        
        tickers = self.api.get24hTicker(None)

        upQuoteAsset = "UPUSDT"
        downQuoteAsset = "DOWNUSDT"

        banTickers = ["VEN", "BUSD", "USD", "EUR", "GBP", "PAX", "TUSD", "STRAT", "USDC", "BEAR", "BULL", "DAI", "SUSD"]

        markets = []
        downMarkets = []
        upMarkets = []

        for ticker in tickers:

            t = Ticker24h(ticker)
            
            if t.symbol[-len(quoteAsset):] == quoteAsset:

                if t.symbol[-len(upQuoteAsset):] == upQuoteAsset: 

                    upMarkets.append(t)

                elif t.symbol[-len(downQuoteAsset):] == downQuoteAsset:

                    downMarkets.append(t) 

                elif t.symbol[:-len(quoteAsset)] not in banTickers:

                    markets.append(t)


        return markets, downMarkets, upMarkets


    
    def _sortMarkets(self, markets, top):

        topGainers = sorted(markets, reverse=True, key=lambda d: float(d.priceChangePercent))[:top]
        topLosers = sorted(markets, key=lambda d: float(d.priceChangePercent))[:top]
        topVolumes = sorted(markets, reverse=True, key=lambda d: float(d.quoteVolume))[:top]

        return topGainers, topLosers, topVolumes



    def getIndicators(self, marketSymbol, interval):

        candlesticks = self.api.getCandlesticks(marketSymbol, interval)

        return Indicator(candlesticks)



    def waitForBuySignal(self):

        tradeMarketSymbols = ["LINKUPUSDT", "LINKDOWNUSDT"]
        interval = "15m"
        stochRsiTreshold = 0.0001

        buySignal = None

        while not buySignal:

            for symbol in tradeMarketSymbols:

                indicator = self.getIndicators(symbol, interval)

                if indicator.fastk[-1] < stochRsiTreshold:

                    indicator = self.followZeroStoch(symbol, interval)
                    ticker = Ticker(self.api.getTicker(symbol))
                    buySignal = BuySignal(symbol, ticker.price, indicator)

                    break

                else:

                    time.sleep(30)
        
        return buySignal

    

    def waitForSellSignal(self, symbol, buyPrice):

        interval = "15m"
        stochRsiTreshold = 0.0001
        stopLossPercentage = 0.95

        sellSignal = None
        while not sellSignal:
            
            indicator = self.getIndicators(symbol, interval)
            ticker = Ticker(self.api.getTicker(symbol)) 

            print(ticker.price, indicator.fastk[-1])

            if (buyPrice * stopLossPercentage) >= buyPrice:
                sellSignal = TradeSignal("sell", symbol, ticker.price, indicator)
                print("stoploss")

            if indicator.fastk[-1] <= stochRsiTreshold:
                sellSignal = TradeSignal("sell", symbol, ticker.price, indicator)
                print("zerostoch")

            else:
                time.sleep(30)

                

    def followZeroStoch(self, marketSymbol, interval):
        #TODO FALSE POSITIVES

        zeroStochRSI = 0
        while zeroStochRSI < 5:

            time.sleep(50)

            indicator = self.getIndicators(marketSymbol, interval)

            if indicator.fastk[-1] > 0.0001:
                zeroStochRSI += 1

            else:
                zeroStochRSI = 0

        return indicator
