import json
import os

from models.apikey import ApiKey


class FileManager():


    def _fileExists(self, fileName):

        return os.path.exists(fileName)



    def _readFile(self, fileName):

        with open(fileName) as file:

            data = json.load(file)

        file.close()

        return data


   
    def _writeFile(self, fileName, data):

        with open(fileName, "w") as file:

            file.write(data)

        file.close()
        


    def loadApiKeys(self):

        path = "config/apikeys.json"
        keyObj = None
        
        if self._fileExists(path):

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

    auth = FileManager().loadApiKeys()

    print(auth.key)
    print(auth.secret)
    