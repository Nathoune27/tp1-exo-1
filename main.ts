input.onButtonPressed(Button.A, function () {
    led.unplot(posX, 0)
    posX += -1
    led.plot(posX, 0)
    if (posX <= 0) {
        posX = 0
        led.plot(posX, 0)
    }
})
input.onButtonPressed(Button.B, function () {
    led.unplot(posX, 0)
    posX += 1
    led.plot(posX, 0)
    if (posX >= 4) {
        posX = 4
        led.plot(posX, 0)
    }
})
let posX = 0
posX = 0
let N = 1
led.plot(posX, 0)
basic.forever(function () {
    basic.pause(1000)
    led.unplot(posX, 0)
    posX += N
    if (posX <= 0) {
        N = 1
    } else if (posX >= 4) {
        N = -1
    }
    led.plot(posX, 0)
})
