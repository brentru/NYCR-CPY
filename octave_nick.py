import time
from adafruit_circuitplayground.express import cpx

a = 440
b_flat = 466
b = 494
c = 523

notes = [a, b_flat, b, c]

note = a

while True:
    for note_fu in range(0, len(notes)):
        print("Playing ", note_fu)
        note = note * pow(2, .083333333)
        cpx.play_tone(note, 1)
        time.sleep(0.5)