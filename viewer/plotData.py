#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

class PlotData(object):
	
	def __init__(self,\
	plotType="simple",\
	parentName=None,\
	name=None,\
	y=None,\
	x=None):
		
		self.plotType = plotType
		self.parentName = parentName
		self.name = name
		self.y = y
		self.x = x
		
		if (self.checkData()==False):
			self.help()
			self.isValid = False
		else:
			self.isValid = True
		
	def help(self):
		
		print "Error in string of type " + self.plotType
		
		print "string must have one of the following format :"
		print "-----------------------------------------------"
		print "		pySimplePlot <name> <y> <x>"
		print "		pySubPlot <parentName> <name> <y> <x>"
		print "		pyMultiPlot <parentName> <name> <y> <x> (in implementation)"
		print "-----------------------------------------------"
		
	def checkData(self):
		
		if ((self.plotType == "simple") and (self.name != None) and (self.y != None) and (self.x != None)):
			return 1
			
		if ((self.plotType == "sub") and (self.parentName != None) and (self.name != None) and (self.y != None) and (self.x != None)):
			return 1
			
		if ((self.plotType == "multi") and (self.parentName != None) and (self.name != None) and (self.y != None) and (self.x != None)):
			return 1
			
		return 0
	
	
