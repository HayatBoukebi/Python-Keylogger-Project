#Controlling the mouse
from pynput.mouse import Controller    
from pynput.keyboard import Controller

def controllerMouse():
    mouse = Controller()
    mouse.position = (100,20)
controllerMouse()

def controllerkeyboard():
    keyboard = Controller()
    keyboard.type("hayat")

controllerkeyboard()