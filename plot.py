#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from collections import deque
from matplotlib import pyplot as plt
import sys
import serial
import re
import threading
from time import sleep

class NumData:
	
	def __init__(self, buffSize):
		
		self.buffSize = buffSize
		self.bufNames = []
		self.ybufs = []
		self.xbufs = []
	
	def addToBuf(self, name, yval, xval):
		i = self.retrieveBufInd(name)
		self.ybufs[i].append(yval)
		self.xbufs[i].append(xval)
	
	def add(self, name, ydata, xdata):
		if self.isBufExist(name):
			self.addToBuf(name, ydata, xdata)
		else:
			self.createNewBuffer(name)
			self.addToBuf(name, ydata, xdata)
		
	def createNewBuffer(self, name):
		self.bufNames.append(name)
		self.ybufs.append(deque([0.0]*self.buffSize, self.buffSize))
		self.xbufs.append(deque([0.0]*self.buffSize, self.buffSize))
	
	def isBufExist(self, name):
		return name in self.bufNames
	
	def retrieveBufInd(self, name):
		return self.bufNames.index(name)
		
	def numBuffers(self):
		return len(self.bufNames)
	
	
class NumPlot:
	
	def __init__(self, numData):
		self.numWindows=0
		plt.ion() #interactive mode on
	
	def update(self, numData):
		
		numCurrentBufs=0
		
		if numData.numBuffers() >0:
			for xbuf, ybuf, name in zip(numData.xbufs, numData.ybufs, numData.bufNames):
				numCurrentBufs+=1
				if numCurrentBufs > self.numWindows:
					self.createNewPlot(name, xbuf, ybuf)
					self.numWindows+=1
				else:
					fig = plt.figure(name)
					fig.axes[0].lines[0].set_data(xbuf, ybuf)
					axes = plt.gca()
					axes.relim()
					axes.autoscale_view(True,True,True)
			plt.draw()
		
		
		
	def createNewPlot(self, name, xbuf, ybuf):
		fig = plt.figure(name)
		plt.ylim([-10, 10])
		axis = plt.plot(xbuf, ybuf)
		axis = plt.gca()
		axis.set_autoscale_on(True)
		axis.autoscale_view(True,True,True)
		

		
class Display:
	
	def __init__(self, serialBaud=None, serialPort=None):
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
		self.data = NumData(256)
		self.plot = NumPlot(self.data)
		self.readThread.start()
		
		while True:
			try:
				sleep(0.01)
				self.plot.update(self.data)

			except KeyboardInterrupt:
				self.readThread._Thread__stop()
				break
		
	def parseLine(self, string):
		#find the "py" command
		if (string.find("py") != 0) and (len(string) != 0) :
			print string
			return None
		
		#if py found, continue and parse
		cont = string.split(" ")
		
		#plot format : py name yaxis xaxis \n
		if len(cont) == 5:
			#print cont
			return cont[1], eval(cont[2]), eval(cont[3])
			
		#print cont
		#print "fail " + string
            
        
	#for reading stdin
	def readPipe(self):
		print 'start thread'
		while not self._stopEvent.isSet():
			sleep(0.0001)
			line = sys.stdin.readline()
			res = self.parseLine(line)
			if not (res == None):
				self.data.add(res[0], res[1], res[2])
				

		print 'exit thread'
	
	#for reading serial infos
	def readThread(self):
		print 'start thread'
		ser.Serial(self.serialPort, self.serialBaud)
		while not self._stopEvent.isSet():
			line = ser.readline()
			res = self.parseLine(line)
			if not (res == None):
				self.data.add(res[0], res[1], res[2])
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
	disp = Display()
	#------------------------
	
	disp.loop()
	

if __name__ == '__main__':
	main()

