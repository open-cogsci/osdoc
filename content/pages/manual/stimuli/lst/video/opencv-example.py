import cv
import pygame

# Full path to the video file
path = exp.get_file('my_video.avi')

# Open the video and determine the video dimensions
video = cv.CreateFileCapture(path)
width = cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_WIDTH)
height = cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_HEIGHT)

# The video needs to be converted twice, so we need to intermediate OpenC
# matrices
src_tmp = cv.CreateMat(exp.height, exp.width, cv.CV_8UC3)
src_rgb = cv.CreateMat(exp.height, exp.width, cv.CV_8UC3)

# A loop to play the video file. This can also be a while loop until a key
# is pressed. etc.
for i in range(100):

	# Get a frame, resize it to the full screen, convert it to the proper
	# color format, and finally convert it to a PyGamesurface
	src = cv.QueryFrame(video)
	cv.Resize(src, src_tmp)
	cv.CvtColor(src_tmp, src_rgb, cv.CV_BGR2RGB)
	surf = pygame.image.frombuffer(src_rgb.tostring(), cv.GetSize(src_rgb), 'RGB')

	# Now you can draw whatever you want onto the PyGame surface!
	pygame.draw.rect(surf, (255,0,0), (100, 100, 200, 200))

	# Show the PyGame surface!
	exp.surface.blit(surf, (0, 0))
	pygame.display.flip()

