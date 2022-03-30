# Creates key, value for dict based on user input
# Combine with loops to avoid manual repetition

test_dict = dict()
strs = input("Enter key values pairs -- User1:65 User2:87 ")

for temp in strs.split():
    print(temp)
    key_val= temp.split(':')
    try:
        test_dict[key_val[0]] = float(key_val[1])
        #print(type(dict))
    except ValueError as e:
        print("encountered non integer input")
        test_dict[key_val[0]] = (key_val[1])


  
print(test_dict) 

#for item, key1 in test_dict.items():
    #print(type(key1))
    #for key, value in item.iteritems():


values=list()
for d in test_dict.values():
    if (type(d)== float):
        values.append(d)



max = 0
sim_pos=[]

for j in range(len(values)):

    if values[j]>max:
        max=values[j]

print (max)

for key, value in test_dict.items():
    if (type(value)==float):
        if (value == max):
            print (" The key", key, "is assigned to the maximum value", max)



      #  print(key)



# print(strs.splitlines())

# d = dict(x.split() for x in strs.splitlines())

# print(d)




# class_list = dict()
# data = input('Enter name & score separated by ":" ')
# temp = data.split(':')
# print(temp)
# print(temp[0])
# print(temp[1])
# temp[0]=int(temp[0])
# class_list[temp[0]] = temp[1]
# print(type(temp[0]))
# print(type(temp[1]))
# OR

# key = input("Enter key") 
# value = input("Enter value") 
# class_list[key] = [value]