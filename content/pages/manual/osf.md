title: Integration with the Open Science Framework

[TOC]

## About

The OpenScienceFramework extension connects OpenSesame to the [Open Science Framework](https://osf.io) (OSF), which is a web platform for sharing, connecting, and streamlining scientific workflows. To use this extension, [you need an OSF account](https://osf.io/login/?sign_up=True).

With the OpenScienceFramework extension, you can:

- Automatically save your experiment to the OSF
- Automatically upload data to the OSF
- Open experiments from the OSF
- Share your experiment and data with other researchers, by giving them access through the OSF

## Logging in to the OSF

To log into the OSF:

- Create an account on <https://osf.io>. (You cannot create an account from within OpenSesame.)
- In OpenSesame, click on the log-in button in the main toolbar, and enter your credentials.
- Once logged in, you can open the OSF Explorer by clicking on your name where the login button used to be, and selecting *Show explorer*. The explorer will show an overview of all your OSF projects, and all repositories/ cloud services that are linked to your projects.

## Linking an experiment to the OSF

If you link an experiment to the OSF, each time that you save the experiment in OpenSesame, a new version is also uploaded to the OSF.

To link an experiment:

- Save the experiment on your computer.
- Open the OSF explorer and select a folder or repository where you would like your experiment to be stored on the OSF. Right-click on this folder and select *Sync experiment to this folder*. The OSF node to which the experiment is linked will be shown at the top of the explorer.
- The experiment is then uploaded to the selected location.
- If you check *Always upload experiment on save*, a new version is automatically saved to OSF on each save; if you don't enable this option, you will be asked every time whether or not you want to do this.

To unlink an experiment:

- Open the OSF explorer, and click the *Unlink* button next to the *Experiment linked to* link.

## Linking data to the OSF

If you link data to the OSF, each time that data has been collected (normally after every experimental session), this data is also uploaded to the OSF.

To link data to the OSF:

- Save the experiment on your computer.
- Open the OSF explorer, right-click on the folder that you want the data to be uploaded to, and select *Sync data to this folder*. The OSF node that the data is linked to will be shown at the top of the explorer.
- If you check *Always upload collected data*, data files will be automatically saved to OSF after they have been collected; if you don't enable this option, you will be asked every time whether or not you want to do this.

To unlink data from the OSF:

- Open the OSF explorer, and click the *Unlink* button next to the *Data stored to* link.

## Opening an experiment stored on the OSF

To open an experiment from the OSF:

- Open the OSF explorer, and find the experiment.
- Right-click on the experiment and select *Open experiment*.
- Save the experiment on your computer.

## Handling non-matching versions

If you open an experiment on your computer that is linked to the OSF, but differs from the version on the OSF, you will be asked what you want to do:

- Use the version from your computer; or
- Use the version from the OSF. If you choose to use the version from the OSF, it will be downloaded and overwrite the experiment on your computer.

## Installing the OpenScienceFramework extension

The OpenScienceFramework extension is installed by default in the Windows package of OpenSesame. If the extension is not installed, you can install it as follows:

From PyPi:

~~~
pip install opensesame-extension-osf
~~~

In an Anaconda environment

~~~
conda install -c cogsci opensesame-extension-osf
~~~

The source code of the extension is available on GitHub:

- <https://github.com/dschreij/opensesame-extension-osf>

And for the `python-qosf` module, which is used by the extension:

- <https://github.com/dschreij/python-qosf>
