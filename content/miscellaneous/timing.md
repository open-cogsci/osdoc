---
layout: osdoc
title: Timing
group: Miscellaneous
permalink: /timing/
---

This page describes various issues related to timing and provides scripts that you can use to benchmark your own system. If you experience problems with timing, please take the time to read this page. Many issues are resolved by taking into account things such as stimulus preparation and the properties of your monitor.

:--
cmd: overview
--:
	
## Is OpenSesame capable of millisecond precision timing?

The short answer is: yes. The long answer is the rest of this page.
	
## Important considerations for time-critical experiments

### Understanding your monitor

Computer monitors refresh periodically. For example, if the refresh rate of your monitor is 100 Hz, the display is refreshed every 10 ms (1000 ms / 100 Hz). This means that a visual stimulus is always presented for a duration that is a multiple of 10 ms, and you will not be able to present a stimulus for, say, 5 or 37 ms.

In the video below you can see what a monitor refresh looks like in slow motion. On CRT monitors (i.e. non-flatscreen, center) the refresh is a single pixel that traces across the monitor from left to right and top to bottom. Therefore, only one pixel is lighted at a time, which is why CRT monitors flicker slightly. On LCD or TFT monitors (flatscreen, left and right) the refresh is a 'flood fill' from top to bottom. Therefore, LCD and TFT monitors do not flicker. (Unless you present a flickering stimulus, of course.)

:--
cmd: video
src: vimeo
id: 24216910
width: 640
height: 240
caption: A slow-motion video of the refresh cycle on CRT (center) and LCD/ TFT monitors. Video courtesy of Jarik den Hartog and the VU University Amsterdam technical support staff.
--:

If a new stimulus display is presented while the refresh cycle is halfway, you will observe 'tearing'. That is, the upper half of the monitor shows the old display, while the lower part shows the new display. This is generally considered undesirable, and therefore a new display should be presented at the exact moment that the refresh cycle starts from the top. This is called 'synchronization to the vertical refresh' or simply 'v-sync'. When v-sync is enabled, tearing is no longer visible, because the tear coincides with the upper edge of the monitor. However, and this appears to be a little recognized fact, v-sync does not change anything about the fact that the monitor will always, for some time, present both the old and the new display.

Another important concept is that of 'blocking on the vertical retrace' or the 'blocking flip'. Usually, when you send a command to show a new display, the computer will accept this command right away and put the to-be-shown display in a queue. However, the display may not actually appear on the monitor for some time, typically until the start of the next refresh cycle (assuming that v-sync is enabled). Therefore, you don't know exactly when the display has appeared and your timestamps will not be exact. To get around this issue, some software employs a 'blocking flip'. This basically means that when you send a command to show a new display, the computer will freeze until the display actually appears. This allows you to get very accurate display timestamps, at the cost of a significant performance hit due to the computer being frozen for much of the time. But for the purpose of experiments, a blocking flip is generally considered the optimal strategy.

Finally, LCD monitors may suffer from 'input lag'. This means that there is an extra and sometimes variable delay between the moment that the computer 'thinks' that a display appears, and the moment that the display actually appears. This delay results from various forms of digital processing that are performed by the monitor. As far as I know, input lag is not something that can be resolved programmatically, and you should avoid monitors with significant input lag for time-critical experiments.

For a related discussion, see:

- <http://docs.expyriment.org/Timing.html#visual>

### Making the refresh deadline

Imagine that you arrive at a train station at 10:30. Your train leaves at 11:00, which gives you exactly 30 minutes to get a cup of coffee. However, when you have coffee for exactly 30 minutes, you will arrive at the track just in time to see your train depart and you will have to wait for the next train. Therefore, if you have 30 minutes waiting time, you should have a coffee for slightly less than 30 minutes. 25 minutes, for example.

The situation is analogous when specifying intervals for visual-stimulus presentation. Let's say that you have a 100 Hz monitor (so 1 refresh every 10 ms) and want to present a target stimulus for 100 ms, followed by a mask. Your first inclination might be to specify an interval of 100 ms between the target and the mask, because that's after all what you want. However, specifying an interval of exactly 100 ms will likely cause the mask to 'miss the refresh deadline', and the mask will be presented only on the next refresh cycle, which is 10 ms later (assuming that v-sync is enabled). So if you specify an interval of 100 ms, you will in most cases end up with an interval of 110 ms! The solution is simple: You should specify an interval that is slightly shorter than what you are aiming for, such as 95 ms. Don't worry about the interval being too short, because on a 100 Hz monitor the interval between two stimulus displays is necessarily a multiple of 10 ms. Therefore, 95 ms will become 100 ms (10 frames), 1 ms will become 10 ms (1 frame), etc. Phrased differently, intervals will be rounded up (but never rounded down!) to the nearest interval that is consistent with your monitor's refresh rate.

