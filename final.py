from ultralytics import YOLO
import cvzone
import cv2
import math
import serial

ser=serial.Serial('COM15',115200)

# Running real-time from webcam
cap = cv2.VideoCapture(0)

model = YOLO('C:/Users/Dell/Downloads/WEAPON/best.pt')


# Reading the classes
classnames = ['Grenade', 'Knife', 'Pistol', 'Rifle', 'Shotgun']



frame_number = 0


while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    result = model(frame, stream=True)
    s1 = 0

    # Getting bbox, confidence, and class names information to work with
    for info in result:
        boxes = info.boxes
        for box in boxes:
            confidence = box.conf[0]
            confidence = math.ceil((box.conf[0]*100))/100
            Class = int(box.cls[0])
            if confidence>=0.65:
                
                print("Confidence --->",confidence)
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
                cvzone.putTextRect(frame, f'{classnames[Class]} {confidence}%', [x1 + 8, y1 + 100],
                                scale=1.5, thickness=2)

                
                if classnames[Class] == "Grenade":
                    a = 'Grenade'
                    ser.write(b'A')
                    print('data pass')
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Knife":
                    a = 'Knife'
                    ser.write(b'B')
                    print('data pass')
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                   

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Pistol":
                    a = 'Pistol'
                    ser.write(b'C')
                    print('data pass')
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Rifle":
                    a = 'Rifle'
                    ser.write(b'D')
                    print('data pass')
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                elif classnames[Class] == "Shotgun":
                    a = 'Shotgun'
                    ser.write(b'E')
                    print('data pass')
                    frame_number += 1
                    coordinates = f'({x1}, {y1}) to ({x2}, {y2})'
                    

                    # Print status
                    print(f"Detected: {classnames[Class]}, Confidence: {confidence}, Coordinates: {coordinates}")
                    
                
                    
                                    
                else:
                    print("No Data")
                    
            else:
                    print("No Data")
                    

    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    
    # Save Excel workbook


cv2.destroyAllWindows()