from adafruit_circuitplayground.express import cpx

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

# Try playing one of the tones above!
cpx.play_tone(a, 1)

# What happens if we increase the duration...
cpx.play_tone(c, 2)
