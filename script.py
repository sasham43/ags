# from gpiozero import Button
# button = Button(21)
import os

script_dir = '/home/pi/ags-vids'
# script_dir = '/Users/sashakramer/ags-vids'

index = 0

vids = os.listdir(script_dir)
# print(os.listdir(script_dir))
current_vid = vids[index]

command = 'omxplayer --no-osd --loop {0}'.format(current_vid)

subprocess = os.subprocess(command)

print("The exit code was: %d" % subprocess.returncode)