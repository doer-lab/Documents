# coding = utf-8

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("First number:")
	if first_number == 'q':
		break
	second_number = input("Second number:")
	if second_number == 'q':
		break
	
	try:
		answer = int(first_number)/int(second_number)          # maybe raise error
	except ZeroDivisionError:
		print("You can't divide by 0!")
		break
	else:
		print(answer)
		break