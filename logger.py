from filemanager import FileManager
import time

from models.tradesignal import TradeSignal
from tulp import Indicator


class Logger():


    def __init__(self):

        self.fileManager = FileManager()
        


    def _currentTime(self, timestamp):

        return time.strftime("%H:%M:%S", time.localtime(timestamp))



    def tradeSignal(self, signal: TradeSignal):

        self.fileManager.saveTradeSignal(signal)

        print("\n{:<10} {} {:<10} Price: {:<20}".format(self._currentTime(signal.timestamp), signal.marketSide.upper(), signal.marketSymbol, signal.price))
        print("\t   RSI: {:<8.2f}  STOCHRSI: {:<8.2f}".format(
            signal.rsi,
            signal.stochRsi,
            )
        )



    def indicators(self, symbol, interval, indicator: Indicator):

        print("\n" + 14 * "=" + " {:<15} {} ".format(symbol, interval) + 14 * "=" + "\n")
    
        print("BBANDS\t :\t{:>10.2f} {:>10.2f} {:>10.2f}\nRSI\t :\t{:>10.2f} {:>10.2f} {:>10.2f}\nSTOCHRSI :\t{:>10.2f} {:>10.2f}".format(
            indicator.bbandsUpper[-1],
            indicator.bbandsMiddle[-1],
            indicator.bbandsLower[-1],
            indicator.rsiFast[-1],
            indicator.rsiMedium[-1],
            indicator.rsiSlow[-1],
            indicator.fastk[-1],
            indicator.fastd[-1]
            )
        )



    def indicatorInfo(self, indicator):

        print("\nType: {}\nFull name: {}\nInputs: {}\nOptions: {}\nOutputs: {}".format(
            indicator.type,
            indicator.full_name,
            indicator.inputs,
            indicator.options,
            indicator.outputs
            )
        )
