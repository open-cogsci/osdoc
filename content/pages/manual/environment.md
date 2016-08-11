title: Installing packages, plugins, and extensions


[TOC]


## Using pip / PyPi

### Installing

The easiest way to install Python packages, and OpenSesame plugins/ extensions is through pip, the PyPA-recommended tool for installing Python packages. Although OpenSesame plugins/ extensions are not strictly Python packages, they can nevertheless be installed as such.

From within OpenSesame, to install `opensesame-plugin-media_player_mpy`, run the following in the debug window:

	import pip
	pip.main(['install', 'opensesame-plugin-media_player_mpy'])

From a terminal, to install `opensesame-plugin-media_player_mpy`, run:

	pip install opensesame-plugin-media_player_mpy

### Upgrading

From within OpenSesame, to upgrade `python-pygaze` to the latest version, run the following in the debug window:

	import pip
	pip.main(['install', 'python-pygaze', '--upgrade'])

From a terminal, to upgrade `python-pygaze` to the latest version, run:

	pip install python-pygaze --upgrade


## Manually installing plugins and extensions

The easiest way to install OpenSesame plugins/ extensions is using `pip install`, as described above.
{: .alert .alert-info}

To manually install a plugin or extension, simply copy the plugin/ extension folder to one of the folders that OpenSesame scans for plugins and extensions. Which folders these are depends on your operating system and distribution of OpenSesame.

Under Windows, assuming that OpenSesame has been installed to `c:\Program Files (x86)\OpenSesame`, you can generally place plugins/ extensions in the following folders:

	c:\Program Files (x86)\OpenSesame\share\opensesame_plugins
	c:\Program Files (x86)\OpenSesame\share\opensesame_extensions

Under Linux, you can generally place plugins/ extensions in the following folders:

	/home/[username]/.local/share/opensesame_plugins
	/home/[username]/.local/share/opensesame_extensions

If you are unsure which folders are scanned, you can see the list of folders by executing the following in the debug window:

	from libopensesame import misc
	print(misc.base_folders)


## Manually installing Python packages and modules

The easiest way to install Python packages is using `pip install`, as described above.
{: .alert .alert-info}

You can also copy a Python package or module to one of the folders in the Python path. Which folders these are depends on your operating system and distribution of OpenSesame. You can get a list of all folders in the Python path by executing the following in the debug window:

	import sys
	print(sys.path)

A Python *module* is a single `.py` file; this file should be copied directly into one of the folders in the Python path. A Python *package* is a folder with `.py` files in it; this folder should also be copied directly into one of the folders in the Python path.


## Customizing your environment with environment.yaml

You can tell OpenSesame to scan extra folders, by specifying these folders in a file called `environment.yaml`. There are three entries:

- `PYTHON_PATH`
- `OPENSESAME_PLUGIN_PATH`
- `OPENSESAME_EXTENSION_PATH`

Each entry should be a semicolon-separated list of folders. All entries are optional.

	PYTHON_PATH: "/home/user/mylibs1;/home/user/mylibs2"
	OPENSESAME_PLUGIN_PATH: "/home/user/myplugins1;/home/user/myplugins2"
	OPENSESAME_PLUGIN_PATH: "/home/user/myextensions1;/home/user/myextensions2"

This file should be placed in the working directory of OpenSesame. Under Windows, this is generally the OpenSesame program folder; under Linux and Mac OS this is generally your home folder. You can find out what the working directory is by executing the following in the debug window:

	import os
	print(os.getcwd())
