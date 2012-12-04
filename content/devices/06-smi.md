---
layout: osdoc
title: SMI eye tracker
group: Devices
permalink: /smi/
level: 1
sortkey: 009.006
---

##### This posts describes libsmi.py. Alternatively, you may want to consider Ryan Hope's PyViewX module. I haven't tested it myself, but it appears to be reasonably well maintained and easy to use. You can find PyViewX at <https://github.com/RyanHope/PyViewX>.

There are no plug-ins for the SMI eye tracker yet (<http://www.smivision.com>), but using the device is fairly straightforward with the custom Python library `libsmi`. This class assumes that communication is handled through the serial port. I have not had the opportunity to test `libsmi.py` extensively yet, but the example experiments work flawlessly on the SMI Red test set-up (iViewX 2.3 build 21, OpenSesame 0.24, Windows XP). Please let me know of any problems and feel free to extend/ modify the code.

Download/ examples
------------------

The latest version of libsmi.py and two example experiments are available on GitHub:

- <https://github.com/smathot/libsmi>

Using libsmi
------------

The easiest way to use libsmi is through the external_script plug-in, as demonstrated in the example experiments. First, download libsmi.py from GitHub and select it in the external_script plug-in. This will assure that libsmi is available in inline_scripts as `exp.tracker`. So, to perform a calibration, you would simply use the following inline_script:

{% highlight python %}
exp.tracker.calibrate()
{% endhighlight %}

For a full list of available functions, see the function overview.

If you want to use functionality that is not offered directly by libsmi, you can send commands as specified in the iViewX [manual][]. For example, you can save the data by sending the `ET_SAV` command directly:

{% highlight python %}
exp.tracker.send('ET_SAV "my_data.idf"')
{% endhighlight %}

{% include doc/libsmi %}

[manual]: http://drcwww.uvt.nl/~Cenv/dci-lab/smi/iViewX.pdf