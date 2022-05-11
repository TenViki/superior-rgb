import importlib
from os import system
import time
from lib.animations import get_animations
from lib.leds import Leds
from lib.aura import Aura
from lib.logitech import Logitech
from lib.tray import setuptray
from threading import Thread

aura = Aura("http://127.0.0.1:27339")
leds = Leds(29, "COM5")
logitech = Logitech()

animationThread = None

animation = {
    "name": None,
    "max_t": 0,
    "module": None
}
animationEnded = False

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

def animate():
    global animation
    print("Animating", animation)

    max_t = animation["max_t"]
    module = animation["module"]

    while True:
        for t in range(max_t + 1):
            delay, r, g, b = module.process(t)
            print(delay, r, g, b)
            set_color(r, g, b)
            time.sleep(delay / 1000)
            if animationEnded:
                return




def quit():
    global animationEnded
    print("Quitting")
    animationEnded = True
    exit(0)

def set_color(r, g, b):
    aura.setColor(r, g, b)
    leds.setAllLeds(r, g, b)
    logitech.setColor(r, g, b)

def main():
    # tray_thread = Thread(target=setuptray, args=(get_animations(), set_animation, quit), daemon=False)
    # tray_thread.start()

    print("Oh oy")

    setuptray(get_animations(), set_animation, quit)

if __name__ == "__main__":
    main()


