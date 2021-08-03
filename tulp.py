import numpy as np
import tulipy as ti


class Indicator():

    RSI_FAST_PERIOD     = 6
    RSI_MEDIUM_PERIOD   = 12
    RSI_SLOW_PERIOD     = 24

    STOCHRSI_PERIOD     = 14
    FASTK_PERIOD        = 3
    FASTD_PERIOD        = 3

    BOLLINGER_PERIOD    = 14
    STANDARD_DEVIATION  = 2


    def __init__(self, candlesticks):

        self.prices = self._extractClosePrices(candlesticks)
        
        self.bbandsLower, self.bbandsMiddle, self.bbandsUpper = self._bbands(self.prices, self.BOLLINGER_PERIOD, self.STANDARD_DEVIATION)
        
        self.fastk, self.fastd = self._stochrsi(self.prices, self.STOCHRSI_PERIOD, self.FASTK_PERIOD, self.FASTD_PERIOD)

        self.rsiFast    = self._rsi(self.prices, self.RSI_FAST_PERIOD)
        self.rsiMedium  = self._rsi(self.prices, self.RSI_MEDIUM_PERIOD)
        self.rsiSlow    = self._rsi(self.prices, self.RSI_SLOW_PERIOD)



    def _extractClosePrices(self, priceData):

        closePrices = []

        for p in priceData:

            closePrices.append(p[4])

        return np.array(closePrices, dtype='f8')



    def _rsi(self, closePrices, period):

        return ti.rsi(closePrices, period)



    def _stochrsi(self, closePrices, period, fastkPeriod, fastdPeriod):

        rsi = self._rsi(closePrices, period)

        return ti.stoch(rsi, rsi, rsi, period, fastkPeriod, fastdPeriod)



    def _bbands(self, closePrices, period, deviation):

        return ti.bbands(closePrices, period, deviation)

        
