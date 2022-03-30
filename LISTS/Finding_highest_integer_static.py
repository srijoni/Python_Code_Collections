
hetero_list = [4, 7, 8, 8]

def maximum_list(hetero_list):

    max1 = 0
    sim_pos=[]

    for j in range(len(hetero_list)):

        if hetero_list[j]>max1:

            max1=hetero_list[j]
            #print(j)

    for j in range(len(hetero_list)):

        if hetero_list[j]==max1:

            sim_pos.append(j)
    return max1, sim_pos




max1, sim_pos = maximum_list(hetero_list)

print("max", max1)
print("positions", sim_pos)



print(hetero_list)

# Calculating the sum of list elements
#print("Sum = ", sum(user_list))