### Taking into account stimulus-preparation time/ the prepare-run structure

If you care about accurate timing during visual-stimulus presentation, you should prepare your stimuli in advance. That way, you will not get any unpredictable delays due to stimulus preparation during the time-critical parts of your experiment.

Let's first consider a script (you can paste this into an `inline_script` item) that includes stimulus-preparation time in the interval between `canvas1` and `canvas2`. The interval that is specified is 95 ms, so--taking into account the 'rounding up' rule--you would expect an interval of 100 ms on my 60 Hz monitor. However, on my test system the script below results in an interval of 150 ms, which corresponds to 9 frames on a 60 Hz monitor. This is an unexpected delay of 50 ms, or 3 frames, due to the preparation of `canvas2`.

{% highlight python %}
# Warning: This is an example of how you should *not*
# implement stimulus presentation in time-critical
# experiments.
from openexp.canvas import canvas
# Prepare canvas 1 and show it
canvas1 = canvas(exp)
canvas1.text('This is the first canvas')
t1 = canvas1.show()
# Sleep for 95 ms to get a 100 ms delay
self.sleep(95)
# Prepare canvas 2 and show it
canvas2 = canvas(exp)
canvas2.text('This is the second canvas')
t2 = canvas2.show()
# The actual delay will be more than 100 ms, because
# stimulus preparation time is included. This is bad!
print 'Actual delay: %s' % (t2-t1)
{% endhighlight %}

Now let's consider a simple variation of the script above. This time, we first prepare both `canvas1` and `canvas2` and only afterwards present them. On my test system, this results in a consistent 100 ms interval, just as it should!

{% highlight python %}
# Prepare canvas 1 and 2
canvas1 = canvas(exp)
canvas1.text('This is the first canvas')
canvas2 = canvas(exp)
canvas2.text('This is the second canvas')
# Show canvas 1
t1 = canvas1.show()
# Sleep for 95 ms to get a 100 ms delay
self.sleep(95)
# Show canvas 2
t2 = canvas2.show()
# The actual delay will be 100 ms, because stimulus
# preparation time is not included. This is good!
print 'Actual delay: %s' % (t2-t1)
{% endhighlight %}

When using the graphical interface, the same considerations apply, but OpenSesame helps you by automatically handling most of the stimulus preparation in advance. However, you have to take into account that this preparation occurs at the level of `sequence` items, and not at the level of `loop` items. Practically speaking, this means that the timing *within* a `sequence` is not confounded by stimulus-preparation time. But the timing *between* sequences is.

To make this more concrete, let's consider the structure shown below. Suppose that the duration of `sketchpad` is set to 95 ms, thus aiming for a 100 ms duration, or 6 frames on a 60 Hz monitor. On my test system the actual duration is 133 ms, or 8 frames, because the timing is confounded by preparation of the `sketchpad` item, which occurs each time that that the sequence is executed. So this is an example of how you should *not* implement time-critical parts of your experiment.

:--
cmd: figure
src: stimulus-preparation-incorrect.png
caption: An example of an experimental structure in which the timing between successive presentations of `sketchpad` is confounded by stimulus-preparation time.
--:
	
Now let's consider the structure shown below. Suppose that the duration of `sketchpad1` is set to 95 ms, thus aiming for a 100 ms interval between `sketchpad1` and `sketchpad2`. In this case, both items are shown as part of the same `sequence` and the timing will not be confounded by stimulus-preparation time. On my test system the actual interval between `sketchpad1` and `sketchpad2` is therefore indeed 100 ms, or 6 frames on a 60 Hz monitor.

Note that this only applies to the interval between `sketchpad1` and `sketchpad2`, because they are executed in that order as part of the same sequence. The interval between `sketchpad2` on run *i* and `sketchpad1` on run *i+1* is again confounded by stimulus-preparation time.

