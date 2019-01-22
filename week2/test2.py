from __future__ import print_function
from psychopy import core, event, visual


def change_color(win, log=False):
    win.color = 'blue' if win.color == 'gray' else 'gray'
    if log:
        print('Changed color to %s' % win.color)


win = visual.Window(color='gray')
text = visual.TextStim(win,
                       text='Press C to change color,\n CTRL + Q to quit.')

# Global event key to change window background color.
event.globalKeys.add(key='c',
                     func=change_color,
                     func_args=[win],
                     func_kwargs=dict(log=True),
                     name='change window color')

# Global event key (with modifier) to quit the experiment ("shutdown key").
event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)

while True:
    text.draw()
    win.flip()
