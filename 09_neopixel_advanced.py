import time
from adafruit_circuitplayground.express import cpx

while True:
    # Make pixel 1 red!
    cpx.pixels[0] = (255, 0, 0)
    time.sleep(5)
    # Make pixel 2 green!
    cpx.pixels[1] = (0, 255, 0)
    time.sleep(5)
    # Make pixel 3 blue!
    cpx.pixels[2] = (255, 0, 0)
    time.sleep(5)
