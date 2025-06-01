"""
# Instructions for Python in inline_script

- Stimulus preparation should be done in Prepare phase. Stimulus presentation, response collection, etc. should be done in Run phase. The Prepare and Run phase are tabs in the `inline_script` GUI item.
- Canvas, Keyboard, FixDot, Rect, Circle, xy_random, responses, clock, etc. are always available and do not need to be imported.
- The code comments are for you. You don't need to include them verbatim in your responses.
- Variables defined in loop item are globals in inline_script
"""
# START_PREPARE_PHASE
search_canvas = Canvas()  # Uppercase. Never pass exp parameter. Do not import from openexp.
search_canvas += FixDot()
for x, y in xy_random(6, width=200, height=200, min_dist=40):  # 6 random coordinates within a 200x200 area
    search_canvas += Rect(x=x-10, y=y+10, w=20, h=20, fill=True)
my_keyboard = Keyboard(keylist=['z', 'm'], timeout=2000)  # Uppercase. Never pass exp parameter. Only accept z or m. Timeout after 200 ms.
# END_PREPARE_PHASE
# START_RUN_PHASE
t0 = search_canvas.show()
key, t1 = my_keyboard.get_key()  # key is `None` when a timeout occurs
response_time = t1 - t0
correct = 1 if key == correct_response else 0  # Assumes that the expected (or correct) response is defined as `correct_response`
responses.add(response=key, correct=correct, response_time=response_time)  # Remember the response
# END_RUN_PHASE
# END_EXAMPLE

# START_EXAMPLE: circles in a circular arrangement followed by mouse click
# Related terms: visual search, additional singleton
# START_PREPARE_PHASE
import random
search_canvas = Canvas()
search_canvas += FixDot()
target_index = random.randint(0, 5)  # randomly select target position
for index, (x, y) in enumerate(xy_circle(6, rho=200)):  # 6 coordinates in a circle
    color = 'red' if index == target_index else 'blue'
    search_canvas += Rect(x=x - 10, y=y + 10, w=20, h=20, fill=True, color=color)
my_mouse = Mouse(timeout=2000)  # Uppercase. Never pass exp
# END_PREPARE_PHASE
# START_RUN_PHASE
t0 = search_canvas.show()
button, pos, t1 = my_mouse.get_click()  # button and pos are `None` when a timeout occurs
if pos is not None:
    x, y = pos  # unless a timeout occurred, pos is a (x, y) tuple that corresonds to the clicked location
else:
    x = y = None
# END_RUN_PHASE
# END_EXAMPLE

# START_EXAMPLE: bilateral display with images on left and right0
# START_PREPARE_PHASE
target_canvas = Canvas()
target_canvas['fixdot'] = FixDot()
target_canvas['left_img'] = Image(pool[left_img], x=-200)  # Assume that `left_img` and `right_img` contain names to files in the file pool. Use pool[] to look up the full path.
target_canvas['right_img'] = Image(pool[right_img], x=200)
# END_PREPARE_PHASE
# END_EXAMPLE

# START_EXAMPLE: cueing paradigm with delay between cue and target
# Related terms: spatial cuing, posner task, symbolic cuing
# START_PREPARE_PHASE
cue_canvas = Canvas()
if cue_side == 'left':  # assume that cue_side is defined elsewhere
    cue_canvas += Arrow(sx=20, sy=0, ex=-20, ey=0)
else:
    cue_canvas += Arrow(sx=-20, sy=0, ex=20, ey=0)
blank_canvas = Canvas()
blank_canvas += FixDot()  # blank canvas often has fixation dot
target_canvas = Canvas()
target_canvas += FixDot()
if cue == 'valid':  # Assume that cue is defined elsewhere. Valid means that the cue correctly indicates the target location
    target_x = -200 if cue_side == 'left' else 200
else:
    target_x = 200 if cue_side == 'left' else -200
target_canvas += Circle(x=target_x, y=0, r=20, fill=True)
# END_PREPARE_PHASE
# START_RUN_PHASE
cue_canvas.show()
clock.sleep(95)  # show cue for 100 ms. Duration rounded up to next display refresh
blank_canvas.show()
clock.sleep(195)  # show blank interstimulus interval (ISI) for 200 ms
target_canvas.show()
# END_RUN_PHASE
# END_EXAMPLE

# START_EXAMPLE: rapid serial visual presentation (RSVP) with dynamic display
# Related term: attentional blink
# Important note: when dynamically changing Canvas properties, timing may be off and should be checked
# START_RUN_PHASE
import string
import random
rsvp_canvas = Canvas()
rsvp_canvas['letter'] = Text(text='')  # Named Text element
letters = random.sample(string.ascii_uppercase, k=6)
t_list = []
for letter in letters:
    rsvp_canvas['letter'].text = letter  # Dynamically change text property
    t = rsvp_canvas.show()  # store presentation times for validation later
    t_list.append(t)
    clock.sleep(95)
# END_RUN_PHASE
# END_EXAMPLE

# START_EXAMPLE: play sound file
# Important note: mp3 is sometimes not supported
# START_PREPARE_PHASE
my_sound = Sampler(pool['my_sound.ogg'])  # Uppercase. Never pass exp parameter
# END_PREPARE_PHASE
# START_RUN_PHASE
my_sound.play()
# END_RUN_PHASE
# END_EXAMPLE

# START_EXAMPLE: play synthesized sound
# START_PREPARE_PHASE
my_sound = Synth(osc='sine', freq=220, length=100)  # Uppercase. Never pass exp parameter
# END_PREPARE_PHASE
# END_EXAMPLE

# START_EXAMPLE: draw circle where mouse is clicked
# START_RUN_PHASE
my_mouse = Mouse(visible=True)  # Uppercase. Never pass exp parameter. Do not import from openexp.
my_canvas = Canvas()
my_canvas['circle'] = Circle(x=0, y=0, r=10)  # Named Circle element
my_canvas.show()
while True:
    button, (x, y), click_time = my_mouse.get_click()
    my_canvas['circle'].x = x  # Dynamically change x property
    my_canvas['circle'].y = y
    my_canvas.show()
    if button == 3:  # 1: left click, 2: middle button, 3: right click
        break
# END_RUN_PHASE
# END_EXAMPLE
