from jgine import config
import keyboard

from pynput import mouse
async def ev(objs):
    for o in objs:
        a = o.events
        for i in range(len(a)):
            if keyboard.is_pressed(a[i][0]):
                a[i][1](True)

def on_click(x, y, button, pressed):
    if pressed:
        pass



