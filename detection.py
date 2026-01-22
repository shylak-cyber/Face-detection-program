import cv2
from ultralytics import YOLO

model=YOLO('yolov8n.pt')

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"face",(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,0.9,(255,0,0),2)

   
    results=model(frame)
    for r in results:
        for box in r.boxes:
            cls=int(box.cls[0])
            label=model.names[cls]
            conf=float(box.conf[0])

            x1,y1,x2,y2=map(int,box.xyxy[0])
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"{label} {conf:.2f}",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
            print("Detected:",label)

    cv2.imshow('face + object detection',frame)
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()