:--
cmd: figure
src: stimulus-preparation-correct.png
caption: An example of an experimental structure in which the timing between the presentation of `sketchpad1` and `sketchpad2` is not confounded by stimulus-preparation time.
--:

For more information, see:

- [usage/prepare-run]

### Differences between back-ends

OpenSesame is not tied to one specific way of controlling the display, system timer, etc. Therefore, OpenSesame *per se* does not have specific timing properties, because these depend on the back-end that is used. The performance of the various back-ends are not perfectly correlated: It is possible (although not typical) that on some system the [psycho] back-end works best, whereas on another system the [xpyriment] back-end works best. Therefore, one of the great things about OpenSesame is that you can choose which back-end works best for you!

In general, the [xpyriment] and [psycho] back-ends are preferable for time-critical experiments, because they use a blocking flip, as described above. On the other hand, the [legacy] back-end is slightly more stable and also considerably faster when using [forms].

Under normal circumstances the three current OpenSesame back-ends have the following properties:

|__Back-end__	|__V-sync__	|__Blocking flip__	|
|[legacy]		|yes		|no					|
|[xpyriment]	|yes		|yes				|
|[psycho]		|yes		|yes				|

See also:

- [back-ends]

## Benchmark results and tips for testing your own system

### Checking whether v-sync is enabled

As described above, the presentation of a new display should ideally coincide with the start of a new refresh cycle (i.e. 'v-sync'). You can test whether this is the case quite easily by presenting displays of different colors in rapid alternation. If v-sync is not enabled you will clearly observe horizontal lines running across the monitor (i.e. 'tearing'). To run this test, paste the following script into an `inline_script` item:

{% highlight python %}
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
{% endhighlight %}

### Testing consistency of timing and timestamp accuracy

Timing is consistent when you can present visual stimuli over and over again with the same timing. Timestamps are accurate when they accurately reflect when visual stimuli appear on the monitor. The script below allows you to check timing consistency and timestamp accuracy. This test can be performed both with and without an external photodiode, although the use of a photodiode provides extra verification.

In the script, a white canvas is presented for a single frame, followed by a black canvas for a longer duration. The script logs when the white canvas is presented. Based on the refresh rate of your monitor, you can deduce what the interval between two successive presentations of the white canvas should be. As you can read in the code comments, with the listed values and assuming a 100 Hz monitor, there should be an interval of 100 ms between successive presentations of the white canvas. This interval should be constant, ideally with a standard deviation of less than 1 ms.

There are a number of things that can go wrong here:

- *Symptoms:* There is a large standard deviation in the reported intervals (> 5 ms). If you look at the individual timestamps, you see that they vary more-or-less randomly and do not reflect the refresh rate of the monitor. For example, if you have a 100 Hz monitor, you may observe intervals such as 95, 93, 107, 101, etc. 
	- *Possible cause:* OpenSesame does not use a blocking flip. This is normal for the [legacy] back-end, but indicates a problem with the [xpyriment] and [psycho] back-ends.
- *Symptoms:* There is a large standard deviation in the reported intervals (> 5 ms). If you look at the individual timestamps, you see that they reflect the refresh rate of the monitor. For example, if you have a 100 Hz monitor, you observe intervals such as 90, 100, 110, 90, etc.
	- *Possible cause:* OpenSesame has trouble generating and presenting the stimuli in time. This may be due to too many stimuli that are preloaded or an old graphics card. It may also indicate that stimulus-preparation time is included in the interval.
- *Symptoms:* There is a very small standard deviation in the reported intervals (< 1 ms), but the intervals are consistently too high. The reported interval reflects the refresh rate of the monitor. For example, if you have a 100 Hz monitor, you observe an interval of 120 ms, while you were aiming for 100 ms.
	- *Possible cause:* OpenSesame has trouble generating and presenting the stimuli in time. This may be due to too many stimuli that are preloaded or an old graphics card. It may also indicate that stimulus-preparation time is included in the interval.

Generally speaking, problems with timing will be exposed when you run the script below and inspect the timestamps as reported by OpenSesame. However, the best way to be absolutely sure that your system is running smoothly is to measure the onsets of the white frame using an external photodiode as well. The idea behind this is that the photodiode will be triggered every time that a white display is presented. This provides you with a separate list of timestamps, which you can compare with the timestamps as reported by OpenSesame. Needless to say, these should be in very close agreement. Certain problems, such as the TFT input lag discussed above, may only come out when you measure timestamps using a photodiode.

