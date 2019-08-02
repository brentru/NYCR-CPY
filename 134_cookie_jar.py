import time
from adafruit_circuitplayground.express import cpx

# Bright light
bright_light_level = 900

light_level = 0
while True:
    light_level = cpx.light
    print("Light Level:", cpx.light)
    if light_level > bright_light_level:
        print('JAR OPEN!!')
        cpx.play_tone(587, 10)
    else:
        print('Jar closed')