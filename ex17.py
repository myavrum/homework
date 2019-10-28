#ex17
x = {"key1": 1, "key2": 3, "key3": 2}
y = {"key1": 1, "key2": 2}

for key in x.keys():
	try:
		if y[key] == x[key]:
			print(key, " is present in both x and y")
	except KeyError:
		pass