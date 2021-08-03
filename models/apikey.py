import json


class ApiKey():
    

    def __init__(self, key, secret):

        self.key = key
        self.secret = secret


    def toJson(self):

        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
