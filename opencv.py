import cv2

'''#reading images and videos 

img = cv2.imread('image.jpg')

#display the image as a new window

cv2.imshow('image', img)

#wait for the key to be pressed
'''
capture = cv2.VideoCapture('traffic.mp4')

#add loop for every seconds of the video

while True:
	isTrue, frame = capture.read()
	cv2.imshow('traffic', frame)
	key = cv2.waitKey(1)

	if key==81 or key==113:
		break