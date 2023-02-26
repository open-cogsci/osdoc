title: Sound recording

[TOC]


## Audio Low Latency plugins

The Audio Low Latency plugins, developed by Bob Rosbag, are the recommended way to record sound input. The main goal of this set of plugins is to play and record audio with minimal and predictable latencies to achieve a high accuracy and precision. The `PyAlsaAudio` package which uses the Linux ALSA audio system provided the best results within Python. `PortAudio` and `sounddevice` are cross-platform and work on both Windows as Linux.

The plugins are not installed by default, but can be installed through pip:

```bash
pip install opensesame-plugin-audio-low-latency
```

See also:

- <https://pypi.org/project/opensesame-plugin-audio-low-latency/>


## Sound recorder plugins

The sound recorder plugins, developed by Daniel Schreij, are no longer under active development and are therefore no longer recommended. More information about this set of plugins can be found on previous version of this page:

- <https://osdoc.cogsci.nl/3.2/manual/response/soundrecording/>
