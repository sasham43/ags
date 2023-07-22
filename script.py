# from gpiozero import Button
# button = Button(21)
import os
import subprocess

script_dir = '/home/pi/ags-vids'
# script_dir = '/Users/sashakramer/ags-vids'

index = 0

vids = os.listdir(script_dir)
# print(os.listdir(script_dir))
current_vid = vids[index]

# command = 'omxplayer --no-osd --loop {0}'.format(current_vid)
command = [
    'omxplayer',
    '--no-osd',
    '--loop',
    current_vid
]

sp = subprocess.run(command)

print("The exit code was: %d" % sp.returncode)