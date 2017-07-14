#!/usr/bin/env python

#Psuedo-Code
#1. Take a STRIP of LED's and animate a "heart beat"
#2. Heartbeat should essentially be a sine wave


import opc,time, math
#Debugging Purposes: For plotting a graph
#pip install matplotlib
#import matplotlib.pyplot as plt

numLEDs = 512
#Chunk lights into sections of circle
chunks = (360 / numLEDs) - 1


#Uncomment when running live
#client = opc.Client('localhost:7890')

#Debugging: Hold x and y values
#xvalues = []
#yvalues =[]


#Frame of animation
counter = 0

#Every second, for every light in the range, light up based on position in
#sine wave
while True:
	print("Frame: " + str(counter))
	for x in range(numLEDs):
		#intensity should be between -0 and 1 based on position * chunk of circle
		y = math.cos(math.radians((x + counter) * chunks))
		#Max value should be 255, so 1*255
		intensity = y * 255
		#Print Light values if needed
		print("LIGHT: " + str(x) + " VALUE: " + str(y))
		pixels = [ (0,0,0) ] * numLEDs
		pixels[x] = (intensity, intensity, intensity)
		client.put_pixels(pixels)
		#Debug: xvalues.append(x)
		#Debug: values.append(y)
		#print(str(x) + "," + str(y))
	counter = counter + 1
	#Debugging: plt.plot(xvalues,yvalues)
	#Debugging: plt.show()
	#Reduce this value to animate faster
	time.sleep(1)
