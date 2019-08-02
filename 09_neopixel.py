import time
from adafruit_circuitplayground.express import cpx

while True:
    # Make it red!
    cpx.pixels.fill((255, 0, 0))
    time.sleep(5)
    # Make it green!
    cpx.pixels.fill((0, 255, 0))
    time.sleep(5)
    # Make it blue!
    cpx.pixels.fill((0, 0, 255))
    time.sleep(5)
