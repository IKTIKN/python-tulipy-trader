import json
import os

from models.apikey import ApiKey
from models.tradesignal import TradeSignal


class FileManager():


    def _pathExists(self, path):

        directory = path.split("/")[0]

        if not os.path.isdir(directory):

            os.mkdir(directory)

        return os.path.exists(path)



    def _readFile(self, fileName):

        with open(fileName) as file:

            data = json.load(file)

        file.close()

        return data


   
    def _writeFile(self, fileName, data):

        with open(fileName, "w") as file:

            file.write(data)

        file.close()
    


    def saveTradeSignal(self, tradeSignal: TradeSignal):

        path = "output/tradesignals.json"

        if self._pathExists(path):

            dict = self._readFile(path)
            dict["tradeSignals"].append(json.loads(tradeSignal.toJson()))

            self._writeFile(path, json.dumps(dict))
            
        else:
            dict = {"tradeSignals": [json.loads(tradeSignal.toJson())]}           
            self._writeFile(path, json.dumps(dict))



    def loadApiKeys(self):

        path = "config/apikeys.json"
        keyObj = None
        
        if self._pathExists(path):

            keyData = self._readFile(path)
            keyObj = ApiKey(keyData["key"], keyData["secret"])

        else:

            apiKey = input("\n[!] No API key found\n\n    Enter API key : ")
            secret = input("    Enter secret  : ")

            keyObj = ApiKey(apiKey, secret)

            self._writeFile(path, keyObj.toJson())
        
        return keyObj



    def loadSettings(self):

        pass


if __name__ == "__main__":
    fileManager = FileManager()
    
    fileManager.saveTradeSignal()
    fileManager.loadApiKeys()
    # print(fileManager._pathExists(teststring))

    