import requests
import time

class Aura:
    def __init__(self, url):
        self.url = url
        self.initApi()
        self.devices = self.getDevices()
    
    def initApi(self):
        requests.post(self.url + "/AuraSDK", json={"category": "SDK"})

    def getDevices(self):
        try:
            result = requests.get(self.url + "/AuraSDK/AuraDevice")
            print("Devices: ", result.json())
            if(result.json()["result"] != '0'):
                time.sleep(1)
                raise Exception("AuraSDK/AuraDevice: " + result.json()["result"])
            return result.json()
        except:
            return self.getDevices()

    def setColor(self, r, g, b):
        data = []
        for deviceId in self.devices.keys():
            obj = {
                "device" : deviceId,
                "range" : "all",
                "color" : rgbToDecimal(r, g, b),
                "apply": "true"
            }
            data.append(obj)
        
        result = requests.put(self.url + "/AuraSDK/AuraDevice/", json={"data": data})
        

# convert r g b to 65280 like format
def rgbToDecimal(r, g, b):
    return str((b << 16) | (g << 8) | r)