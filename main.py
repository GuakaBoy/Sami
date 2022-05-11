def on_button_pressed_a():
    for indeks in range(3):
        music.play_tone(262, music.beat(BeatFraction.QUARTER))
        basic.show_number(3 - indeks)
    music.play_tone(392, music.beat(BeatFraction.WHOLE))
    basic.show_string("GO!")
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.show_icon(IconNames.HEART)