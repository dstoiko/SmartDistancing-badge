import time
from adafruit_circuitplayground import cp


c = 0

while True:
    c = (c + 1) % 2
    color = [0, 0, 0]
    r = 0
    while r < 5:
        for i in range(1, 20):
            cp.pixels.brightness = i * 5 / 100
            color[c] = 255
            cp.pixels.fill(color)
        for i in range(1, 20):
            cp.pixels.brightness = (100 - i * 5) / 100
            color[c] = 255
            cp.pixels.fill(color)
        r += 1
    time.sleep(1)