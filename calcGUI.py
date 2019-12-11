import tkinter as tk

def calc(num1, num2, operator):
	if operator == "+":
		out = num1 + num2
	elif operator == "-":
		out = num1 - num2
	elif operator == "*":
		out = num1 * num2
	elif operator == "/":
		out = num1 / num2
	elif operator == "=":
		out = num1
	return out

class calcGUI:
	global result
	global screen
	global operator
	result = int(0)
	screen = ""
	operator = ""
	def __init__(self, master):
		self.master = master
		master.title("My Calc")

		self.label = tk.Label(master, 
								text = result, 
								height = 2,
								font='Helvetica 12 bold')
		self.label.grid(row = 0, columnspan = 4)
		
		self.seven_button = tk.Button(master, 
										text = "7", 
										command = self.seven, 
										height = 2, 
										width = 3)
		self.seven_button.grid(row = 1, column = 0)
		
		self.eight_button = tk.Button(master, 
										text = "8", 
										command = self.eight,
										height = 2,
										width = 3)
		self.eight_button.grid(row = 1, column = 1)
		
		self.nine_button = tk.Button(master, 
										text = "9", 
										command = self.nine,
										height = 2,
										width = 3)
		self.nine_button.grid(row = 1, column = 2)
		
		self.add_button = tk.Button(master, 
										text = "+", 
										command = self.add,
										height = 2,
										width = 3)
		self.add_button.grid(row = 1, column = 3, padx = 10)
		
		self.four_button = tk.Button(master, 
										text = "4", 
										command = self.four,
										height = 2,
										width = 3)
		self.four_button.grid(row = 2, column = 0)
		
		self.five_button = tk.Button(master, 
										text = "5", 
										command = self.five,
										height = 2,
										width = 3)
		self.five_button.grid(row = 2, column = 1)
		
		self.six_button = tk.Button(master, 
										text = "6", 
										command = self.six,
										height = 2,
										width = 3)
		self.six_button.grid(row = 2, column = 2)
		
		self.subtract_button = tk.Button(master, 
										text = "-", 
										command = self.subtract,
										height = 2,
										width = 3)
		self.subtract_button.grid(row = 2, column = 3, padx = 10)
		
		self.one_button = tk.Button(master, 
										text = "1", 
										command=self.one,
										height = 2,
										width = 3)
		self.one_button.grid(row = 3, column = 0)
		
		self.two_button = tk.Button(master, 
										text = "2", 
										command = self.two,
										height = 2,
										width = 3)
		self.two_button.grid(row = 3, column = 1)
		
		self.three_button = tk.Button(master, 
										text = "3", 
										command = self.three,
										height = 2,
										width = 3)
		self.three_button.grid(row = 3, column = 2)
		
		self.multiply_button = tk.Button(master, 
										text = "*", 
										command = self.multiply,
										height = 2,
										width = 3)
		self.multiply_button.grid(row = 3, column = 3, padx = 10)
		
		self.zero_button = tk.Button(master, 
										text = "0", 
										command = self.zero,
										height = 2,
										width = 8)
		self.zero_button.grid(row = 4, column = 0, columnspan = 2)
		
		self.period_button = tk.Button(master, 
										text = ".", 
										command = self.period,
										height = 2,
										width = 3)
		self.period_button.grid(row = 4, column = 2)
		
		self.divide_button = tk.Button(master, 
										text = "/", 
										command = self.divide,
										height = 2,
										width = 3)
		self.divide_button.grid(row = 4, column = 3, padx = 10)
		
		self.clear_button = tk.Button(master, 
										text = "CE", 
										command = self.clear,
										height = 2,
										width = 12)
		self.clear_button.grid(row = 5, columnspan = 3, pady = 10)
		
		self.equal_button = tk.Button(master, 
										text = "=", 
										command = self.equal,
										height = 2,
										width = 3)
		self.equal_button.grid(row = 5, column = 3, padx = 10, pady = 10)
		
		#self.close_button = tk.Button(master, text="Close", command=master.quit)
		#self.close_button.grid()

	def one(self):
		global screen
		screen = screen + "1"
		self.label.config(text=screen)
		
	def two(self):
		global screen
		screen = screen + "2"
		self.label.config(text=screen)
		
	def three(self):
		global screen
		screen = screen + "3"
		self.label.config(text=screen)
		
	def four(self):
		global screen
		screen = screen + "4"
		self.label.config(text=screen)
		
	def five(self):
		global screen
		screen = screen + "5"
		self.label.config(text=screen)
		
	def six(self):
		global screen
		screen = screen + "6"
		self.label.config(text=screen)
		
	def seven(self):
		global screen
		screen = screen + "7"
		self.label.config(text=screen)
		
	def eight(self):
		global screen
		screen = screen + "8"
		self.label.config(text=screen)
		
	def nine(self):
		global screen
		screen = screen + "9"
		self.label.config(text=screen)
		
	def zero(self):
		global screen
		screen = screen + "0"
		self.label.config(text=screen)
		
	def period(self):
		global screen
		screen = screen + "."
		self.label.config(text=screen)
		
	def add(self):
		global screen
		global result
		global operator
		if operator in ["+", "-", "*", "/"]:
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		elif operator == "":
			result = float(screen)
		screen = ""
		operator = "+"
		
	def subtract(self):
		global screen
		global result
		global operator
		if operator in ["+", "-", "*", "/"]:
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		elif operator == "":
			result = float(screen)
		screen = ""
		operator = "-"
		
	def multiply(self):
		global screen
		global result
		global operator
		if operator in ["+", "-", "*", "/"]:
			result = calc(result, float(screen), operator)
			self.label.config(text=result)
		elif operator == "":
			result = float(screen)
		screen = ""
		operator = "*"
		
	def divide(self):
		global screen
		global result
		global operator
		if operator in ["+", "-", "*", "/"]:
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		elif operator == "":
			result = float(screen)
		screen = ""
		operator = "/"
		
	def equal(self):
		global screen
		global result
		global operator
		if operator != "":
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		else:
			result = int(screen)
		screen = ""
		operator = "="
		self.label.config(text=result)
		
	def clear(self):
		global screen
		global result
		global operator
		screen = ""
		result = ""
		operator = ""
		self.label.config(text=result)


root = tk.Tk()
my_gui = calcGUI(root)
root.mainloop()