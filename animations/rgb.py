max_t = 2

def process(t):
    if (t == 0):
        return [1000, 255, 0, 0]
    elif (t == 1):
        return [1000, 0, 255, 0]
    elif (t == 2):
        return [1000, 0, 0, 255]