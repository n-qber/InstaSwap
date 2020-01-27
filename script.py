from pynput.mouse import Controller, Listener
from time import sleep

mouse = Controller()
pressed = False
released = False
to_subtract = 0

def identifyScroll(posX, posY, button, state):
    global to_subtract
    global pressed
    #print(state)
    #if button.name == "middle":
    if button.name == "right":

        if state:
            #print('Pressed')
            pressed = True
        else:
            #print("Released")
            pressed = False


        if pressed:
            to_subtract = posX

        else:
            toScroll = posX - to_subtract
            #print(toScroll)
            to_subtract = posX
            
            if toScroll > 0:
                toScroll = 400
            elif toScroll < 0:
                toScroll = -400
            
                                    
            mouse.scroll(toScroll*-1, 0)


with Listener(on_click=lambda *args: identifyScroll(args[0], args[1], args[2], args[3])) as l:
    l.join()

