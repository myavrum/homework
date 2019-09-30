def even_or_odd(number):
	if number % 2 == 0:
		return "Even"
	return "Odd"

our_number = input("Enter a number ->")

print(even_or_odd(int(float(our_number))))