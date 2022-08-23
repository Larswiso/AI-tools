# Video Converter (takes video input and produces photos for every second of duration)
# Base: https://www.geeksforgeeks.org/python-process-images-of-a-video-using-opencv/
# Modified by Lars Wisotzky


import cv2, os

# Parameters:

video = cv2.VideoCapture(r'AI-Tools\Pyxler\videos\example_video.mp4')

interval = 60							# Every 60th frame will be saved.

filename = 'frame '
directory = r'AI-Tools\Pyxler\frames' 	# The folder where the images are saved

# ================================================================================

os.chdir(directory)

if (video.isOpened() == False):
	print("Error opening the video file")
	quit()

index=0
index2=0

while(video.isOpened()):
	
	ret, frame = video.read()
	if ret == True:
		
		if index == interval:
			cv2.imwrite(filename+str(index2)+".png", frame)
			index = 0
			index2+=1
		#cv2.imshow('Frame',frame)
		
		key = cv2.waitKey(1)
		if key == ord('q'):
			break
	else:
		break
	index+=1
	
video.release()
cv2.destroyAllWindows()