from models.basemodel import BaseModel

class Ticker(BaseModel):
    
    def __init__(self, ticker):

        self.symbol = ticker["symbol"]
        self.price = float(ticker["price"])