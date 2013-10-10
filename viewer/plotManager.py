#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

import plotBuffer
from collections import defaultdict
from matplotlib import pyplot as plt

class PlotManager(object):
	
	def __init__(self):
		
		self.numPlots=0
		self.numWindows=0
		self.figList = defaultdict(list)
		plt.ion()
		
	def update(self, plotBuffer):
		
		numCurrentBufs=0
		buf = plotBuffer
		
		if plotBuffer.numBuffers() > 0:
			for plotType, xbuf, ybuf, name, parentName in zip(buf.plotTypes, buf.xbufs, buf.ybufs, buf.bufNames, buf.parentNames):
				if len(self.figList[parentName])==0:
					#windows does not exist, we have to create it
					self.createFigure(plotType, parentName, name, ybuf, xbuf)
					self.figList[parentName].append(name)
				elif not (name in self.figList[parentName]):
					#windows exist but a new curve have to be displayed
					self.addPlotToFigure(plotType, parentName, name, ybuf, xbuf)
					self.figList[parentName].append(name)
				else:
					#just update existing curves
					self.updateCurve(plotType, parentName, name, ybuf, xbuf)
					pass
					#print self.figList
					
			plt.draw()
					
	def createFigure(self, plotType, parentName, name, ybuf, xbuf):
		if plotType == "simple":
			fig = plt.figure(name)
			plt.ylim([-10, 10])
			plt.plot(xbuf, ybuf, label=name)
			axis = plt.gca()
			axis.set_autoscale_on(True)
			axis.autoscale_view(True,True,True)
		
		elif (plotType == "sub") or (plotType == "multi"):
			fig = plt.figure(parentName)
			ax = fig.add_subplot(111)
			ax.plot(xbuf, ybuf, label=name)
			axis = plt.gca()
			axis.set_autoscale_on(True)
			axis.autoscale_view(True,True,True)
		
		plt.legend()
			
		
	def addPlotToFigure(self, plotType, parentName, name, ybuf, xbuf):
		if plotType == "simple":
			self.createFigure(plotType, parentName, name, ybuf, xbuf)
			
		elif plotType == "sub":
			fig = plt.figure(parentName)
			nbsub = len(fig.axes)
			for i in range(nbsub):
				fig.axes[i].change_geometry(nbsub+1, 1, i+1)
			
			ax = fig.add_subplot(nbsub+1, 1, nbsub+1)
			ax.plot(ybuf, xbuf, label=name)
			
		elif plotType == "multi":
			fig = plt.figure(parentName)
			plt.plot(ybuf, xbuf, label=name)
		
		plt.legend()
			
	def updateCurve(self, plotType, parentName, name, ybuf, xbuf):
		if plotType == "simple":
			fig = plt.figure(name)
			fig.axes[0].lines[0].set_data(xbuf, ybuf)
			axes = plt.gca()
			axes.relim()
			axes.autoscale_view(True,True,True)
		
		elif (plotType == "sub"):
			fig = plt.figure(parentName)
			#find the number of the axis in the figure
			index = self.figList[parentName].index(name)
			
			#update
			axes = fig.axes[index]
			axes.lines[0].set_data(xbuf, ybuf)
			axes.relim()
			axes.autoscale_view(True,True,True)
			
		elif plotType == "multi":
			fig = plt.figure(parentName)
			index = self.figList[parentName].index(name)
			axes = fig.axes[0]
			axes.lines[index].set_data(xbuf, ybuf)
			axes.relim()
			axes.autoscale_view(True,True,True)

	
		