{% highlight python %}
from openexp.canvas import canvas
import numpy as np
# On a 100 Hz monitor, a 85 ms interval will be 'rounded up'
# to 90 ms, or 9 frames. This is the presentation duration for
# the black canvas. The white canvas will be presented for
# a single frame, or 10 ms on a 100 Hz monitor. So the total
# presentation cycle should be 100 ms, again assuming a
# 100 Hz monitor and an interval of 85. These numbers may be
# different for different refresh rates!
interval = 85
# The number of presentation cycles
N = 100
# Create a black and a white canvas
white_canvas = canvas(exp, bgcolor='white')
black_canvas = canvas(exp, bgcolor='black')
# Create an array to store the timestamps of the white display.
a_white = np.empty(N)
# Loop through the presentation cycles
for i in range(N):
	# Present a white canvas for a single frame, which corresponds to
	# 10 ms on a 100 Hz monitor. This white canvas can be used to
	# trigger a photodiode, so you can record timestamps on an 
	# external device and compare these with the timestamps reported 
	# by OpenSesame.
	a_white[i] = white_canvas.show()
	# Present a black canvas for a longer interval, as specified
	# above. We don't record the timestamps for the black canvas
	# here (although you could), because the timestamps of the 
	# white display are sufficient.
	black_canvas.show()
	self.sleep(interval)
# Write the timestamps to a file
np.savetxt('timestamps.txt', a_white)
{% endhighlight %}

I ran this script on Ubuntu 12.04 using the [xpyriment] back-end (*N* = 1000). The refresh rate of the monitor was 85 Hz and I set the interval such that the total presentation cycle should take 200 ms: 1 white frame (11.8 ms) followed by 16 black frames (188.2 ms). I measured the onsets of the white frame also using a photodiode.

As you can see in the table below, there is very close agreement between the photiodiode measurements and the timestamps reported by OpenSesame. According to both measurements, the mean interval between two white frames was 199.94 ms. There is also very little variation and no frames were dropped in the entire run.

|**Source**	|*M*	|*SD*	|*Min*	|*Max*	|
|Photodiode	|199.94	|0.02	|199.88	|200.00	|
|OpenSesame |199.94	|0.45	|198.00	|201.00	|

In the figure below you can see display timestamps as reported by OpenSesame plotted against the photiodiode measurements during the first 2 seconds of the test run. Again, the close agreement is clear.

:--
cmd: figure
src: duration-benchmark-xpyriment.png
caption: Photodiode timestamps as a function of self-reported timestamps. Tested on Ubuntu 12.04 with the [xpyriment] back-end.
--:

### Checking for clock drift in high-resolution timers (Windows only)

Under Windows, there are two ways to obtain the system time. The Windows *Performance Query Counter* (QPC) API reportedly provides the highest accuracy. The CPU *Time Stamp Counter* (TSC), which relies on the number of clock ticks since the CPU started running, is somewhat less accurate. Of course, these two timers should be in sync with each other. A significant deviation between the QPC and TSC indicates a problem with your system's internal timer. Currently, only the [psycho] back-end makes use of the QPC. The [legacy] and [xpyriment] back-ends rely on the TSC.

The script below determines a drift value that indicates how much the QPC and TSC diverge. This value should be very close to 1, meaning no divergence. Values higher than 1 indicate that the TSC runs faster than the QPC. You can run this script directly in a Python interpreter or by pasting it in an `inline_script` item (in which case you may need to comment out the references to `matplotlib`, because this library is not included in all OpenSesame packages).

{% highlight python %}
from time import time as getTickTime, sleep as tickSleep
from ctypes import byref, c_int64, windll
from matplotlib import pyplot as plt
import numpy as np

# The number of samples to get
N = 1000
# The sleep period between samples (in sec.)
sleep = .1

def getQPCTime():

	"""
	Uses the Windows QueryPerformanceFrequency API to get the system time. This
	implements the high-resolution timer as used for example by PsychoPy and
	PsychoPhysics toolbox.

	Returns:
	A timestamp (float)
	"""

	_winQPC(byref(_fcounter))
	return  _fcounter.value/_qpfreq

