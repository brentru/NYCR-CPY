import time
from adafruit_circuitplayground.express import cpx

# Maximum temperature, in degrees C
MAX_TEMP = 24

# Minimum temperature, in degrees C
MIN_TEMP = 14

# NeoPixel Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

while True:
    # Take the temperature
    temp = cpx.temperature

    # Evaluate the temperature
    if temp > MAX_TEMP:
        cpx.play_tone(587, 5)
        cpx.pixels.fill(RED)
    elif temp < MIN_TEMP:
        cpx.play_tone(494, 5)
        cpx.pixels.fill(BLUE)
    else:
        cpx.pixels.fill(GREEN)

    # Let's wait a second before taking the temp again
    time.sleep(1)
