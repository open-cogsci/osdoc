<div class="ClassDoc YAMLDoc" markdown="1">

# instance __clock__

The `clock` object offers basic time functions. A `clock` object is
created automatically when the experiment starts.

__Example__

~~~ .python
# Get the timestamp before and after sleeping for 1000 ms
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
time_passed = t1 - t0
print(f'This should be 1000: {time_passed}')
~~~

[TOC]

## loop_for(ms, throttle=None, t0=None)

*New in v3.2.0*

An iterator that loops for a fixed time.

__Parameters__

- **ms**: The number of milliseconds to loop for.
- **throttle**: A period to sleep for in between each iteration.
- **t0**: A starting time. If `None`, the starting time is the moment at
which the iteration starts.

__Returns__

- 

__Example__

~~~ .python
for ms in clock.loop_for(100, throttle=10):
    print(ms)
~~~



## once_in_a_while(ms=1000)

*New in v3.2.0*

Periodically returns `True`. This is mostly useful
for executing
code (e.g. within a `for` loop) that should only be
executed once
in a while.

__Parameters__

- **ms**: The minimum waiting period.

__Returns__

- `True` after (at least) the minimum waiting period has
passed since
the last call to `Clock.once_in_a_while()`, or
`False` otherwise.

__Example__

~~~ .python
for i in range(1000000):
    if clock.once_in_a_while(ms=50):
        # Execute this code only once every 50 ms
        print(clock.time())
~~~



## sleep(ms)

Sleeps (pauses) for a period.


__Parameters__

- **ms**: The number of milliseconds to sleep for.

__Example__

~~~ .python
# Create two canvas objects ...
my_canvas1 = Canvas()
my_canvas1.text('1')
my_canvas2 = Canvas()
my_canvas2.text('2')
# ... and show them with 1 s in between
my_canvas1.show()
clock.sleep(1000)
my_canvas2.show()
~~~



## time()

Gives a current timestamp in milliseconds. The absolute meaning of
the timestamp (i.e. when it was 0) depends on the backend.



__Returns__

- A timestamp.

__Example__

~~~ .python
t = clock.time()
print(f'The current time is {t}')
~~~



</div>

