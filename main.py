''' 
///////////// Garage /////////////
——————————————————————————————————
- free_spaces
——————————————————————————————————
+ enterGarage()  > decrease free_spaces
+ leaveGarage()  > increase free_spaces
+ updateGUI()    > update: text, progress bar, such
'''

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk


MAX_SPACES = 20

class Garage:
	filled_spaces = 0
	
	def enterGarage(self):
		if self.filled_spaces >= MAX_SPACES:
			return
		self.filled_spaces += 1
		self.updateGUI()

	def leaveGarage(self):
		if self.filled_spaces <= 0:
			return
		self.filled_spaces -= 1
		self.updateGUI()

	def updateGUI(self):
		main_txt.configure(text=f"Filled Parking Spots: {self.filled_spaces}/{MAX_SPACES}")
		bar['value'] = self.filled_spaces * (100/MAX_SPACES)

garage = Garage()


win = Tk()
win.title("Parking Garage App")
win.geometry('600x580')


main_txt = Label(win, text=f"Filled Parking Spots: 0/{MAX_SPACES}", pady=20)
main_txt.grid(column=0, row=0, columnspan=2)

bar = Progressbar(win, length=600)
bar['value'] = 0
bar.grid(column=0, row=1, columnspan=2)

enter_garage_btn = Button(win, text="Enter Garage", command=garage.enterGarage)
enter_garage_btn.grid(column=0, row=2)
leave_garage_btn = Button(win, text="Leave Garage", command=garage.leaveGarage)
leave_garage_btn.grid(column=1, row=2, pady=10)

win.mainloop()