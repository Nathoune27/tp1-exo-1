def on_button_pressed_a():
    global posX
    led.unplot(posX, 0)
    posX += -1
    led.plot(posX, 0)
    if posX < 0:
        posX = 0
        led.plot(posX, 0)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global posX
    led.unplot(posX, 0)
    posX += 1
    led.plot(posX, 0)
    if posX > 4:
        posX = 4
        led.plot(posX, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

posX = 0
posX = 0
N = 1
led.plot(posX, 0)

def on_forever():
    global posX, N
    basic.pause(1000)
    led.unplot(posX, 0)
    posX += N
    if posX == 0:
        N = 1
    elif posX == 4:
        N = -1
    led.plot(posX, 0)
basic.forever(on_forever)
