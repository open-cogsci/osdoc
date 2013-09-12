response_time = 1000 # Assume that the RT was 1000ms
correct = 1 # Assume that the response was correct

exp.set('total_responses', self.get('total_responses')+1)
exp.set('total_correct', self.get('total_correct')+correct)
exp.set('total_response_time', self.get('total_response_time')+response_time)

avg_rt = self.get('total_response_time')/self.get('total_responses')
acc = 100.*self.get('total_correct')/self.get('total_responses')

exp.set('average_response_time', avg_rt)
exp.set('avg_rt', avg_rt)
exp.set('accuracy', acc)
exp.set('acc', acc)

