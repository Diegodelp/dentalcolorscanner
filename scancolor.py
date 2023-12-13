import cv2 as cv
import numpy as np
from tkinter import *
from PIL import Image, ImageTk 

cap = cv.VideoCapture(0)



if not cap.isOpened():
 print("Cannot open camera")
 exit()
 
while True:
 # Capture frame-by-frame
    ret, frame = cap.read()
 # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display the resulting frame
    cv.imshow('frame', frame)
    break
# When everything done, release the capture




def mouse_callback(event, x, y, flags, param):
    global start_x, start_y, frame
    start_x = 0
    start_y = 0
    if event == cv.EVENT_LBUTTONDOWN:
        # Get the coordinates of the mouse click
        start_x = x
        start_y = y

    elif event == cv.EVENT_MOUSEMOVE:
        # Draw a rectangle from the start point to the current mouse position
        frame, start_x, start_y
        cv.rectangle(frame, (start_x, start_y), (x, y), (0, 255, 0), 2)

    elif event == cv.EVENT_LBUTTONUP:
        # Get the coordinates of the mouse release
        end_x = x
        end_y = y
 
        # Get the selected area
        roi = cv.selectROI("frame", frame)

        # Crop the selected area from the frame
        selected_frame = frame[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]

        # Average the colors of the selected rectangle
        average_color = np.mean(selected_frame, axis=(0, 1))
        average_color_list = list(average_color)
        average_color_list = list(reversed(average_color_list))
        average_color = np.array(average_color_list)
        average_color_int = average_color.astype(int)
        average_color_list = list(average_color_int)
        print(average_color_list)
        
        hex_code = f"#{format(average_color_list[0], '02x')}{format(average_color_list[1], '02x')}{format(average_color_list[2], '02x')}"

        print(hex_code)                       
        # Print the average color to the console
        

   
        

if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv.setMouseCallback("frame", mouse_callback)

        cv.imshow("frame", frame)


        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cv.destroyAllWindows()

