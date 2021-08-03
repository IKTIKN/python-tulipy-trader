
from models.basemodel import BaseModel


class ApiKey(BaseModel):
    

    def __init__(self, key, secret):

        self.key = key
        self.secret = secret
