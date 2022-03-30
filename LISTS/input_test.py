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
        print("error message")


for j in hetero_list:
    print(type(j))

print(hetero_list)

# Calculating the sum of list elements
#print("Sum = ", sum(user_list))