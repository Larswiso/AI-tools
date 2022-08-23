# This program takes the screen every few seconds (see variable "time_difference")
# and saves the recordings in the folder "collected_data".
# This program is free to use and may also be modified.
# Developer: Lars Wisotzky

from PIL import ImageGrab 
import time
import keyboard

# Parameters:

time_difference = 1         # time between frames in seconds

time_before_start = 5
img_name = "image "
path = "collected_data/"

quit_key = "q"
pause_key = "p"

start_index = 0

# =======================================================

paused_status = False

print("It starts in {} seconds.".format(time_before_start))
print("spam {} to exit".format(quit_key))
time.sleep(time_before_start)
print("lets go!")
while True:
    if paused_status == False:
        snapshot = ImageGrab.grab()

        save_path = path+img_name+str(start_index)+".png"
        snapshot.save(save_path)
        print(save_path) 

        start_index += 1

        time.sleep(time_difference)

    if keyboard.is_pressed(quit_key) == True:
        print("exit!")
        print("================================")
        quit()
    if keyboard.is_pressed(pause_key) == True and paused_status == False:
        print("================================")
        print("paused!")
        print("Wait 5 seconds before it can be used again!")
        time.sleep(5)
        print("Now it can go on again :)")
        print("================================")

        paused_status = True
    
    if keyboard.is_pressed(pause_key) == True and paused_status == True:
        paused_status = False