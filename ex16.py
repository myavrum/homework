#ex16
Beatles = {1: "Oh yeah, I'll tell you somethin'", 
			2: "I think you'll understand", 
			3: "When I say that somethin'",
			4: "I want to hold your hand", 
			5: "I want to hold your hand",
			6: "I want to hold your hand"}
while True:
	try:
		number = int(input("Enter a number -> "))
		print(Beatles[number])
		break
	except ValueError:
		print("Input a correct value -> ")
	except KeyError:
		print("Input a correct number-> ")