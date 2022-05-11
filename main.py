from lib.leds import Leds
from lib.aura import Aura

aura = Aura("http://127.0.0.1:27339")
leds = Leds(29, "COM5")

def main():
    print("Hello world!")
    aura.setColor(0, 128, 0)
    leds.setAllLeds(0, 128, 0)


if __name__ == "__main__":
    main()
