title: Running experiment without the GUI

## About

`opensesamerun` is a simple tool that allows you to execute OpenSesame experiments with a minimal GUI, or directly, by specifying all necessary options via the command line. A minimal GUI will automatically appear if not all command line options have been specified, notably the experiment file, the subject number, and the log file.

~~~
Usage: opensesamerun [experiment] [options]

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit

  Subject and log file options:
    -s SUBJECT, --subject=SUBJECT
                        Subject number
    -l LOGFILE, --logfile=LOGFILE
                        Logfile

  Display options:
    -f, --fullscreen    Run fullscreen
    -c, --custom_resolution
                        Do not use the display resolution specified in the
                        experiment file
    -w WIDTH, --width=WIDTH
                        Display width
    -e HEIGHT, --height=HEIGHT
                        Display height

  Miscellaneous options:
    -d, --debug         Print lots of debugging messages to the standard
                        output
    --stack             Print stack information

  Miscellaneous options:
    --pylink            Load PyLink before PyGame (necessary for using the
                        Eyelink plug-ins in non-dummy mode)
~~~

## Example

Let's say that you want to run the gaze cuing example experiment, for subject #1, and save the log file in your Documents folder (this example assumes Linux, but it works analogously on other platforms):

~~~
opensesamerun /usr/share/opensesame/examples/gaze_cuing.opensesame.tar.gz -s 1 -l /home/sebastiaan/Documents/subject1.tsv -f 
~~~
