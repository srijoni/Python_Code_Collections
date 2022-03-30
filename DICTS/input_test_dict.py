# Creates key, value for dict based on user input
# Combine with loops to avoid manual repetition

test_dict = dict()
strs = input("Enter key values pairs -- User1:65 User2:87 ")

for temp in strs.split():
	#print(temp)
	key_val= temp.split(':')
	try:
		test_dict[key_val[0]] = float(key_val[1])
		#print(type(dict))
	except ValueError as e:
		print("encountered non integer input")
		test_dict[key_val[0]] = (key_val[1])


  
print(test_dict) 

