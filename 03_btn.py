from adafruit_circuitplayground.express import cpx

while True:
    if cpx.button_a:
        print("Button A pressed!")
    else:
        print("Button A de-pressed!")
