import cv2
from cvzone.HandTrackingModule import HandDetector
import socket 

#Parameters
#Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1024)
cap.set(4, 768)
success, img = cap.read()

# Hand Detector
h, w, _ = img.shape
detector = HandDetector(detectionCon = 0.8, maxHands = 2)

# Communication 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverAddressPort = ("127.0.0.1", 5052)

while True:
    # Get the frame from the webcam
    success, img = cap.read()
    # Hands
    hands, img = detector.findHands(img)

    data = []
    # Landmark values - (x, y, z) * 21
    if hands:
        # Get the first hand detected 
        hand = hands[0]

        #Get the landmark list 
        lmList = hand['lmList']
        #print(lmList)
        for lm in lmList:
            data.extend([lm[0], h - lm[1], lm[2]])
        #print(data)
        sock.sendto(str.encode(str(data)), serverAddressPort)


    
    cv2.imshow("Image", img)

    key = cv2.waitKey(10)
    if key==81 or key==113:
        break