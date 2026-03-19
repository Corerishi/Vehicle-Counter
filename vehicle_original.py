import cv2
import numpy as np
import os

VIDEO_PATH = 'video.mp4'         
MIN_WIDTH  = 80                    
MIN_HEIGHT = 80                    
COUNT_LINE_Y = 550                 
OFFSET = 6                         

if not os.path.exists(VIDEO_PATH):
    print(f"Error: Video file not found at '{VIDEO_PATH}'")
    print("Place your video file in the same directory as this script and rename it 'video.mp4'")
    exit()

cap = cv2.VideoCapture(VIDEO_PATH)

if not cap.isOpened():
    print(f"Error: Could not open video file at '{VIDEO_PATH}'")
    exit()

algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def get_center(x, y, w, h):
    """Return the center point of a bounding rectangle."""
    cx = x + int(w / 2)
    cy = y + int(h / 2)
    return cx, cy

detect  = []  
counter = 0  

while True:
    ret, frame = cap.read()

    if not ret:
        print("End of video or unreadable frame — exiting.")
        break

    grey  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur  = cv2.GaussianBlur(grey, (3, 3), 5)

    img_sub   = algo.apply(blur)
    dilated   = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel    = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    processed = cv2.morphologyEx(dilated, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(processed, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (25, COUNT_LINE_Y), (1200, COUNT_LINE_Y), (255, 127, 0), 3)

    for c in contours:
        (x, y, w, h) = cv2.boundingRect(c)

        if w < MIN_WIDTH or h < MIN_HEIGHT:
            continue

        center = get_center(x, y, w, h)
        detect.append(center)

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Vehicle " + str(counter), (x, y - 20),
                    cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 244, 0), 1)
        cv2.circle(frame, center, 4, (0, 0, 255), -1)

    for (cx, cy) in detect[:]:  
        if (COUNT_LINE_Y - OFFSET) < cy < (COUNT_LINE_Y + OFFSET):
            counter += 1
            cv2.line(frame, (25, COUNT_LINE_Y), (1200, COUNT_LINE_Y), (0, 127, 255), 3)
            detect.remove((cx, cy))
            print(f"Vehicle counted: {counter}")

    cv2.putText(frame, "VEHICLE COUNT: " + str(counter),
                (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow('Vehicle Counter', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
print(f"\nFinal vehicle count: {counter}")
