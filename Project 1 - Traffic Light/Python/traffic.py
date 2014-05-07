import pibrella
import time
import signals

#Create variables to control times

delay = 10
sequence = 2

#Create the sequence

#Green on for 10 seconds
pibrella.light.green.on()
time.sleep(10)
pibrella.light.green.off()
#Amber for 2 seconds
pibrella.light.amber.on()
time.sleep(2)
pibrella.light.amber.off()
#Red for 10 seconds.
pibrella.light.red.on()
time.sleep(10)
pibrella.light.red.off()
