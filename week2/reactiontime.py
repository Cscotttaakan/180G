from psychopy import core, visual,event, logging
import random
import pyglet
import matplotlib.pyplot as plt
import time
from timeit import default_timer as timer
from datetime import datetime
#setup stimulus
win=visual.Window([400,400])
gabor = visual.GratingStim(win, tex='sin', mask='gauss', sf=5,
    name='gabor', autoLog=False)
fixation = visual.Circle(win=win, units='pix',radius=15,
        fillColor=[128,128,128],lineColor=[-1,-1,-1]) 
win.recordFrameIntervals = True
win.refreshThreshold = 1/60 + 0.004

logging.console.setLevel(logging.WARNING)

numberPressed = 0
experiment = True
clock = core.Clock()

key=pyglet.window.key
keyboard = key.KeyStateHandler()
win.winHandle.push_handlers(keyboard)

reactiontimes = []

def calculateTime(floor,cieling):
    refreshRate = 60.0

    return float((cieling - floor)/refreshRate)


event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

#let's draw a stimulus for 200 frames, drifting for frames 50:100


while experiment and numberPressed < 51:
    tim = random.randint(200,600)
    for frameN in range(tim):#for exactly 200 frames
        if tim - 50 <= frameN:  # present fixation for a subset of frames
            fixation.draw()
            if keyboard[key.F]:
                reactiontimes.append((calculateTime(tim - 50, frameN) - 0.080))
                numberPressed += 1
                break;
        win.flip()
with open('data.txt', 'w') as f:
    for item in reactiontimes:
        f.write("%s\n" % item)
