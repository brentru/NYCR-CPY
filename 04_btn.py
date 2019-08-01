from adafruit_circuitplayground.express import cpx

BUTTON_A = cpx.button_a
BUTTON_B = cpx.button_b

while True:
    if BUTTON_A:
        cpx.red_led = True
    elif BUTTON_B:
        cpx.red_led = False
    else:
        print("What button was that?")
