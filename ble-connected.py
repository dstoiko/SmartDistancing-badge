import time
from adafruit_circuitplayground import cp

time.sleep(3)
while True:
    blue = (0, 0, 255)
    off = (0, 0, 0)
    for i in range(10):
        if cp.pixels[i] == off:
            cp.pixels[i] = blue
    time.sleep(1)