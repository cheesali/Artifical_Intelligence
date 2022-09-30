import cv2

#our image
#img_file = 'cars.png'
video = cv2.VideoCapture('traffic.mp4')

#our pre-trained car-classifier
classifier_file = 'car_detector.xml'

#create car classifier 
car_tracker = cv2.CascadeClassifier(classifier_file)

#Run forever until video stops
while True:

	#read the current frame
	(read_successful, frame) = video.read()

	#safe coding
	if read_successful: 
		#must convert to grayscale
		grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	else:
		break

	#detect cars (of any scale)
	cars = car_tracker.detectMultiScale(grayscaled_frame)

	#draw rectangles around the cars
	for (x, y, w, h) in cars:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

	#display('Car Detector') the image with the cars spotted
	cv2.imshow('Car Detector', frame)
	
	#dont autoclose	
	key = cv2.waitKey(1)

	if key==81 or key==113:
		break

	



'''
#create opencv image
img = cv2.imread(img_file)

#convert to grayscale (needed for haar cascade)
black_n_white = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#car1 = cars[0] на 23 строчку, чтобы единично выделять машины
#(x, y, w, h) = car1


#numbers where cars (rectangles x, y, witdth, height)
#print(cars)


print("Code completed")
'''