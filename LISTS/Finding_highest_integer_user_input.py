input_string = input('Enter elements of a list separated by space ')
print("\n")
hetero_list = input_string.split()
# print list
print('list: ', hetero_list)

# convert each item to int type
#for i in range(len(hetero_list)):

#error for i in hetero_list:
for i in range(len(hetero_list)):
    # convert each item to int type
    try:
        hetero_list[i] = int(hetero_list[i])
    except ValueError as e:
        print("encountered a non integer input")

max = 0
sim_pos=[]

for j in range(len(hetero_list)):
    if (type(hetero_list[j])==int):
        if hetero_list[j]>max:
            max=hetero_list[j]
            #print(j)

for j in range(len(hetero_list)):
    if (type(hetero_list[j])==int):
        if hetero_list[j]==max:
            sim_pos.append(j)





print("max", max)
print("positions", sim_pos)



print(hetero_list)

# Calculating the sum of list elements
#print("Sum = ", sum(user_list))