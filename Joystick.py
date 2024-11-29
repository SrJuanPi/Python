# Code created by BallaMOTO https://www.youtube.com/watch?v=AgHov-F_tKg&t=794s

import serial
import pydirectinput

arduino = serial.Serial('COM4', 115200, timeout=0.1)     # serial input from arduino, change COM port
                                                        # to wherever your arduino is connected

pydirectinput.PAUSE = 0

keysDown = {}       # list of currently pressed keys    

def keyDown(key):               # what to do if key pressed. takes value from handleJoyStickAsArrowKeys
    keysDown[key] = True        # adds key to KeysDown list
    pydirectinput.keyDown(key)  # runs pydirectinput using key from (argument)
    # print('Down: ', key)       # remove '#' from print to test data stream
    

def keyUp(key):                     # what to do if key released. takes value from handleJoyStickAsArrowKeys
    if key in keysDown:
        del (keysDown[key])         # remove key from keysDown
        pydirectinput.keyUp(key)    # runs pydirectinput using key from (argument)
        # print('Up: ', key)         # remove '#' from print to test data stream
        
def handleJoyStickAsArrowKeys(x,y,z):
    if x == 0:          # 0 is up on joystick
        keyDown('s')   # add up key to keyDown (argument)
        keyUp('w')   # add down key to keyUp (argument), as you can't press up and down together
    elif x == 2:        # 2 is down on joystick
        keyDown('w')
        keyUp('s')
    else:               # 1 is neutral on joystick
        keyUp('s')
        keyUp('w')
        
    if y == 2:          # 2 is up on joystick
        keyDown('a')
        keyUp('d')
    elif y == 0:        # 0 is left on joystick
        keyDown('d')
        keyUp('a')
    else:               # 1 is neutral on joystick
        keyUp('d')
        keyUp('a')
    
    if z == 1:          # z argument is JSButton in this case. 1 is button pressed
        keyDown('0')    # key to be pressed whit Joystick button. Change to any key
    else:
        keyUp('0')      # 0 is button not pressed

while True:
    rawdata = arduino.readline()                    # read serial data from arduino one line at a time
    data = str(rawdata.decode('utf-8'))             # decode the raw byte data into UTF-8
    if data.startswith("S"):                        # make sure the read starts in the correct place
        dx = int(data[1])                           # X direction is second digit in data (data[0] is 'S')
        dy = int(data[3])                           # Y direction is fourth digit in data
        JSButton = int(data[5])                     # JSButton is sixth digit in data
        #print(dx, dy, JSButton)                    # remove '#' from print to test data stream
        handleJoyStickAsArrowKeys(dx, dy, JSButton) # run body of code using dx, dy and JSButton as inputs
        
