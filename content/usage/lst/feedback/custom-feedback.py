if self.get('acc') > 90:
	exp.set('feedback_msg', 'Excellent, well done!')
elif self.get('acc') > 75:
	exp.set('feedback_msg', 'Pretty good')
else:
	exp.set('feedback_msg', 'Come on, you can do better!')

