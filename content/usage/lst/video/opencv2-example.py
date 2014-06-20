import cv2
import numpy
import pygame
# Full path to the video file
path = exp.get_file('myvideo.avi')
# Open the video and determine the video dimensions
video = cv2.VideoCapture()
# A loop to play the video file. This can also be a while loop until a key
# is pressed. etc.
for i in range(100):
	# Get a frame
	retval, frame = video.read()
	# Rotate it, because for some reason it otherwise appears flipped.
	frame = numpy.rot90(frame)
	# The video uses BGR colors and PyGame needs RGB
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	# Create a PyGame surface
	surf = pygame.surfarray.make_surface(frame)
	# Now you can draw whatever you want onto the PyGame surface!
	pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))
	# Show the PyGame surface!
	exp.surface.blit(surf, (0, 0))
	pygame.display.flip()
