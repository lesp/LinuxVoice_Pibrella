import pibrella
import time
import signals

#Create variables to control times

delay = 10
sequence = 2

#Create functions for ease of use

def traffic_lights():
    #Create the sequence
    while pin.read() == 0:
        #Green on for 10 seconds
        print("GREEN")
        pibrella.light.green.on()
        time.sleep(delay)
        pibrella.light.green.off()
        #Amber for 2 seconds
        print("AMBER")
        pibrella.light.amber.on()
        time.sleep(sequence)
        pibrella.light.amber.off()
        #Red for 10 seconds.
        print("RED")
        pibrella.light.red.on()
        time.sleep(delay)
        #Don't turn off the red light until the end of the amber sequence.
        pibrella.light.red.off()
        print("AMBER")
        pibrella.light.amber.on()
        time.sleep(sequence)
        pibrella.light.amber.off()

def crossing():
    for i in range(0,6):
        pibrella.light.green,blink(1,1)

def button_changed(pin):
    if pin.read() == 1:
        crossing()
    else:
        traffic_lights()

pibrella.button.changed(button_changed)
   
