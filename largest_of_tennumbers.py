numbers = int(input("Enter number: "))
counter = 0
largest = numbers

while counter < 10:
	numbers = int(input("Enter number: "))
	if largest > numbers:
		largest = numbers
	counter+=1	
print(f"{largest} {counter}")
