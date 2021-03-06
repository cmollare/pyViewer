#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from viewer import *
import sys
import serial
import re
import threading
from time import sleep

class App:
	
	def __init__(self, serialBaud=None, serialPort=None, displayPeriod=0.005, readingPeriod=0.0001, buffSize=500):
		self.displayPeriod=displayPeriod #display period (1/freq)
		self.readingPeriod=readingPeriod #reading thread period
		self.buffSize=buffSize #size of Buffers
		
		self.run = True
		if (serialBaud != None) and (serialPort != None):
			print 'serial mode'
			self.serialBaud = serialBaud
			self.serialPort = serialPort
			self.readThread = threading.Thread(None, self.readThread)
		else:
			print 'pipeline mode'
			self.readThread = threading.Thread(None, self.readPipe)
			
		self._stopEvent = threading.Event()
		
	def loop(self):
		self.buffers = PlotBuffer(self.buffSize) #plot data
		self.plotManager = PlotManager() #display interface
		self.readThread.start() #start reading thread
		
		#display loop
		while True:
			try:
				sleep(self.displayPeriod) #display period
				self.plotManager.update(self.buffers)

			except KeyboardInterrupt:
				self.readThread._Thread__stop()
				break
        
	#for reading stdin
	def readPipe(self):
		print 'start thread'
		while not self._stopEvent.isSet():
			sleep(self.readingPeriod)
			line = sys.stdin.readline()
			res = PlotParser(line).getPlotData()
			if not (res == None):
				self.buffers.add(res)
				

		print 'exit thread'
	
	#for reading serial infos
	def readThread(self):
		print 'start thread'
		ser.Serial(self.serialPort, self.serialBaud)
		while not self._stopEvent.isSet():
			line = ser.readline()
			res = PlotParser(line).getPlotData()
			if not (res == None):
				self.data.add(res)
		print 'end thread'
		
		ser.flush()
		ser.close()
		
def main():
	
	
	print 'plotting....'
	
	#uncomment what you need
	#------------------------
	#for serial port:
	#disp = Display(serialBaud=9600, serialPort=None)
	#for pipeline:
	app = App()
	#------------------------
	
	app.loop()
	

if __name__ == '__main__':
	main()
