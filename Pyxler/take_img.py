# This program takes the screen every few seconds (see variable "time_difference")
# and saves the recordings in the folder "collected_data".
# This program is free to use and may also be modified.
# Developer: Lars Wisotzky

from PIL import ImageGrab 
import time
import keyboard
import os

# =======================================================

time_difference = 2 # time between frames in seconds

time_before_start = 5
img_name = "image "
path = "collected_data/"
quit_key = "p"

# =======================================================

dir_list = os.listdir(path)

try:
    last_img = dir_list[-1]
    start_index = int(''.join([n for n in last_img if n.isdigit()])) + 1
except IndexError:
    start_index = 0

print("It starts in {} seconds.".format(time_before_start))
time.sleep(time_before_start)
print("lets go!")
while True:
    snapshot = ImageGrab.grab()

    save_path = path+img_name+str(start_index)+".png"
    snapshot.save(save_path)
    print(save_path) 

    start_index += 1

    if keyboard.is_pressed(quit_key) == True:
        print("exit!")
        quit()

    time.sleep(time_difference)