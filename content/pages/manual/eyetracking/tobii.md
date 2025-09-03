title: Tobii

## Installing Tobii research

`tobii-research` is the Python library for Tobii support. Currently, `tobii-research` only supports Python 3.10 and earlier, whereas the standard packages of OpenSesame are built with Python 3.13. Therefore, you must use the Python 3.10 (or earlier) package of OpenSesame from [GitHub releases](https://github.com/open-cogsci/OpenSesame/releases).

Next, `tobii-research` can be installed:

```
pip install tobii-research
```

For more information, see:

- <http://www.tobii.com/en/eye-tracking-research/global/>


## PyGaze

After you have install `tobii-research`, you can use Tobii with PyGaze! See:

- %link:pygaze%


## Titta eye-tracking plugin

Bob Rosbag, Diederick C. Niehorster & Marcus Nyström have developed their own Tobii plug-ins for OpenSesame. These are somewhat similar to the PyGaze plugins, but offer some functionality that is not available through PyGaze, and may also be more stable. To install these plugins, run:

```
pip install opensesame-plugin-titta-eyetracking
```

For more information, please visit:

- <https://github.com/dev-jam/opensesame-plugin-titta_eyetracking>
