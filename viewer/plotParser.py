#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from plotData import *

class PlotParser(object):
	
	def __init__(self, string):
		self.string = string
		self.parseLine(string)
		
	def getPlotData(self):
		return self.plotData

	def parseLine(self, string):
		#find the "py..." command
		if (string.find("pySimplePlot") == 0):
			self.plotData = self.parseSimplePlot(string)
		elif (string.find("pySubPlot") == 0):
			self.plotData = self.parseSubPlot(string)
		elif (string.find("pyMultiPlot") == 0):
			self.plotData = self.parseMultiPlot(string)
		else:
			if (len(string) != 0):
				print string
			self.plotData = None
		
	def parseSimplePlot(self, string):
		cont = string.split(" ")
		if len(cont) != 5:
			return None
		return PlotData(plotType="simple", name=cont[1], y=eval(cont[2]), x=eval(cont[3]))
		
	def parseSubPlot(self, string):
		if len(cont) != 6:
			return None
		return PlotData(plotType="sub", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=eval(cont[4]))
	
	def parseMultiPlot(self, string):
		if len(cont) != 6:
			return None
		return PlotData(plotType="multi", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=eval(cont[4]))
	
	
