#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from collections import deque
import plotData

class PlotBuffer(object):
	
	def __init__(self, buffSize):
		
		self.buffSize = buffSize
		self.plotTypes = []
		self.parentNames = []
		self.bufNames = []
		self.ybufs = []
		self.xbufs = []
	
	def addToBuf(self, plotData):
		
		i = self.retrieveBufInd(plotData.name)
		self.ybufs[i].append(plotData.y)
		self.xbufs[i].append(plotData.x)
	
	def add(self, plotData):
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
	
	def isBufExist(self, name):
		return name in self.bufNames
	
	def retrieveBufInd(self, name):
		return self.bufNames.index(name)
		
	def numBuffers(self):
		return len(self.bufNames)
