from ultralytics import YOLO
import cv2
import cvzone
import math

#cap = cv2.VideoCapture(1) #for webcam
#cap.set(3, 640)
#cap.set(4, 480)
cap = cv2.VideoCapture("../Videos/ppe 1.1.mp4") #for video


model = YOLO("../Yolo-weights/yolov8l.pt")
#model = YOLO("ppe.pt")

classNames = ['curb', 'dash', 'distressed', 'grate', 'manhole', 'marking', 'pothole', 'utility']

myColour = (0,255,0)

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            #cv2.rectangle(img, (x1, y1,), (x2, y2), (255, 0, 200), 3)


            w, h = x2 - x1,y2 - y1
            #cvzone.cornerRect(img, (x1 ,y1 ,w ,h))

            conf = math.ceil((box.conf[0]*100))/100
            cls = int(box.cls[0])
            currentClass = classNames[cls]
            print(currentClass)
            if currentClass =='curb':
                myColour = (0,255,0)
            else:
                myColour(0,0,255)

            cv2.rectangle(img, (x1, y1), (x2, y2), myColour, 3)
            cvzone.putTextRect(img,f'{classNames[cls]} {conf}',(max (0, x1),max(35,y1)),scale=1,thickness=1,colorB=myColour,colorT=(255,255,255),colorR=myColour)

    cv2.imshow("Image",img)
    cv2.waitKey(1)
