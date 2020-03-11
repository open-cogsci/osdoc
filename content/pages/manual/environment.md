title: Installing packages, plugins, and extensions


[TOC]

If you receive permission errors on Windows, run OpenSesame as administrator.
{: .alert .alert-info}


## Using conda (preferred)

As of OpenSesame 3.3, the standard Windows packages come with a fully functioning Anaconda environment. This means that you can use `conda` to manage packages. To execute `conda` from the console:

- Prefix `conda` with `!` (to indicate that you want to execute a program rather than Python code)
- Pass the `-y` flag to avoid conda from prompting for input (which sometimes freezes the console)
- Have patience! (`conda` is known to be slow, and you will not get visual feedback until the command is finished)

Example: to install seaborn (a plotting library):

```
!conda install seaborn -y
```

Example: to update `rapunzel` and all its dependencies (which includes OpenSesame) using the `cogsci` and `conda-forge` channels:

```
!conda update rapunzel -c cogsci -c conda-forge -y
```

See also:

- <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html>


## Using pip

As of OpenSesame 3.3, you can use `pip` to manage packages directly from the console. Prefix `pip` with `!` (to indicate that you want to execute a program rather than Python code).

Example: to install the OpenScienceFramework extension:

```
!pip install opensesame-extension-osf
```

To see how you can use `pip` as a Python module, see the old documentation (this is no longer recommended):

- <https://osdoc.cogsci.nl/3.2/manual/environment/#using-pip-pypi>


## Using the Python package manager (experimental)

The Python package manager is unstable. If it crashes, use the installation/ upgrade methods described above.
{: .alert .alert-info}

A graphical package manager is available under Menu → Tools → Python package manager. This is a graphical manager for pip / PyPi.


## Manually installing plugins and extensions

To manually install a plugin or extension, simply copy the plugin/ extension folder to one of the folders that OpenSesame scans for plugins and extensions. Which folders those are depends on your operating system and distribution of OpenSesame.

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
