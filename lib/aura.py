import requests

class Aura:
    def __init__(self, url):
        self.url = url
        self.initApi()
        self.devices = self.getDevices()
        print(self.devices)
    
    def initApi(self):
        result = requests.post(self.url + "/AuraSDK", json={"category": "SDK"})
        print(result.json())

    def getDevices(self):
        try:
            result = requests.get(self.url + "/AuraSDK/AuraDevice")
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
        
        print(data)
        result = requests.put(self.url + "/AuraSDK/AuraDevice/", json={"data": data})
        print(result.json())
        

# convert r g b to 65280 like format
def rgbToDecimal(r, g, b):
    return str((b << 16) | (g << 8) | r)