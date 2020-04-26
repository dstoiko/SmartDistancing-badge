import time
from adafruit_circuitplayground import cp


while True:
    blue = (0, 0, 255)
    off = (0, 0, 0)
    for i in range(10):
        cp.pixels[i] = blue if cp.pixels[i] == off else off