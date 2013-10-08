#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

import random
from time import sleep
import numpy as np

def sample():
	return random.random()*50;

def sinus(freq):
	return np.sin(2*np.pi*freq*numIteration)
	
def display():

	string =  'pySubPlot lol plot1 ' + str(sinus(0.005)) + ' ' + str(numIteration) + ' '

	if numIteration > 20:
		string += '\npySubPlot lol plot2 ' + str(sinus(0.01)) + ' ' + str(numIteration) + ' '
		
	return string

def main():
	
	global numIteration
	numIteration=0
	print 'Starting server...'
	
	while True:
		try:
			print display()
			numIteration+=1
			#sleep(0.5)
		except KeyboardInterrupt:
			print 'Stopping server...'
			break
		
if __name__ == '__main__':
	main()
