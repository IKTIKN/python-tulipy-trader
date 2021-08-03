import json

class BaseModel():

    def toJson(self):

        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
