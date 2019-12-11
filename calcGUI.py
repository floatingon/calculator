import tkinter as tk

def calc(num1, num2, operator):
	if operator == "+":
		out = num1 + num2
	if operator == "-":
		out = num1 - num2
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

		self.label = tk.Label(master, text=result)
		self.label.grid(row=0)
		
		self.one_button = tk.Button(master, text="1", command=self.one)
		self.one_button.grid(row=1, column=0)
		
		self.two_button = tk.Button(master, text="2", command=self.two)
		self.two_button.grid(row=1, column=1)
		
		self.three_button = tk.Button(master, text="3", command=self.three)
		self.three_button.grid(row=1, column=2)
		
		self.four_button = tk.Button(master, text="4", command=self.four)
		self.four_button.grid(row=2, column=0)
		
		self.five_button = tk.Button(master, text="5", command=self.five)
		self.five_button.grid(row=2, column=1)
		
		self.six_button = tk.Button(master, text="6", command=self.six)
		self.six_button.grid(row=2, column=2)
		
		self.seven_button = tk.Button(master, text="7", command=self.seven)
		self.seven_button.grid(row=3, column=0)
		
		self.eight_button = tk.Button(master, text="8", command=self.eight)
		self.eight_button.grid(row=3, column=1)
		
		self.nine_button = tk.Button(master, text="9", command=self.nine)
		self.nine_button.grid(row=3, column=2)
		
		self.zero_button = tk.Button(master, text="0", command=self.zero)
		self.zero_button.grid(row=4, column=1)
		
		self.add_button = tk.Button(master, text="+", command=self.add)
		self.add_button.grid(row=1, column=3)
		
		self.subtract_button = tk.Button(master, text="-", command=self.subtract)
		self.subtract_button.grid(row=2, column=3)
		
		self.equal_button = tk.Button(master, text="=", command=self.equal)
		self.equal_button.grid(row=3, column=3)
		
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
	def add(self):
		global screen
		global result
		global operator
		if operator != "":
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		else:
			result = int(screen)
		screen = ""
		operator = "+"
		
	def subtract(self):
		global screen
		global result
		global operator
		if operator != "":
			result = calc(result, int(screen), operator)
			self.label.config(text=result)
		else:
			result = int(screen)
		screen = ""
		operator = "-"
		
	def equal(self):
		global screen
		global result
		global operator
		if operator == "+":
			result = result + int(screen)
		if operator == "-":
			result = result - int(screen)
		self.label.config(text=result)


root = tk.Tk()
my_gui = calcGUI(root)
root.mainloop()