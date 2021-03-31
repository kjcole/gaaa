/** 

Written by Kevin Cole <ubuntourist@hacdc.org> 2021.03.25

Use screen or putty to generate "music" (and I use the term "music" loosely)


 */
let ping : Buffer = null
serial.redirectToUSB()
let tonic = 27.5
//  2.0 ** (1.0 / 12.0)
let twelfth_root = 1.0594630943592953
let note = tonic
let scale = []
for (let index = 0; index < 88; index++) {
    scale.push(note)
    note = note * twelfth_root
}
//  basic.pause(200)
//  music.play_tone(tonic, music.beat(BeatFraction.WHOLE))
//  print(tonic)
basic.forever(function on_forever() {
    
    ping = serial.readBuffer(0)
    if (ping.length > 0) {
        basic.showString("" + ping.toString())
    }
    
})
