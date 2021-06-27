def Factorial(number):
	if (number == 0):
		return 1
		
	return number * Factorial(number-1)
	
sequence = int(input())
print("Factorial of " + str(sequence) + " is ")
print(Factorial(sequence))