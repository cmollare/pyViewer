#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from __future__ import print_function #for using print(string, end='') (remove \n at the end)

class PlotParser(object):
	
	def __init__(self, string):
		self.string = string
		self.parseLine(string)
		
	def getPlotData(self):
		return self.plotData

	def parseLine(self, string):
		#find the "py..." command
		if (string.find("pySimplePlot") == 0):
			#print string
			self.plotData = self.parseSimplePlot(string)
		elif (string.find("pySubPlot") == 0):
			#print string
			self.plotData = self.parseSubPlot(string)
		elif (string.find("pyMultiPlot") == 0):
			#print string
			self.plotData = self.parseMultiPlot(string)
		else:
			#print the original string if not known
			if (len(string) != 0):
				print(string, end=' ')
			self.plotData = None
			
################## parsing fuctions ###########################################################
		
	def parseSimplePlot(self, string):
		cont = string.split(" ")
		if len(cont) == 5:
			return PlotData(plotType="simple", name=cont[1], y=eval(cont[2]), x=eval(cont[3]))
		elif len(cont) == 4:
			return PlotData(plotType="simple", name=cont[1], y=eval(cont[2]), x=None)
		else:
			return None
		
	def parseSubPlot(self, string):
		cont = string.split(" ")
		if len(cont) == 6:
			return PlotData(plotType="sub", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=eval(cont[4]))
		elif len(cont) == 5:
			return PlotData(plotType="sub", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=None)
		else:
			return None
			
	def parseMultiPlot(self, string):
		cont = string.split(" ")
		if len(cont) == 6:
			return PlotData(plotType="multi", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=eval(cont[4]))
		elif len(cont) == 5:
			return PlotData(plotType="multi", parentName=cont[1], name=cont[2], y=eval(cont[3]), x=None)
		else:
			return None
	
	
