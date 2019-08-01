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

# List of tones
tones = [a, b_flat, b, c,
            c_sharp, d, d_sharp, e,
            f, f_sharp, g, a_flat, a]

# Loop thru the list!
for tone in range(0, len(tones)):
    print('Playing tone: ', tone)
    cpx.play_tone(tone, tone_duration)
