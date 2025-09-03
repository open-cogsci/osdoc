"""
# Instructions for Python in inline_script

- Stimulus preparation should be done in Prepare phase. Stimulus presentation, response collection, etc. should be done in Run phase. The Prepare and Run phase are tabs in the `inline_script` GUI item. When providing scripts to the user, use the START_PREPARE_PHASE and START_RUN_PHASE comments to clearly indicate what goes where.
- Canvas, Keyboard, FixDot, Rect, Circle, xy_random, responses, clock, etc. are always available and do not need to be imported.
- The code comments and the API documentation are for you. You don't need to include this verbatim in your responses.
- Variables defined in loop item are globals in inline_script

# Canvas class API Reference

Canvas is used for visual stimulus presentation. Create canvases, draw on them, and show them on screen. All drawing methods accept style keywords: `color`, `background_color`, `fill`, `penwidth`, `font_family`, `font_size`, `font_bold`, `font_italic`, `font_underline`, `html`. Colors can be names, hex, RGB tuples, or CSS strings.

## Examples
```python
# Basic drawing and display
canvas = Canvas()
canvas.fixdot(color='black')
canvas.circle(0, -100, 50, fill=True, color='red')
canvas.text('Hello', y=100, font_size=24)
timestamp = canvas.show()

# Named elements with interaction
canvas = Canvas()
canvas['target'] = Circle(100, 0, 30, color='green')
canvas['feedback'] = Text('Click the circle!')
canvas.show()
mouse = Mouse()
button, (x, y), time = mouse.get_click()
if (x, y) in canvas['target']:
    canvas['feedback'].text = 'Hit!'
    canvas.show()
```

## API
```python
Canvas(color=None, background_color=None, **style_args) -> Canvas
canvas.line(sx: float, sy: float, ex: float, ey: float, **style_args) -> None
canvas.arrow(sx: float, sy: float, ex: float, ey: float, body_length: float = 0.8, body_width: float = 0.5, head_width: float = 30, **style_args) -> None
canvas.rect(x: float, y: float, w: float, h: float, **style_args) -> None
canvas.circle(x: float, y: float, r: float, **style_args) -> None
canvas.ellipse(x: float, y: float, w: float, h: float, **style_args) -> None
canvas.polygon(vertices: List[Tuple[float, float]], **style_args) -> None
canvas.text(text: str, center: bool = True, x: float = None, y: float = None, max_width: float = None, **style_args) -> None
canvas.text_size(text: str, center: bool = True, max_width: float = None, **style_args) -> Tuple[float, float]
canvas.image(fname: str, center: bool = True, x: float = None, y: float = None, scale: float = None, rotation: float = None) -> None
canvas.fixdot(x: float = None, y: float = None, style: str = 'default', **style_args) -> None
canvas.gabor(x: float, y: float, orient: float, freq: float, env: str = 'gaussian', size: int = 96, stdev: float = 12, phase: float = 0, col1: str = 'white', col2: str = 'black', bgmode: str = 'avg') -> None
canvas.noise_patch(x: float, y: float, env: str = 'gaussian', size: int = 96, stdev: float = 12, col1: str = 'white', col2: str = 'black', bgmode: str = 'avg') -> None
canvas.show() -> float
canvas.prepare() -> None
canvas.clear(**style_args) -> None
canvas.elements_at(x: float, y: float) -> List[Element]
canvas.width: int
canvas.height: int
canvas.size: Tuple[int, int]
```

# Keyboard Class API Reference

Keyboard collects key presses from participants. Create instances with `Keyboard()`. Response keywords `timeout` and `keylist` can be passed to constructor or methods. Key names are case-insensitive and include letters, numbers, arrow keys ('up', 'down', 'left', 'right'), and special keys ('space', 'return', 'escape').

## Examples
```python
# Basic response collection
kb = Keyboard()
start_time = clock.time()
key, end_time = kb.get_key()
rt = end_time - start_time

# Multiple choice with timeout
kb = Keyboard(keylist=['1', '2', '3'], timeout=5000)
key, time = kb.get_key()
if key is None:
    print('No response!')

# Check modifiers
key, time = kb.get_key()
if 'shift' in kb.get_mods():
    print('Shift was pressed!')
```

## API
```python
Keyboard(timeout: int = None, keylist: List[str] = None) -> Keyboard
keyboard.get_key(**resp_args) -> Tuple[str, float]
keyboard.get_key_release(**resp_args) -> Tuple[str, float]
keyboard.get_mods() -> List[str]
keyboard.flush() -> bool
keyboard.timeout: int
keyboard.keylist: List[str]
```

# Mouse Class API Reference

Mouse collects mouse input including clicks, position, and button states. Create instances with `Mouse()`. Button numbers: 1=left, 2=middle, 3=right, 4=scroll up, 5=scroll down. Response keywords: `timeout`, `buttonlist`, `visible`.

## Examples
```python
# Get click with coordinates
mouse = Mouse()
button, (x, y), timestamp = mouse.get_click()
print(f'Clicked button {button} at ({x}, {y})')

# Track cursor movement
mouse = Mouse()
canvas = Canvas()
for t in clock.loop_for(5000):
    (x, y), timestamp = mouse.get_pos()
    canvas.clear()
    canvas.fixdot(x, y)
    canvas.show()
```

## API
```python
Mouse(timeout: int = None, buttonlist: List[int] = None) -> Mouse
mouse.get_click(**resp_args) -> Tuple[int, Tuple[float, float], float]
mouse.get_click_release(**resp_args) -> Tuple[int, Tuple[float, float], float]
mouse.get_pos() -> Tuple[Tuple[float, float], float]
mouse.get_pressed() -> Tuple[bool, bool, bool]
mouse.flush() -> bool
mouse.show_cursor(show: bool = True) -> None
mouse.set_pos(pos: Tuple[float, float] = (0, 0)) -> None
mouse.synonyms(button: Union[int, str]) -> List[Union[int, str]]
```

# Sampler Class API Reference

Sampler plays sound files from the file pool. Supports WAV, MP3, and OGG formats. Playback keywords: `volume` (0-1), `pitch` (speed multiplier), `pan` (-1 to 1), `duration` (ms), `fade_in` (ms), `block` (bool).

## Examples
```python
# Play a sound
sound = Sampler(pool['beep.wav'])
sound.play()

# Background music with control
music = Sampler(pool['music.ogg'], volume=0.3)
music.play(block=False)
clock.sleep(5000)
music.stop()

# Stereo and pitch effects
sound = Sampler(pool['tone.wav'])
sound.play(pan='left', pitch=1.5)
```

## API
```python
Sampler(src: str, **playback_args) -> Sampler
sampler.play(**playback_args) -> None
sampler.stop() -> None
sampler.pause() -> None
sampler.resume() -> None
sampler.is_playing() -> bool
sampler.wait() -> None
sampler.volume: float
sampler.pitch: float
sampler.pan: float
sampler.duration: float
sampler.fade_in: float
sampler.block: bool
```

# clock Object API Reference

The `clock` singleton provides timing functions. All times are in milliseconds.

## Examples
```python
# Measure reaction time
t0 = clock.time()
response = get_response()
rt = clock.time() - t0

# Create timed displays
fixation.show()
clock.sleep(500)
stimulus.show()

# Implement timeout
for ms in clock.loop_for(5000):
    if keyboard.get_key()[0] is not None:
        print(f'Response at {ms} ms')
        break
```

## API
```python
clock.time() -> float
clock.sleep(ms: float) -> None
clock.loop_for(ms: float, throttle: float = None, t0: float = None) -> Iterator[float]
clock.once_in_a_while(ms: float = 1000) -> bool
```

# log Object API Reference

The `log` singleton handles data logging to files. Write individual messages or all experiment variables.

## Examples
```python
# Write all variables (like logger item)
log.write_vars()

# Write specific variables
log.write_vars(['response_time', 'correct', 'subject_nr'])

# Write custom messages
log('Trial started')
log.write(f'RT: {rt}')
```

## API
```python
log.write(msg: str, newline: bool = True) -> None
log.write_vars(var_list: List[str] = None) -> None
log.open(path: str) -> None
log.close() -> None
log(msg: str) -> None
```

# responses Object API Reference

The `responses` singleton stores response history and calculates accuracy/RT feedback. Responses are stored in reverse chronological order (newest first). Adding responses automatically updates variables like `var.response`, `var.correct`, `var.acc`, and `var.avg_rt`.

## Examples
```python
# Add a response
kb = Keyboard()
start = clock.time()
key, end = kb.get_key()
correct = 1 if key == var.correct_response else 0
responses.add(response=key, correct=correct, response_time=end-start)

# Check performance
print(f"Accuracy: {var.acc}%")

# Analyze recent responses
for r in responses[:10]:
    if r.correct == 1 and r.response_time < 500:
        print("Fast correct!")
```

## API
```python
responses.add(response=None, correct: int = None, response_time: float = None, item: str = None, feedback: bool = True) -> None
responses.clear() -> None
responses.reset_feedback() -> None
len(responses) -> int
responses[index] -> Response
for response in responses: ...
response.response: Any
response.correct: int
response.response_time: float
response.item: str
response.feedback: bool
```

# pool Object API Reference

The `pool` singleton provides dict-like access to the file pool. Files can be in the temporary pool folder or the __pool__ subfolder of the experiment.

## Examples
```python
# Get file paths
image_path = pool['stimulus.png']
sound_path = pool['beep.wav']

# Check existence
if 'image.png' in pool:
    canvas.image(pool['image.png'])

# Add external file
pool.add('/home/user/photo.jpg', 'stimulus.jpg')
```

## API
```python
pool[filename: str] -> str
filename in pool -> bool
del pool[filename] -> None
len(pool) -> int
for filename in pool: ...
pool.add(path: str, new_name: str = None) -> None
pool.rename(old_path: str, new_path: str) -> None
pool.folder() -> str
pool.folders(include_fallback_folder: bool = True, include_experiment_path: bool = False) -> List[str]
pool.fallback_folder() -> str
pool.files() -> List[str]
pool.size() -> int
pool.in_folder(path: str) -> bool
```

# Miscellaneous Functions API Reference

# Synthesize a tone and return it as a Sampler object.
Synth(osc: Literal['sine','saw','square','white_noise'] = 'sine', freq: Union[int, str] = 440, length: int = 100, attack: int = 0, decay: int = 5, **playback_args) -> Sampler
# Return a copy of a sketchpad's canvas by the item name.
copy_sketchpad(name: str) -> Canvas
# Pause the experiment until externally resumed.
pause() -> None
# Register a function to be executed after the experiment ends (incl. crashes).
register_cleanup_function(fnc: Callable[[], None]) -> None
# Reset all feedback variables to their initial values.
reset_feedback() -> None
# Set the subject number and derived parity (even/odd).
set_subject_nr(nr: int) -> None
# Return True with probability p.
sometimes(p: float = 0.5) -> bool
# Generate n (x,y) coordinates arranged on a circle.
xy_circle(n: int, rho: float, phi0: float = 0, pole: Tuple[float, float] = (0, 0)) -> List[Tuple[float, float]]
# Compute Euclidean distance between two points.
xy_distance(x1: float, y1: float, x2: float, y2: float) -> float
# Convert polar (rho, phi° clockwise) to Cartesian (x,y).
xy_from_polar(rho: float, phi: float, pole: Tuple[float, float] = (0, 0)) -> Tuple[float, float]
# Generate (x,y) coordinates in a grid arrangement.
xy_grid(n: Union[int, Tuple[int, int]], spacing: Union[float, Tuple[float, float]], pole: Tuple[float, float] = (0, 0)) -> List[Tuple[float, float]]
# Generate n random (x,y) coordinates with a minimum inter-point distance.
xy_random(n: int, width: float, height: float, min_dist: float = 0, pole: Tuple[float, float] = (0, 0)) -> List[Tuple[float, float]]
# Convert Cartesian (x,y) to polar (rho, phi counterclockwise).
xy_to_polar(x: float, y: float, pole: Tuple[float, float] = (0, 0)) -> Tuple[float, float]
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