max_t = 510

def process(t):
    if(t < 255):
        return [20, 255, int(t / 2), 0]
    else:
        t -= 255
        t = 255 - t
        return [20, 255, int(t / 2), 0]