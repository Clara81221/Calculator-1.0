import time as t

# Addition section, used later

def addition():
	additionInput1 = input("Input the first number to add: ")
	additionInput2 = input("Input the second number to add: ")
	print()
	print(int(additionInput1) + int(additionInput2))
	t.sleep(2)
	start()

# Subtraction section, used later

def subtraction():
	subtractionInput1 = input("Input the first number to subtract: ")
	subtractionInput2 = input("Input the second number to subtract: ")
	print()
	print(int(subtractionInput1) - int(subtractionInput2))
	t.sleep(2)
	start()

# Multiplication section, used later

def multiplication():
	multiplicationInput1 = input("Input the first number to multiply: ")
	multiplicationInput2 = input("Input the second number to multiply: ")
	print()
	print(int(multiplicationInput1) * int(multiplicationInput2))
	t.sleep(2)
	start()

# Division section, used later

def division():
	divisionInput1 = input("Input the first number to divide: ")
	divisionInput2 = input("Input the second number to divide: ")
	print()
	print(int(divisionInput1) / int(divisionInput2))
	t.sleep(2)
	start()

# User inputs number for which task to complete

def start():
	print("Basic Calculator 0.1-b")
	print()
	print("""Input a number corresponding to the task
	1 Addition
	2 Subtraction
	3 Multiplication
	4 Division""")
	userInput = input("Input number: ")
	userInput = int(userInput)
	if userInput == 1:
		addition()
	if userInput == 2:
		subtraction()
	if userInput == 3:
		multiplication()
	if userInput == 4:
		division()

start()