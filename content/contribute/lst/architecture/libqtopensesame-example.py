from libqtopensesame.qtopensesame import qtopensesame
from libqtopensesame.items.experiment import experiment

# A very basic experiment in OpenSesame script
exp_str = u'''
set start my_sketchpad
define sketchpad my_sketchpad
	draw textline 0 0 "Dummy text"
'''

main_window = qtopensesame()

# Parse the OpenSesame script into an experiment object
exp = experiment(main_window, u'experiment', string=exp_str)
# Calling the `experiment.run()` method will launch the full experiment
exp.run()
