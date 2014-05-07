import pibrella
import time
import signals

#Create variables to control times

delay = 10
sequence = 2

#Create the sequence
while True:
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
