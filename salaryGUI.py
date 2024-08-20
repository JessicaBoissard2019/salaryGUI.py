"""
Program: salaryGUI.py
Jessica Boissard
8/13/2024

**NOTE: the module breezypythongui.py MUST be in the same directory as this file for the app to run correctly!

GUI-based application that calculates for hourly wage times hours
"""
# imports can go here
from breezypythongui import EasyFrame
from tkinter.font import Font

# Class header (class name will change project to project)
class SalaryCalculator(EasyFrame):

	# Definition of our classes' constructor method
	def __init__(self):
		# Call to the Easy Frame class constructor
		EasyFrame.__init__(self, title = "SalaryCalculator 2.0", background = "lightgreen")

		#Variable to store a font desing to use with multiple labels
		labelFont = Font(size = 14, family = "Georgia")

		#Add the widgets to the window
		self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, sticky = "NSEW", background = "lightgreen", font = Font(size = 22, family = "Impact"))

		self.addLabel(text = "Hourly wage:", row = 1, column = 0, background = "lightgreen", font = labelFont)

		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)

		self.addLabel(text = "Hours Worked:", row = 2, column = 0, background = "lightgreen", font = labelFont)

		self.hoursField = self.addFloatField(value = 0.0, row = 2, column = 1)

		#bind the hoursFiled to the press of the Enter key event
		self.hoursField.bind("<Return>", lambda event: self.compute())

		self.button = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)

		self.button["background"] = "firebrick"
		self.button["foreground"] = "white"
		self.button["width"] = 15
		
		self.addLabel(text = "Calculated salary is:", row = 4, column = 0, background = "lightgreen", font = labelFont)

		self.outputField = self.addFloatField(value = 0.0, row = 4, column = 1, state = "readonly", precision = 2)

	#Definition of the compute() function
	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.hoursField.getNumber()
		salary = wage * hours
		self.outputField.setNumber(salary)



# Global definition of the main() method
def main():
	# Instantiate an object from the class into mainloop()
	SalaryCalculator().mainloop()

# Global call to main() for program entry
if __name__ == '__main__':
	main()