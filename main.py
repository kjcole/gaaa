"""

Written by Kevin Cole <ubuntourist@hacdc.org> 2021.03.25

Use screen or putty to generate "music" (and I use the term "music" loosely)

"""
ping: Buffer = None
serial.redirect_to_usb()
tonic = 27.5
# 2.0 ** (1.0 / 12.0)
twelfth_root = 1.0594630943592953
note = tonic
scale = []
for index in range(88):
    scale.append(note)
    note = note * twelfth_root
# basic.pause(200)
# music.play_tone(tonic, music.beat(BeatFraction.WHOLE))
# print(tonic)

def on_forever():
    global ping
    ping = serial.read_buffer(0)
    if len(ping) > 0:
        basic.show_string("" + (ping.to_string()))
basic.forever(on_forever)
