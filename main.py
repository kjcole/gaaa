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
keyboard = {"z": Note.C4,
            "s": Note.CSHARP4,
            "x": Note.D4,
            "d": Note.EB4,
            "c": Note.E4,
            "v": Note.F4,
            "g": Note.FSHARP4,
            "b": Note.G4,
            "h": Note.GSHARP4,
            "n": Note.A4,
            "j": Note.BB4,
            "m": Note.B4,
            ",": Note.C5,
            "l": Note.CSHARP5,
            ".": Note.D5,
            ";": Note.EB5,
            "/": Note.E5}
for index in range(88):
    scale.append(note)
    note = note * twelfth_root
# basic.pause(200)
# music.play_tone(tonic, music.beat(BeatFraction.WHOLE))
# print(tonic)

def on_forever():
    global ping
    global scale
    global keyboard
    ping = serial.read_buffer(0)
    if len(ping) > 0:
        basic.show_string("" + (ping.to_string()))
basic.forever(on_forever)
