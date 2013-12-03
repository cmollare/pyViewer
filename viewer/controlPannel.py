#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from Tkinter import *

class ControlPannel():
	
	def __init__(self):
		self.mainWin = Tk()
		self.mainFrame=self.mainWin
		
		self.mainFrame = Frame(self.mainWin, width=512, height=640, borderwidth=1)
		self.mainFrame.pack(fill='both')
		#self.titleFrame = Frame(self.mainFrame
		
		self.recordFrame = Frame(self.mainFrame, width=256, height=300, borderwidth=1)
		self.recordFrame.pack(side='left')
		
		self.displayFrame = Frame(self.mainFrame, width=256, height=300, borderwidth=1)
		self.displayFrame.pack(side='left')
		
		self.quitButton = Button(self.mainFrame, text="Quitter", command=self.quit)
		self.quitButton.pack(side='bottom')
		
		self.updateButton = Button(self.mainFrame, text="Update", command=self.update)
		self.updateButton.pack(side='bottom')
		
		
		
		
	def quit(self):
		pass
	
	def update(self):
		pass
		
	def main(self):
		self.mainWin.mainloop()
		

if __name__ == '__main__':
	test = ControlPannel()
	test.main()
