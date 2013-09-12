from openexp.canvas import canvas
from openexp.keyboard import keyboard
# Create a blue and a yellow canvas
blue_canvas = canvas(exp, bgcolor='blue')
yellow_canvas = canvas(exp, bgcolor='yellow')
# Create a keyboard object
my_keyboard = keyboard(exp, timeout=0)
# Alternately present the blue and yellow canvas until
# a key is pressed.
while my_keyboard.get_key()[0] == None:
	blue_canvas.show()
	self.sleep(95)
	yellow_canvas.show()
	self.sleep(95) 
