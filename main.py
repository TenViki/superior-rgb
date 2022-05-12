import importlib
import json
from os import system
import time
from lib.animations import get_animations
from lib.leds import Leds
from lib.aura import Aura
from lib.logitech import Logitech
from lib.tray import setuptray
from threading import Thread

animationThread = None

animation = {
    "name": None,
    "max_t": 0,
    "module": None
}
animationEnded = False

config = None

def loadConfig():
    global config
    config = json.loads(open("config.json").read())

def updateConfig(config):
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=" ")

loadConfig()

print("Waiting 2 minutes to give all the services time to start")
time.sleep(120)

# Load all the SDKS
print("Loading SDKs")
aura = Aura("http://127.0.0.1:27339")
leds = Leds(config["stripLeds"], config["port"], config["baudrate"])
logitech = Logitech()
print("SDKs loaded")

def set_animation(_, animationstr):
    global animationEnded
    global animation
    global animationThread

    animationName = animationstr.split(".")[0]
    module = importlib.import_module("animations." + animationName)

    animation["name"] = animationName
    animation["max_t"] = module.max_t
    animation["module"] = module

    print("Set animation to", animation["name"])

    if animationThread is not None:
        animationEnded = True
        animationThread.join()

    animationThread = Thread(target=animate, daemon=False)
    animationEnded = False
    animationThread.start()

    config["animation"] = animation["name"]
    updateConfig(config)

def animate():
    global animation
    print("Animating", animation)

    max_t = animation["max_t"]
    module = animation["module"]

    while True:
        for t in range(max_t + 1):
            delay, r, g, b = module.process(t)
            set_color(min(r, 255), min(g, 255), min(255, b))
            time.sleep(delay / 1000)
            if animationEnded:
                return




def quit():
    global animationEnded
    print("Quitting")
    if animationThread is not None:
        animationEnded = True
        animationThread.join()


def set_color(r, g, b):
    logitech.setColor(r, g, b)
    aura.setColor(r, g, b)
    leds.setAllLeds(r, g, b)

def main():
    if(config["animation"] is not None):
        set_animation(None, config["animation"])

    setuptray(get_animations(), set_animation, quit)

if __name__ == "__main__":
    main()


