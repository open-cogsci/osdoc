# Warning: This is an example of how you should *not*
# implement stimulus presentation in time-critical
# experiments.
#
# Prepare canvas 1 and show it
canvas1 = Canvas()
canvas1 += Text('This is the first canvas')
t1 = canvas1.show()
# Sleep for 95 ms to get a 100 ms delay
clock.sleep(95)
# Prepare canvas 2 and show it
canvas2 = Canvas()
canvas2 += Text('This is the second canvas')
t2 = canvas2.show()
# The actual delay will be more than 100 ms, because
# stimulus preparation time is included. This is bad!
print('Actual delay: %s' % (t2-t1))
