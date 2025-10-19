input.onGesture(Gesture.Shake, function () {
    music.play(music.createSoundExpression(WaveShape.Sine, 500, 500, 255, 0, 5000, SoundExpressionEffect.Vibrato, InterpolationCurve.Linear), music.PlaybackMode.InBackground)
    basic.showLeds(`
        . # . # .
        . # . # .
        . . . . .
        . # . # .
        # . # . #
        `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    music.play(music.builtinPlayableSoundEffect(soundExpression.giggle), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Heart)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    music.play(music.tonePlayable(392, music.beat(BeatFraction.Double)), music.PlaybackMode.UntilDone)
    basic.showIcon(IconNames.Happy)
})
music.play(music.builtinPlayableSoundEffect(soundExpression.yawn), music.PlaybackMode.InBackground)
basic.showString("HI")
basic.showLeds(`
    . # . # .
    . . . . .
    # . . . #
    . # . # .
    . . # . .
    `)
basic.forever(function () {
	
})
