# Prepare canvas 1 and 2
canvas1 = Canvas()
canvas1 += Text('This is the first canvas')
canvas2 = Canvas()
canvas2 += Text('This is the second canvas')
# Show canvas 1
t1 = canvas1.show()
# Sleep for 95 ms to get a 100 ms delay
clock.sleep(95)
# Show canvas 2
t2 = canvas2.show()
# The actual delay will be 100 ms, because stimulus
# preparation time is not included. This is good!
print('Actual delay: %s' % (t2-t1))
