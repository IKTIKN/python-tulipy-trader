
from logger import Logger
from marketanalyzer import MarketAnalyzer


class Bot():

    def run(self):

        while True:

            buySignal = market.waitForBuySignal()
            log.tradeSignal(buySignal)

            sellSignal = market.waitForSellSignal(buySignal.symbol, buySignal.price)
            log.tradeSignal(sellSignal)


if __name__ == "__main__":

    log = Logger()
    market = MarketAnalyzer()
        
    print("\nTAAAAAAAAH JIJ WEER?\n\n")

    Bot().run()

   