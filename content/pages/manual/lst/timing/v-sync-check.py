# Create a blue and a yellow canvas
blue_canvas = Canvas(bgcolor='blue')
yellow_canvas = Canvas(bgcolor='yellow')
# Create a keyboard object
my_keyboard = Keyboard(timeout=0)
# Alternately present the blue and yellow canvas until
# a key is pressed.
while my_keyboard.get_key()[0] is None:
    blue_canvas.show()
    clock.sleep(95)
    yellow_canvas.show()
    clock.sleep(95) 
