#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from collections import deque
import os

class PlotBuffer(object):
	
	def __init__(self, buffSize):
		
		self.buffSize = buffSize #size of buffers
		self.plotTypes = [] #type of plot (simple, multi, etc...)
		self.parentNames = [] #name of parent figure
		self.bufNames = [] #name of plot
		self.ybufs = [] #y values
		self.xbufs = [] #x values
		self.numSamples = [] #num of values added
		try:
			os.remove('data.plt')
		except OSError:
			pass

	
	def addToBuf(self, plotData):
		
		i = self.retrieveBufInd(plotData.name)
		self.numSamples[i] += 1
		self.ybufs[i].append(plotData.y)
		if plotData.x == None: #if we don't specify x coords
			plotData.x=self.numSamples[i]
		self.xbufs[i].append(plotData.x)
		
	
	def add(self, plotData):
		#add current data to buffer
		#if it does not exist, it creates it
		self.addToFile(plotData)#write in file
		
		if plotData.isValid:
			if self.isBufExist(plotData.name):
				self.addToBuf(plotData)
			else:
				self.createNewBuffer(plotData)
				self.addToBuf(plotData)
		
	def createNewBuffer(self, plotData):
		self.bufNames.append(plotData.name)
		self.plotTypes.append(plotData.plotType)
		self.parentNames.append(plotData.parentName)
		self.ybufs.append(deque([0.0]*self.buffSize, self.buffSize))
		self.xbufs.append(deque([0.0]*self.buffSize, self.buffSize))
		self.numSamples.append(0);
	
	def isBufExist(self, name):
		return name in self.bufNames
	
	def retrieveBufInd(self, name):
		return self.bufNames.index(name)
		
	def numBuffers(self):
		return len(self.bufNames)
		
	def addToFile(self, plotData):
		self.fileData = open('data.plt', 'a')
		stringToWrite=''
		if (plotData.plotType == "simple"):
			stringToWrite = "pySimplePlot " + plotData.name + " "
		elif (plotData.plotType == "sub"):
			stringToWrite = "pySubPlot " + plotData.parentName + " " + plotData.name + " "
		elif (plotData.plotType == "multi"):
			stringToWrite = "pyMultiPlot " + plotData.parentName + " " + plotData.name + " "
		
		stringToWrite += str(plotData.y) + " " + str(plotData.x) + " \n"
		self.fileData.write(stringToWrite)
		self.fileData.close()
