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
