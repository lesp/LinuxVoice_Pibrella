import random
import time
import pibrella

def dice():
    guess = random.randint(1,6)
    print("I'm going to think of a number between 1 and 6 and I will flash the lights on your Pibrella to indicate the number I chose")
    print("The number is "+str(guess))
    for i in range(0,(guess)):
        time.sleep(0.5)
        pibrella.light.on()
        pibrella.buzzer.note(1)
        time.sleep(0.5)
        pibrella.light.off()
        pibrella.buzzer.off()

while True:
    while pibrella.button.read() == 1:
        dice()
