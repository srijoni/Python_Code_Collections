
hetero_dict = {'Student1': 45, 'Student2': 50, 'Student3': 74, 'Student4': 74, 'Student5': 'P'}

values=list()
for d in hetero_dict.values():
    if (type(d)== float or type(d) == int):
        values.append(d)

print(values)

def get_key(val):
    key1=[]
    for key, value in hetero_dict.items():
         if (type(value)== float or type(value) == int):
        #if (type(d)== float or type(d) == int):

            if val == value:
                key1.append(key)
    return key1




def maximum_list(values):

    max1 = 0


    for j in range(len(values)):

        if values[j]>max1:

            max1=values[j]
            #print(j)


    return max1

max1 = maximum_list(values)


print("max value keys", get_key(max1))




# Calculating the sum of list elements
#print("Sum = ", sum(user_list))