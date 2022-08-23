# The program is suitable for Pytorch object reconnaissance models.
# It captures the screen and in a new window you can see the detections.
# At the end you can see the average FPS.

from os import path
import mss
import numpy as np
import cv2
import keyboard
import torch 
import time

# In my case I used it for Yolov5
model = model = torch.hub.load('ultralytics/yolov5', 'custom', path="C:/dev/YOLOv5/yolov5/runs/train/exp5/weights/last.pt")
quit_key = "p"


with mss.mss() as sct:
     monitor = {'top': 0, 'left': 0, 'width': 1920, 'height': 1080}

fps_list = []
while True:
    t = time.time()

    img = np.array(sct.grab(monitor))
    results = model(img)

    cv2.imshow("s", np.squeeze(results.render()))
    fps = int(1/(time.time()-t))
    fps_list.append(fps)

    cv2.waitKey(1)
    if keyboard.is_pressed(quit_key):
        break

cv2.destroyAllWindows()
print(sum(fps_list) / len(fps_list))