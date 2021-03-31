/**
 * Written by Kevin Cole <ubuntourist@hacdc.org> 2021.03.25
 * 
 * Use screen or putty to generate "music" (and I use the term "music" loosely)
 */
let ivory = 0
let ping : Buffer = null
serial.redirectToUSB()
let tonic = 27.5
// 2.0 ** (1.0 / 12.0)
let twelfth_root = 1.0594630943592953
let note = tonic
let keyboard : any = {
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
for (let index = 0; index < 88; index++) {
    let scale: number[] = []
    scale.push(note)
    note = note * twelfth_root
}
// basic.pause(200)
// music.play_tone(tonic, music.beat(BeatFraction.WHOLE))
// print(tonic)
basic.forever(function () {
    ping = serial.readBuffer(0)
    if (ping.length > 0) {
        ivory = keyboard[ping.toString()]
        music.playTone(ivory, music.beat(BeatFraction.Half))
        serial.writeBuffer(ping)
        basic.showString("" + (ping.toString()))
    }
})
