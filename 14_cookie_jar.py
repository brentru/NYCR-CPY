import time
from adafruit_circuitplayground.express import cpx

def flash_blink():
    for i in range(0, 10)
    cpx.play_tone(578, 1)
    cpx.pixels.fill((255, 0, 0))
    time.sleep(0.2)
    cpx.play_tone(578, 1)
    cpx.pixels.fill((0, 0, 0))
    time.sleep(0.2)

# Bright light
bright_light_level = 900

light_level = 0
while True:
    light_level = cpx.light
    print("Light Level:", cpx.light)
    if light_level > bright_light_level:
        print('JAR OPEN!!')
        flash_blink()
    else:
        print('Jar closed')