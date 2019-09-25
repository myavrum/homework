#How to use if statement.

PronType = str(input("Enter the type of Pronoun ->"))
Case = str(input("Enter the Case of Pronoun ->"))

if PronType == "Pers" and Case == "Gen":
	print("The Pronoun is Possesive")
	if PronType != "Pers" or Case == "Gen":
		print("The Pronoun is Genitive")
		if PronType == "Pers" or Case != "Gen":
			print("The Pronoun is Personal")
	print("Yes, the Pronoun is Possesive.")

print("Its not Poss Pronoun!")


weather = "cold"

a = 5
b = 3
message = "Hello, world!"

len_of_message = len(message)

if weather == "cold" and a > b and len_of_message > 3:
	print("Its work!")
	if b > 1:
		print("B is greater than 1")
	print("If statement ends there")

print("Our cods ends")


PronType = str(input("Enter the type of Pronoun ->"))
Case = str(input("Enter the Case of Pronoun ->"))

if PronType == "Pers" and Case == "Gen":
	print("The Pronoun is Possesive")

a = 5
b = 6
c = 2

if a < b:
	print("A is less than B")

if a > b:
	print("A is greather than B")

if a < b and c > 5:
	print("A is less or than B")

if a > b and c < 5:
	print("A is greather than B")

My_num1 = 5
My_num2 = 7
if My_num1 < My_num2:
	print("My_num2 is greater")
print("Execution complete")

