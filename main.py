step = 10
test = 0

def on_forever():
    pass
basic.forever(on_forever)

basic.show_string(str(test))

def on_pin_pressed_p0():
    global test
    test += 1
    basic.show_string(str(test))
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_gesture_shake():
    basic.show_icon(IconNames.ANGRY, 1000)
    basic.show_string(str(test))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

# Clear

def on_pin_pressed_p1():
    global test
    test = 0
    basic.show_string(str(test))
input.on_pin_pressed(TouchPin.P1, on_pin_pressed_p1)