# Complicated ctypes magic to initialize the Windows QueryPerformanceFrequency
# API. Adapted from the psychopy.core.clock source code.
_fcounter = c_int64()
_qpfreq = c_int64()
windll.Kernel32.QueryPerformanceFrequency(byref(_qpfreq))
_qpfreq = float(_qpfreq.value)
_winQPC = windll.Kernel32.QueryPerformanceCounter
# Create empty numpy arrays to store the results
aQPC = np.empty(N, dtype=float)
aTick = np.empty(N, dtype=float)
aDrift = np.empty(N, dtype=float)
# Wait for a minute to allow the Python interpreter to settle down.
tickSleep(1)
# Get the onset timestamps for the timers.
onsetQPCTime, onsetTickTime = getQPCTime(), getTickTime()
# Repeatedly check both timers
print "QPC\ttick\tdrift"
for i in range(N):
	# Get the QPC time and the tickTime
	QPCTime = getQPCTime()
	tickTime = getTickTime()
	# Subtract the onset time
	QPCTime -= onsetQPCTime
	tickTime -= onsetTickTime
	# Determine the drift, such that > 1 is a relatively slowed QPC timer.
	drift = tickTime / QPCTime
	# Sleep to avoid too many samples.
	tickSleep(sleep)
	# Print output
	print "%.4f\t%.4f\t%.4f" % (QPCTime, tickTime, drift)
	# Save the results in the arrays
	aQPC[i] = QPCTime
	aTick[i] = tickTime
	aDrift[i] = drift
# The first drift sample should be discarded
aDrift = aDrift[1:]
# Create a nice plot of the results
plt.figure(figsize=(6.4, 3.2))
plt.rc('font', size=10)
plt.subplots_adjust(wspace=.4, bottom=.2)
plt.subplot(121)
plt.plot(aQPC, color='#f57900', label='QPC timer')
plt.plot(aTick, color='#3465a4', label='Tick timer')
plt.xlabel('Sample')
plt.ylabel('Timestamp (sec)')
plt.legend(loc='upper left')
plt.subplot(122)
plt.plot(aDrift, color='#3465a4', label='Timer drift')
plt.axhline(1, linestyle='--', color='black')
plt.xlabel('Sample')
plt.ylabel('tick / QPC')
plt.savefig('systemTimerDrift.png')
plt.savefig('systemTimerDrift.svg')
plt.show()
{% endhighlight %}

I tested this script on two systems. On the first system, shown in the figure below, there was a slight drift of about 1.2%. Importantly, this drift was not consistently present. On another occasion the same system did not exhibit any drift at all. The reason for this inconsistency is unclear.

:--
cmd: figure
src: clock-drift-system1.png
caption: Windows XP, HP Compaq dc7900, Intel Core 2 Quad Q9400 @ 2.66Ghz, 3GB
--:
	
The second system, shown in the figure below, showed no drift at all, at least not during this particular session.

:--
cmd: figure
src: clock-drift-system2.png
caption: Windows 7, Acer Aspire V5-171, Intel Core I3-2365M @ 1.4Ghz, 6GB
--:

This issue is described in more detail on the Psychophysics Toolbox website.

- <http://docs.psychtoolbox.org/GetSecsTest>

## Expyriment benchmarks and test suite

A very nice set of benchmarks is available on the Expyriment website. This information is applicable to OpenSesame experiments using the [xpyriment] back-end.

- <http://docs.expyriment.org/Timing.html>

Expyriment includes a very useful test suite. You can launch this test suite by running the `test_suite.opensesame` example experiment, or by adding a simple inline_script to your experiment with the following lines of code:
	
{% highlight python %}
import expyriment
expyriment.control.run_test_suite()
{% endhighlight %}

For more information, please visit:

- <http://docs.expyriment.org/Testsuite.html>

## PsychoPy benchmarks and timing-related information

Some information about timing is available on the PsychoPy documentation site. This information is applicable to OpenSesame experiments using the [psycho] back-end.

- <http://www.psychopy.org/general/timing/timing.html>

[psycho]: /back-ends/xpyriment/
[xpyriment]: /back-ends/xpyriment/
[legacy]: /back-ends/legacy/
[miscellaneous/clock-drift]: /miscellaneous/clock-drift
[usage/prepare-run]: /usage/prepare-run
[back-ends]: /back-ends
[forms]: /forms