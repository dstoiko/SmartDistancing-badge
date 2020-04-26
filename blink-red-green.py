import time
from adafruit_circuitplayground import cp


c = 0

while True:
    c = (c + 1) % 2
    color = [0, 0, 0]
    if c == 1:
        color[c] = 255
        cp.pixels.fill(color)
        time.sleep(15)
    else:
        for r in range(10):
            color[c] = 255 * int(r % 2 == 0)
            cp.pixels.fill(color)
            time.sleep(0.5)
    time.sleep(1)