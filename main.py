import time
from lib.leds import Leds
from lib.aura import Aura
from lib.logitech import Logitech

aura = Aura("http://127.0.0.1:27339")
leds = Leds(29, "COM5")
logitech = Logitech()

def main():
    print("Hello world!")
    aura.setColor(255, 128, 0)
    leds.setAllLeds(255, 128, 0)
    logitech.setColor(255, 128, 0)
    time.sleep(1)


if __name__ == "__main__":
    main()
