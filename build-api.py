#!/usr/bin/env python3
# coding=utf-8

import yamldoc
import imp
import sys

ROOT = '/home/sebastiaan/git/opensesame-james/'
TARGET = 'include/api/'
sys.path.insert(0, ROOT)

def createdoc(src, target, cls, **kwdict):

	if cls is None:
		obj = imp.load_source('dummy', ROOT + src)
	else:
		obj = getattr(imp.load_source(cls, ROOT + src), cls)
	df = yamldoc.DocFactory(obj, container=u'div', **kwdict)
	print('Writing %s' % target)
	with open(TARGET + target, 'w') as fd:
		fd.write(str(df))


def main():

	global ROOT

	createdoc(src='opensesame_plugins/joystick/_libjoystick/basejoystick.py',
		target='joystick.md', cls='basejoystick', customName='joystick')
	createdoc(src='opensesame_plugins/srbox/libsrbox.py',
		target='srbox.md', cls='libsrbox', customName='srbox')
	createdoc(src='libopensesame/var_store.py',
		target='var.md', cls='var_store', customName='var')
	createdoc(src='libopensesame/file_pool_store.py',
		target='pool.md', cls='file_pool_store', customName='pool')
	createdoc(src='libopensesame/item_store.py',
		target='items.md', cls='item_store', customName='items')
	createdoc(src='libopensesame/response_store.py',
		target='responses.md', cls='response_store', customName='responses')
	createdoc('libopensesame/python_workspace_api.py',
		target='python_workspace_api.md', onlyContents=True,
		types=[u'function', u'module'], cls=None, exclude=['osexception'])

	for backend in ['sampler', 'canvas', 'keyboard', 'mouse', 'clock', 'log']:
		createdoc('openexp/_%s/%s.py' % (backend, backend),
			target='%s.md' % backend, cls=backend)

	for widget in ['form', 'button', 'image', 'image_button', 'checkbox',
		'rating_scale', 'label', 'text_input']:
		createdoc('libopensesame/widgets/_%s.py' % widget,
			target='%s.md' % widget, cls=widget)

	ROOT = '/home/sebastiaan/git/PyGaze/'
	sys.path.insert(0, ROOT)

	createdoc(src='pygaze/_eyetracker/baseeyetracker.py',
		target='eyetracker.md', cls='BaseEyeTracker', customName='eyetracker')


if __name__ == '__main__':
	main()
