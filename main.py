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
# unknown expression:  178
keyboard = {
    "z" : Note.C4,
    "s" : Note.CSharp4,
    "x" : Note.D4,
    "d" : Note.Eb4,
    "c" : Note.E4,
    "v" : Note.F4,
    "g" : Note.FSharp4,
    "b" : Note.G4,
    "h" : Note.GSharp4,
    "n" : Note.A4,
    "j" : Note.Bb4,
    "m" : Note.B4,
    "," : Note.C5,
    "l" : Note.CSharp5,
    "." : Note.D5,
    ";" : Note.Eb5,
    "/" : Note.E5,
}
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
        ivory = ping.to_string()
        music.play_tone(keyboard[ivory], music.beat(BeatFraction.EIGHTH))
        basic.show_string("" + ping.to_string())
basic.forever(on_forever)
