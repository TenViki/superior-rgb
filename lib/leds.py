import serial

class Leds:

    def __init__(self, numleds, port):
        self.com = serial.Serial(port, 115200)
        self.buffer = bytearray(6 + numleds * 3);
        self.colors = []
        self.numleds = numleds

        self.resetLeds()

    def defineLED(self, led, r, g, b, update = True):
        self.colors[led] = [r, g, b]
        if update:
            self.controlLED(self.colors)

    def shiftColors(self, r, g, b):
        self.colors.pop(len(self.colors) - 1)
        self.colors.insert(0, [r, g, b])
    
    def resetLeds(self):
        self.colors = []
        for i in range(self.numleds):
            self.colors.append([0, 0, 0])

    def update(self):
        self.controlLED(self.colors)

    def setAllLeds(self, r, g, b):
        self.colors = []
        for i in range(self.numleds):
            self.colors.append([r, g, b])
            
        self.controlLED(self.colors)

    def controlLED(self, arr):
        self.buffer[0] = 65
        self.buffer[1] = 100
        self.buffer[2] = 97
        self.buffer[3] = (self.numleds - 1) >> 8
        self.buffer[4] = (self.numleds - 1) & 0xff
        self.buffer[5] = self.buffer[3] ^ self.buffer[4] ^ 0x55

        num = 0;

        for i in range(6, 6 + self.numleds * 3, 3):

            self.buffer[i + 0] = int((arr[num][0] * 255) / 255)
            self.buffer[i + 1] = int((arr[num][1] * 255) / 255)
            self.buffer[i + 2] = int((arr[num][2] * 255) / 255)

            num += 1

        self.com.write(self.buffer)
    
    