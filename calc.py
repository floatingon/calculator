#Add
def add(num1,num2):
	return num1 + num2
#Subtract
def subtract(num1,num2):
	return num1 - num2
#Multiply
def multiply(num1,num2):
	return num1 * num2
#Divide
def divide(num1,num2):
	return num1 / num2
#Prompt the user for the first number
out = input("Enter a number: ")
out = float(out)
operator= ""
while operator not in ["C", "c"]:
	print("  (A)dd")
	print("  (S)ubtract")
	print("  (M)ultiply")
	print("  (D)ivide")
	print("  (C)alculate")
	operator = input("Select an option: ")
	if operator not in ["A", "a", "S", "s", "M", "m", "D", "d", "C", "c"]:
		print("Not a valid option")
		continue
	#TODO add input validation
	if operator not in ["C", "c"]:
		num = input("Enter a number: ")
		num = float(num)
		if operator in ["A", "a"]:
			out = out + num
		if operator in ["S", "s"]:
			out = out - num
		if operator in ["M", "m"]:
			out = out * num
		if operator in ["D", "d"]:
			out = out / num
		print(out)
print(out)