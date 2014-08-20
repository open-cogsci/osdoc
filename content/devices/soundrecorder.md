---
layout: osdoc
title: Audio input
group: Devices
permalink: /soundrecorder/
---

%--
toc:
 mindepth: 2
--%

## About the sound recorder plug-ins

With the sound recorder plugin you can record audio directly from your microphone or devices connected to your sound card's line-in port. Please make sure that the input channel you want to record from is indicated as the default audio input device in your operating system settings.

The plugin consists of two items: sound_start_recording and sound_stop_recording, which both appear as draggable items in the item bar and do as their names suggest. In sound_start_recording you can set various options, such as the file/compression type with which the recording should be saved.

## Screenshot

![](/img/fig/fig9.9.1.png)

## Requirements

This plugin uses the [pymedia][pymedia-url] library to read audio from the microphone and compress it to mp3. For creating wav files, the standard python wave module is used.

## Download and installation

You can download the plugin [here][plugin-url]. There are three separate versions available:

- One which does not have the pymedia module included. You can use this version if you are running from source and want to install the pymedia module yourself. For operating systems other than windows you should also choose this version. (all platforms, from source)
- One for OpenSesame 0.26 (which runs on Python 2.6)(Windows only)
- One for OpenSesame 0.27 and higher (which runs on Python 2.7)(Windows only)

These separate versions are necessary because pymedia can only be compiled for specific Python versions.

## Usage

Insert a sound_start_recording item in your experiment at the point at which you would like to start recording and a sound_stop_recording item at the point at which the recording should end. After a recording is finished, it is written to the folder and filename as specified in the options of start_sound_recording.

In a limited way, you can also use the sound recorder object with inline_script. When a sound_start_recording item starts the actual recording, it makes a `self.experiment.soundrecorder` (or `exp.soundrecorder`) object available.
This object has two functions which you can call:

{% highlight python %}
soundrecorder.is_recording(): 
{% endhighlight %}
Returns True if it is currently recording and False if it has finished recording

{% highlight python %}
soundrecorder.stop(): 
{% endhighlight %}
Stops recording. This does the same as the sound_stop_recording item (which basically only calls the stop() function from the exp.soundrecorder item)

[pymedia-url]: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pymedia
[plugin-url]: https://github.com/dschreij/opensesame_soundrecorder_plugins/tags
