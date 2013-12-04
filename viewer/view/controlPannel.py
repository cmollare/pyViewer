#!/usr/bin/python2.7
# -*-coding:Latin-1 -*

from Tkinter import *

class ControlPannel():
	
	def __init__(self):
		self.mainWin = Tk()
		
		self.mainFrame = Canvas(self.mainWin, width=512, height=640, borderwidth=1, background='#E4E4E4')
		self.recordFrame = Canvas(self.mainFrame, width=256, height=640, borderwidth=1, background='#FFFFFF')
		self.displayFrame = Canvas(self.mainFrame, width=256, height=640, borderwidth=1, background='#FFFFFF')
		self.quitButton = Button(self.mainFrame, text="Quitter", command=self.quit)
		self.updateButton = Button(self.mainFrame, text="Update", command=self.update)
		
		
		self.mainFrame.pack(fill='both')
		self.recordFrame.grid(row=1, column=2)
		self.displayFrame.grid(row=1, column=1)
		self.updateButton.grid(row=2, column=1)
		self.quitButton.grid(row=2, column=2)
		
	def quit(self):
		self.mainWin.destroy()
		pass
	
	def update(self):
		pass
		
	def main(self):
		self.mainWin.mainloop()
		

if __name__ == '__main__':
	test = ControlPannel()
	test.main()
