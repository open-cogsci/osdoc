---
layout: osdoc
title: Create plug-in
group: contribute
permalink: /plug-in/
level: 1
sortkey: 0013.004
---

One of the perks of OpenSesame is the ability to add arbitrary functionality through plug-ins. A number of plug-ins have already been created, ranging from a simple plug-in to display a fixation dot to plug-ins for controlling the Eyelink (an eye tracker). In this tutorial we will create a plug-in to play video files. This will provide you with all the information you need to create you own plug-in!

Overview
--------

- [What are we going to do and what do we need?](#what)
- [The folder/file structure](#structure)
- [The code](#code)
- [Screenshot!](#screenshot)

What are we going to do and what do we need? {#what}
--------------------------------------------

OpenSesame doesn't support video playback natively. So we're going create a plug-in to fix this gaping hole in OpenSesame's functionality! Our plug-in uses a video file from the file pool as a source and plays it for a specified duration or until a key has been pressed or a mouse button has been clicked. The user can specify the duration of each frame, effectively controlling the playback speed. The user can also indicate whether the video should be scaled to fit the entire screen or shown in the center of the display in its original size.

The language that we will use is Python 2.6. If you are not familiar with Python it's probably worthwhile to follow some tutorials first:

- <http://www.python.org/doc/>

This plug-in requires opencv 2.1 (not 2.2, which is the most recent version) to be installed. You can download opencv here:

- <http://opencv.willowgarage.com/wiki/>

Because we will use a custom module (opencv), we will need to run OpenSesame from source. You can find out how to do this [in this article][source].

The folder/ file structure {#structure}
--------------------------

First things first, we need to know where to put our plug-in. OpenSesame looks in a few locations for plug-ins. If you are running Windows, the OpenSesame plug-in folders are

	[opensesame folder]\plugins
	[drive]:\Documents and Settings\[user name]\.opensesame\plugins

If you are running Linux, the OpenSesame plug-in folders are

	[home folder]/.opensesame/plugins
	/usr/share/opensesame/plugins

In the plug-in folder, create a folder with the name of your plug-in, in this case video_player.

	[plugin folder]/video_player

OpenSesame expects a couple of files to be present in this folder:

	[plugin folder]/video_player/video_player.py # Contains the plug-in code
	[plugin folder]/video_player/video_player.png # A 16x16 icon for the plug-in
	[plugin folder]/video_player/video_player_large.png # A 32x32 icon for the plug-in
	[plugin folder]/video_player/video_player.html # HTML help file
	[plugin folder]/video_player/info.txt # Some information about the plug-in

The icon and help files are fairly self explanatory (you can choose any icons you like and put whatever you want in the help file), but info.txt warrants some explanation. At this point, info.txt simply contains one line specifying the category of the plug-in, which is used to group the plug-ins in the GUI. You are free to choose any category you like, but, if possible, it's best to use one of the pre-existing categories to prevent unnecessary GUI clutter. Like so:

	category:Visual stimuli

The code {#code}
--------

##### You can find the code for this plug-in here: <https://github.com/smathot/OpenSesame/blob/master/plugins/video_player/video_player.py>

The file `video_player.py` contains the actual plug-in code. We will walk through the plug-in code line by line. You will find that a plug-in contains a lot of “magic”. That is, a lot of the functionality is derived from the underlying classes and you don't have to bother with it yourself. (This makes creating a plug-in quite easy, which is nice, but it also makes it difficult to fully understand the underlying structure. If you are not satisfied with the depth of this tutorial, you may want to take a look at the source code of the `libopensesame.item` and `libqtopensesame.qtplugin` modules.)

It's customary to start with a comment that contains some licensing info (obviously you can use whatever license you want, I personally use the GPL).

{% highlight python %}
"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""
{% endhighlight %}

Next we import all the modules that we are going to need for this plug-in. You will always need the `libopensesame.item` and `libqtopensesame.qtplugin` modules, as they are inherited by the plug-in classes. The rest of the required modules are highly specific to each plug-in.

{% highlight python %}
# Will be inherited by video_player
from libopensesame import item

# Will be inherited by qtvideo_player
from libqtopensesame import qtplugin

# Used to access the file pool
from libqtopensesame import pool_widget

# Used to throw exceptions
from libopensesame import exceptions

# OpenCV is used to read the video file
import cv

# PyGame is used to control the display
import pygame
from pygame.locals import *
{% endhighlight %}

Now we're all set to create the first class, which has the same name as the file, in this case `video_player`. This class handles all the plug-in's functionality, except for the GUI parts, which we will get to later. The `video_player` class has at least three functions, a constructor, a function that is called during the prepare phase of the experiment and a function that is called during the run phase of the experiment. Let's start with the constructor, which simply initializes the plug-in variables. The more complicated stuff is handled by the constructor of the item class.

{% highlight python %}
class video_player(item.item):

	"""
	Implements the plug-in
	"""

	def __init__(self, name, experiment, string = None):

		"""
		Constructor
		"""

		# First we set the plug-ins properties
		self.item_type = "video_player"
		self.description = "Plays a video from file"
		self.duration = "keypress"
		self.fullscreen = "yes"
		self.frame_dur = 50
		self.video_src = ""

		# The parent handles the rest of the construction
		item.item.__init__(self, name, experiment, string)
{% endhighlight %}

Next up is the `prepare()` function. This function is called during the non-time critical prepare phase of the experiment. You should try to minimize the tasks performed by the `run()` function and move as much of the code as possible into the `prepare()` function. In this case, there's not much preparation to be done, except for opening the video for reading. prepare() should return True on success and False on an error (alternatively, you can throw an exception on an error).

{% highlight python %}
	def prepare(self):

		"""
		Opens the video file for playback
		"""

		# Pass the word on to the parent
		item.item.prepare(self)

		# Find the full path to the video file. This will
		# point to some temporary folder where the
		# file pool has been placed
		path = self.experiment.get_file(self.video_src)

		# Open the video file
		self.video = cv.CreateFileCapture(path)

		# Report success
		return True
{% endhighlight %}

The `run()` function does the actual work: playing the video file. Take a look at the code comments to see what the function does. Note that this plug-in accesses PyGame directly, instead of using the `openexp` libraries. `run()` should also return `True` on success and `False` on an error (and, again, you can also throw an exception on an error if you prefer that method).

{% highlight python %}
	def run(self):

		"""
		Handles the actual video playback
		"""

		# Log the onset time of the item
		self.set_item_onset()

		t = pygame.time.get_ticks()
		start_t = t

		# Loop until a key is pressed
		go = True
		while go:

			# Getting the video from the file onto the PyGame canvas is a bit complicated:
			# http://opencv.willowgarage.com/documentation/python/cookbook.html#opencv-to-pygame
			src = cv.QueryFrame(self.video)
			src_rgb = cv.CreateMat(src.height, src.width, cv.CV_8UC3)
			cv.CvtColor(src, src_rgb, cv.CV_BGR2RGB)
			pg_img = pygame.image.frombuffer(src_rgb.tostring(), cv.GetSize(src_rgb), "RGB")

			# In fullscreen mode, the surface is converted to the pixel format of the display surface
			# and scaled directly onto the display surface
			if self.fullscreen == "yes":
				pg_img = pg_img.convert(self.experiment.surface)
				pygame.transform.scale(pg_img, (self.experiment.width, self.experiment.height), self.experiment.surface)

			# In unscaled mode, the surface is blitted onto the center of the display
			else:
				self.experiment.surface.blit(pg_img, ((self.experiment.width - pg_img.get_width()) / 2, (self.experiment.height - pg_img.get_height()) / 2))

			# Show the changes
			pygame.display.flip()

			# Pause before jumping to the next frame
			pygame.time.wait(self.frame_dur - pygame.time.get_ticks() + t)
			t = pygame.time.get_ticks()

			if type(self.duration) == int:
				# Wait for a specified duration
				if t - start_t >= self.duration:
					go = False

			# Catch escape presses
			for event in pygame.event.get():

				if event.type == KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						raise exceptions.runtime_error("The escape key was pressed.")
					if self.duration == "keypress":
						go = False

				if event.type == MOUSEBUTTONDOWN and self.duration == "mouseclick":
					go = False

		# Release the camera
		# Note: This function appears to be missing. Perhaps it's ok
		# and Python will release it automatically?
		# cv.ReleaseCapture(self.video)

		# Report success
		return True
{% endhighlight %}

That's all for the `video_player` class, which is almost a full fledged plug-in. The only thing that is still missing is the GUI. This is handled by the `qtvideo_player` class or, more generally, a class named `qt[name of plugin]`. The constructor of the class is stereotyped, and will probably not vary from plug-in to plug-in (except for the name).

{% highlight python %}
class qtvideo_player(video_player, qtplugin.qtplugin):

	"""
	Handles the GUI aspects of the plug-in.
	"""

	def __init__(self, name, experiment, string = None):

		"""
		Constructor. This function doesn't do anything specific
		to this plugin. It simply calls its parents. Don't need to
		change, only make sure that the parent name matches the name
		of the actual parent.
		"""

		# Pass the word on to the parents
		video_player.__init__(self, name, experiment, string)
		qtplugin.qtplugin.__init__(self, __file__)
{% endhighlight %}

The most important function is the `init_edit_widget()` function. This functions fills the edit tab of the plug-in with all the necessary controls. GUI programming can be quite difficult, but fortunately the `qtplugin` class provides a number of functions which automatically add controls to the GUI. (Of course you can also use PyQt4 directly to create your own GUI. This is more flexible but also considerably more complex.) You simply call these functions and pass the name of the variable that you want the control to be attached to, a description to be shown in the GUI and some other parameters that depend on the type of control.

{% highlight python %}
	def init_edit_widget(self):

		"""
		This function creates the controls for the edit
		widget.
		"""

		# Lock the widget until we're doing creating it
		self.lock = True

		# Pass the word on to the parent
		qtplugin.qtplugin.init_edit_widget(self, False)

		# We don't need to bother directly with Qt4, since the qtplugin class contains
		# a number of functions which directly create controls, which are automatically
		# applied etc. A list of functions can be found here:
		# https://github.com/smathot/OpenSesame/blob/master/libqtopensesame/items/qtplugin.py

		self.add_filepool_control("video_src", "Video file", self.browse_video, default = "", tooltip = "A video file")
		self.add_combobox_control("fullscreen", "Resize to fit screen", ["yes", "no"], tooltip = "Resize the video to fit the full screen")
		self.add_line_edit_control("duration", "Duration", tooltip = "Expecting a value in milliseconds, 'keypress' or 'mouseclick'")
		self.add_spinbox_control("frame_dur", "Frame duration", 1, 500, suffix = "ms", tooltip = "Duration in milliseconds of a single frame")

		# Add a stretch to the edit_vbox, so that the controls do not
		# stretch to the bottom of the window.
		self.edit_vbox.addStretch()

		# Unlock
		self.lock = True
{% endhighlight %}

You may have noticed that `self.browse_video` was passed as a parameter to the add_file_pool_control() function. This is because, unlike the others controls, `add_file_pool()` control is not completely automated and requires a function which is called when the browse button is clicked. Typically, this function will show the file pool dialog and set change the contents of the input field based on the selection from the file pool. If you want to use the file pool in your plug-in, you can simply use this function as a template.

{% highlight python %}
	def browse_video(self):

		"""
		This function is called when the browse button is clicked
		to select a video from the file pool. It displays a filepool
		dialog and changes the video_src field based on the selection.
		"""

		s = pool_widget.select_from_pool(self.experiment.main_window)
		if str(s) == "":
			return
		self.auto_line_edit["video_src"].setText(s)
		self.apply_edit_changes()
{% endhighlight %}

The final two functions of `qtvideo_player` deal with setting the graphical controls based on the plug-in parameters and vice versa. Unless you have created custom controls, you can simply leave these functions unchanged.

{% highlight python %}
	def apply_edit_changes(self):

		"""
		Set the variables based on the controls. The code below causes
		this to be handles automatically. Don't need to change.
		"""

		# Abort if the parent reports failure of if the controls are locked
		if not qtplugin.qtplugin.apply_edit_changes(self, False) or self.lock:
			return False

		# Refresh the main window, so that changes become visible everywhere
		self.experiment.main_window.refresh(self.name)

		# Report success
		return True

	def edit_widget(self):

		"""
		Set the controls based on the variables. The code below causes
		this to be handled automatically. Don't need to change.
		"""

		# Lock the controls, otherwise a recursive loop might arise
		# in which updating the controls causes the variables to be
		# updated, which causes the controls to be updated, etc...
		self.lock = True

		# Let the parent handle everything
		qtplugin.qtplugin.edit_widget(self)

		# Unlock
		self.lock = False

		# Return the _edit_widget
		return self._edit_widget
{% endhighlight %}


That's it! You now have a fully functioning plug-in for playing video files. As a final thing, to be nice to your users, you should add some sensible content to the `.html` help file.

Screenshot! {#screenshot}
-----------

![](/img/fig/fig13.4.1.png)

[source]: /getting-started/running-from-source