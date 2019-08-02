import time
from adafruit_circuitplayground.express import cpx

while True:
    print("Temperature C:", cpx.temperature)
    print("Temperature: {0}C".format(cpx.temperature))
    time.sleep(1)
