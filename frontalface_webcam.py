import cv2

from random import randrange

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#img = cv2.imread('image.JPG') 'video.mp4' 9 строка вместо 0

webcam = cv2.VideoCapture(0)

while True:
	successful_frame_read, frame = webcam.read()
	
	grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
	for (x,y,w,h) in face_coordinates:
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 256, 0), 2)

	cv2.imshow('Programmer Face Detector', frame)
	key = cv2.waitKey(1)

	if key==81 or key==113:
		break
webcam.release()
	
	

#18 строка (0,255,0)
#cv2.imshow('Programmer Face Detector', img)
#cv2.waitKey()








print ("Code Completed")