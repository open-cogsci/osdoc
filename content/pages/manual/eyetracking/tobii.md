title: Tobii

PyGaze offers *experimental* support for Tobii eye trackers.

`tobii-research` is the Python library for Tobii support. As of July 2023, `tobii-research` requires Python 3.10, whereas OpenSesame by default uses Python 3.11. Therefore, until `tobii-research` is updated for Python 3.11, the easiest way to install OpenSesame with Tobii support is by building a Python 3.10 environment through Anaconda.

This sounds complicated, but it is really not. To do so, first read the general procedure for installing OpenSesame through Anaconda as described on the Downloads page:

- %link:download%

Next, once you understand the general procedure, start by creating a Python 3.10 environment, continue with the instructions from the Downloads page, and then install `tobii-research`:

```
# Start by creating a Python 3.10 environment
conda create -n opensesame-py3 python=3.10
conda activate opensesame-py3
# Now follow the instructions from the downloads page
# ...
# Then install Tobii support
pip install tobii-research
# And now launch OpenSesame!
opensesame
```

For more information, see:

- %link:pygaze%
- <https://rapunzel.cogsci.nl/manual/environment/>
- <http://www.tobii.com/en/eye-tracking-research/global/>
