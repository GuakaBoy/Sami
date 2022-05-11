input.onButtonPressed(Button.A, function () {
    for (let indeks = 0; indeks <= 2; indeks++) {
        music.playTone(262, music.beat(BeatFraction.Quarter))
        basic.showNumber(3 - indeks)
    }
    music.playTone(392, music.beat(BeatFraction.Whole))
    basic.showString("GO!")
    basic.showIcon(IconNames.Heart)
})
basic.showIcon(IconNames.Heart)
