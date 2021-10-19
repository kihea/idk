let step = 10;
let test = 0;

basic.forever(function () {
	
})
basic.showString(test.toString())
input.onPinPressed(TouchPin.P0, function() {
    test += 1;
    basic.showString(test.toString());
})
input.onGesture(Gesture.Shake, function() {
  basic.showIcon(IconNames.Angry, 1000);
  basic.showString(test.toString())
})

input.onPinPressed(TouchPin.P1, function() {
    test = 0;
    basic.showString(test.toString())
    //Clear
})