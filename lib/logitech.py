import ctypes
import time

class Logitech:
    def __init__(self):
        self.logidll = ctypes.windll.LoadLibrary("lib/inc/LogitechLedEnginesWrapper.dll")
        self.logidll.LogiLedInit()
        time.sleep(1)

    def setColor(self, r, g, b):
        self.logidll.LogiLedSetLighting(int(r / 256 * 100), int(g / 256 * 100), int(b / 256 * 100))



