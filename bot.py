from models.ticker24h import Ticker24h
import time

from binanceapi import Binance
from filemanager import FileManager
from logger import Logger
from marketanalyzer import MarketAnalyzer
from models.buysignal import BuySignal
from tulp import Indicator


class Bot():


    def runOLD(self):
        markets = ["BTCUP", "BTCDOWN", "DOGE", "ETHUP", "ETHDOWN", "LINKUP", "LINKDOWN", "XMR", "ALICE", "DOTUP", "DOTDOWN"]
        interval = "15m"
        buySignals = [] 

        while True:

            for m in markets:

                marketSymbol = m + "USDT"

                indicator = self.getIndicators(marketSymbol, interval)
                # log.indicators(marketSymbol, interval, indicator)
                
                if indicator.fastk[-1] < 0.0001:

                    self.followZeroStoch(marketSymbol, interval)
                    currentPrice = float(api.getTicker(marketSymbol)["price"])
                    log.buySignal(BuySignal(marketSymbol, currentPrice, indicator))

                time.sleep(0.5)

            time.sleep(60)



    def run(self):

        pass

        

if __name__ == "__main__":

    auth = FileManager().loadApiKeys()
    api = Binance(auth)
    log = Logger()

    market = MarketAnalyzer()
        
    print("\nTAAAAAAAAH JIJ WEER?\n\n")

    for m in market.topVolumesUp:
        print()
        print(m.toJson())

    Bot().run()

   