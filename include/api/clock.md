<div class="ClassDoc YAMLDoc" id="clock" markdown="1">

# class __clock__

The `clock` offers basic time functions.

__Example__:

~~~ .python
# Get the timestamp before and after sleeping for 1000 ms
t0 = clock.time()
clock.sleep(1000)
t1 = clock.time()
time_passed = t1 - t0
print(u'This should be 1000: %s' % time_passed)
~~~

[TOC]

<div class="FunctionDoc YAMLDoc" id="clock-__init__" markdown="1">

## function __clock\.\_\_init\_\___\(experiment\)

Constructor to create a new `clock` object. You do not generally call this constructor directly, because a `clock` object is created automatically when the experiment is launched.

__Arguments:__

- `experiment` -- The experiment object.
	- Type: experiment

</div>

[clock.__init__]: #clock-__init__
[__init__]: #clock-__init__

<div class="FunctionDoc YAMLDoc" id="clock-sleep" markdown="1">

## function __clock\.sleep__\(ms\)

Sleeps (pauses) for a period.

__Example:__

~~~ .python
# Create two canvas objects ...
my_canvas1 = canvas()
my_canvas1.text(u'1')
my_canvas2 = canvas()
my_canvas2.text(u'2')
# ... and show them with 1 s in between
my_canvas1.show()
clock.sleep(1000)
my_canvas2.show()
~~~

__Arguments:__

- `ms` -- The number of milliseconds to sleep for.
	- Type: int, float

</div>

[clock.sleep]: #clock-sleep
[sleep]: #clock-sleep

<div class="FunctionDoc YAMLDoc" id="clock-time" markdown="1">

## function __clock\.time__\(\)

Gives a current timestamp in milliseconds. The absolute meaning of the timestamp (i.e. when it was 0) depends on the backend.

__Example:__

~~~ .python
t = clock.time()
print(u'The current time is %f' % t)
~~~

__Returns:__

A timestamp.

- Type: float

</div>

[clock.time]: #clock-time
[time]: #clock-time

</div>

[clock]: #clock

