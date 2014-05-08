import random
import time
import pibrella

def dice():
    guess = random.randint(1,6)
    print("I'm going to think of a number between 1 and 6 and I will flash the lights on your Pibrella to indicate the number I chose")
    print("The number is "+(guess))
    for i in range(guess):
        pibrella.light.on()
        time.sleep(0.5)
        pibrella.light.off()

def standby():
    for i in range(6):
        pibrella.light.red.fade(0,100,2)
        pibrella.light.amber.fade(0,100,2)
        pibrella.light.green.fade.(0,100,2)
    

def button_changed(pin):
    if pin.read() == 1:
        dice()
    else:
        standby()


