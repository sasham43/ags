from gpiozero import Button
import os
import subprocess

script_dir = '/home/pi/ags-vids'
# script_dir = '/Users/sashakramer/ags-vids'

index = 0

vids = os.listdir(script_dir)
# print(os.listdir(script_dir))
# current_vid = vids[index]

# # command = 'omxplayer --no-osd --loop {0}'.format(current_vid)
# command = [
#     'omxplayer',
#     '--no-osd',
#     '--loop',
#     '{0}/{1}'.format(script_dir, current_vid)
# ]

# sp = subprocess.run(command)

# print("The exit code was: %d" % sp.returncode)


def on_press():
    index = index + 1
    run_cmd()

def run_cmd():
    current_vid = vids[index]

    # command = 'omxplayer --no-osd --loop {0}'.format(current_vid)
    command = [
        'omxplayer',
        '--no-osd',
        '--loop',
        '{0}/{1}'.format(script_dir, current_vid)
    ]

    sp = subprocess.run(command)

    print("The exit code was: %d" % sp.returncode)


button = Button(21)

button.when_pressed = on_press

run_cmd()