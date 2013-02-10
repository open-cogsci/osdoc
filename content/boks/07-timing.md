---
layout: osdoc
title: Timing
group: Boks
permalink: /timing/
level: 1
sortkey: 0019.007
show: True
---

##### The Boks and documentation below is under development.

Overview
--------

- [Communication](#communication)
- [Precision vs accuracy](#precision-vs-accuracy)
- [Bencmarks](#benchmarks)
- [Test your own system](#test-yourself)

Communication {#communication}
-------------

Most response boxes send a continuous stream of characters, and the response time is determined by the moment at which the computer receives a particular character that corresponds to a button press. In contrast, the Boks uses a communication protocol that has been specifically designed to address the primary challenge to temporal precision and accuracy: The delays that occur in sending and receiving data via the USB port.

![](/img/fig/fig19.7.1.png)

In the figure above, you can see a schematic of the communication that occurs between the computer and the Boks during the collection of a button press.

- First, the computer notes the current time as `start_time` (based on the computer clock) and sends a `CMD_SET_T1`. This makes the Arduino also note the current time as `T1` (based on the Arduino clock). This initial step, in which the clocks of the computer and the Arduino are synchronized, is where the potential for temporal error is. In a perfect world, `T1` and `start_time` would be set at the exact same moment, in which case the response time measurements would have essentially zero error. In reality, `T1` will be set slightly after `start_time`, as indicated by a slightly tilted arrow in the figure. However, our tests suggest that this delay is extremely small, on the order of tens of microseconds (depending on the system).
- Next, the computer sends a `CMD_WAIT_PRESS` (or `CMD_WAIT_RELEASE`) signal, which will cause the Arduino to go into a response collection loop.
- When the Arduino detects a response, it immediately notes the current time as `T2` (based on the Arduino clock). Then it sends the button number back to the computer.
- Once the computer has received the button number, it sends a `CMD_GET_TD` signal. This will cause the Arduino to respond by sending `TD` (`=T2-T1`).
- The computer determines the response time based on `start_time` and `TD`: `end_time = start_time + TD`.

The upshot of this approach is that the temporal error of the response time measurements is far smaller than the overall communication time. It also means that one should use the response timestamp as reported by the Boks. That is, this is good ...

{% highlight python %}
t1 = exp.time()
button, t2 = boks.get_button_press()
response_time = t2-t1
{% endhighlight %}

... but this is not ...

{% highlight python %}
t1 = exp.time()
button = boks.get_button_press()[0]
t2 = exp.time()
response_time = t2-t1
{% endhighlight %}

Precision vs accuracy {#precision-vs-accuracy}
---------------------

As explained on [Wikipedia][wikipedia-precision], there is a conceptual difference between the 'precision' and the 'accuracy' of a measurement. The accuracy of a system reflects the extent to which the measured value corresponds to the true value, i.e. is unbiased. The precision of a system reflects the extent to which measurements are constant, i.e. have little variability.

In virtually all circumstances, the temporal precision of response measurements is far more important than the precision, because variability is what reduces statistical power. This situation is fortunate, because establishing the precision of the Boks is easier than establishing its accuracy. The variability in the minimum response latency is a test of *precision*, and is in the order of microseconds (on our reference system), The absolute error in photodiode responses to a white display is a test of *accuracy* (of both the Boks and display presentation), and is in the the order of hundreds of microseconds (on our reference system).

Benchmarks {#benchmarks}
----------

### Minimum response latency

The graph below shows the response time to a continuously pressed button, which indicates the minimum response latency. In relation to the schematic shown above, these results reflect the interval between `T1` and the start of the `WAIT_PRESS` loop.

As you can see, the minimum response latency is much lower on Kubuntu Linux 12.04 than on Windows XP. The results from Windows 7 resemble those from Kubuntu (not shown).

*Results from Kubuntu 12.04*[^system-1]

![](/img/fig/fig19.7.2.png)

*Results from Windows XP*[^system-2]

![](/img/fig/fig19.7.3.png)

### Photodiode test

Another important test is to measure the lowest possible response time that the button box can offer. This can be tested quite easily, using the photodiode that is integrated into the bottom of the Boks (cf. Mathôt et al., 2012, BRM), by holding the photodiode to the top-left of the monitor and measuring the response time to a white display. This test measures the error in the whole cycle from display presentation to response collection. On this system, the minimum response time is low (< 1ms) and constant (*SD* < 200ms). 

You also see that the results depend on the back-end that is used: The legacy back-end performs quite poorly, with high and variable response times. The temporal jitter that you observe with the legacy back-end is not due to the Boks, but the fact that the legacy back-end does not use 'blocking' display presentation and thus has less precise and accurate display timestamps.

Finally, a keen eye may notice response times are actually slightly lower than the minimum response latency shown in the graph above (Windows XP results). This is probably because the computer overestimates the timestamp of the display presentation, and the Boks underestimates the response time (as shown in the schematic above). This introduces a bias (thus not affecting precision) that decreases response times. Since the ideal response time in this test is 0µs, this bias (marginally) boosts accuracy.

*Results from Windows XP*[^system-3]

|Back-end	|Mean (µs)	|Std. dev. (µs)	|
|xpyriment	|930 		|123			|
|psycho		|548 		|123			|
|legacy		|3942		|2727			|

![](/img/fig/fig19.7.4.png)

### Noise

The Boks should not have any noise. That is, the Boks should report the actual state of a button 100% of the time. You can test this with the `noise` component of the `unittest` script (see below), which will ask you to press and release the buttons one by one, while it continuously polls the button state of the Boks. The output of the `noise` test should look like the following, where the number of non-matches is 0.

	Press button 1
	Match = 10000, Non-match = 0
	Release button 1
	Match = 10000, Non-match = 0
	Press button 2
	Match = 10000, Non-match = 0
	Release button 2
	Match = 10000, Non-match = 0

Test your own system {#test-yourself}
--------------------

You can test the Boks your own system using the `unittest` script included with the Boks source. You can run the full test suite with the following command (the command line arguments specify which tests should be performed):

	./unittest led buttons photodiode latency commspeed noise
	
On Linux, you can also run the `testreport` script, which runs a number of tests using the `unittest` script and automatically generates a .pdf file of the results ([example][test-report-example]):
	
	./testreport
		
Furthermore, you can test your Boks in OpenSesame using the `boks_test.opensesame` file included with the Boks source code.

[^system-1]: Acer Aspire V5-171, Intel Core I3-2365M @ 1.4Ghz, 6GB, 11.6" LCD
[^system-2]: HP Compaq dc7900, Intel Core 2 Quad Q9400 @ 2.66Ghz, 3GB, 21" ViewSonic P227f CRT
[^system-3]: See 2
[arduino]: http://arduino.cc/
[wikipedia-precision]: http://en.wikipedia.org/wiki/Accuracy_and_precision
[test-report-example]: /pdf/testlog-dev.boks-0.1.9.pdf
