import time
from adafruit_circuitplayground.express import cpx

# Time the LED is either on or off, in seconds
LED_SLEEP = 0.5

while True:
    cpx.red_led = True
    time.sleep(LED_SLEEP)
    cpx.red_led = False
    time.sleep(LED_SLEEP)
