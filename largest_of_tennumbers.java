numbers = int(input("Enter number: "))
counter = 0
largest = numbers

while counter < 10:
	
	if largest > numbers:
		largest = numbers
		
print(f"{largest} {counter}")
	counter+=1