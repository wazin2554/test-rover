def on_gesture_shake():
    music.play(music.create_sound_expression(WaveShape.SINE,
            500,
            500,
            255,
            0,
            5000,
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.IN_BACKGROUND)
    basic.show_leds("""
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_touched():
    music.play(music.builtin_playable_sound_effect(soundExpression.giggle),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.HEART)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_logo_pressed():
    music.play(music.tone_playable(440, music.beat(BeatFraction.DOUBLE)),
        music.PlaybackMode.UNTIL_DONE)
    basic.show_icon(IconNames.HAPPY)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

music.play(music.builtin_playable_sound_effect(soundExpression.yawn),
    music.PlaybackMode.IN_BACKGROUND)
basic.show_string("HI")
basic.show_leds("""
    . # . # .
    . # . # .
    # . . # #
    . # . # .
    . . # . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
