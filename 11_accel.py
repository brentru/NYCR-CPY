import time
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print('X: {0}, Y: {1}, Z: {2}'.format(x, y, z))
    time.sleep(0.5)
