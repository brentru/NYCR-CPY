import time
from adafruit_circuitplayground.express import cpx

# Maximum temperature, in degrees C
MAX_TEMP = 24

# Minimum temperature, in degrees C
MIN_TEMP = 14

while True:
    # Take the temperature
    temp = cpx.temperature

    # Evaluate the temperature
    if temp > MAX_TEMP:
        cpx.play_tone(587, 5)
    elif temp < MIN_TEMP:
        cpx.play_tone(494, 5)

    # Let's wait a second before taking the temp again
    time.sleep(1)
