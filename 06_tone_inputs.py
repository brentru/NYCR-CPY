from adafruit_circuitplayground.express import cpx

# Amount of time to dwell on the tone, in seconds.
tone_duration = 0.5

# Musicial scale to frequency mappings
# from https://ptolemy.berkeley.edu/eecs20/week8/scale.html
a = 440
b_flat = 466
b = 494
c = 523
c_sharp = 554
d = 587
d_sharp = 622
e = 659
f = 698
f_sharp = 740
g = 784
a_flat = 831
a = 880

while True:
    if cpx.button_a:
        cpx.play_tone(a, 2)
    elif cpx.button_b:
        cpx.play_tone(b, 2)
    elif cpx.touch_a1:
        cpx.play_tone(c, 2)
    else:
        print('Waiting for input...')
