from libopensesame.experiment import experiment

# A very basic experiment in OpenSesame script
exp_str = u'''
set start my_sketchpad
define sketchpad my_sketchpad
	draw textline 0 0 "Dummy text"
'''
# Parse the OpenSesame script into an experiment object
exp = experiment(string=exp_str)
# Calling the `experiment.run()` method will launch the full experiment
exp.run()
# Access the `my_sketchpad` item
my_sketchpad = exp.items[u'my_sketchpad']
print my_sketchpad
# The item in turn contains a reference to the `experiment` object
print my_sketchpad.experiment