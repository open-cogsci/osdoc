# The numbers in this script assume a 100 Hz refresh rate! Adjust the numbers
# according to your monitor.
import numpy as np
# The interval for the black canvas. This will be 'rounded up' to 90 ms, or 9
# frames.
interval = 85
# The number of presentation cycles to test.
N = 100
# Create a black and a white canvas.
white_canvas = Canvas(bgcolor='white')
black_canvas = Canvas(bgcolor='black')
# Create an array to store the timestamps for the white display.
a_white = np.empty(N)
# Loop through the presentation cycles.
for i in range(N):
    # Present a white canvas for a single frame. I.e. do not wait at all after
    # the presentation.
    a_white[i] = white_canvas.show()
    # Present a black canvas for 9 frames. I.e. wait for 85 ms after the
    # presentation.
    black_canvas.show()
    clock.sleep(interval)
# Write the timestamps of the white displays to a file.
np.savetxt('timestamps.txt', a_white)
# For convenience, summarize the intervals between the white displays and print
# this to the debug window.
d_white = a_white[1:]-a_white[:-1]
print('M = %.2f, SD = %.2f' % (d_white.mean(), d_white.std()))
