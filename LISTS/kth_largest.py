
hetero_list = [8, 1, 3, 9, 2, 10]
max = 0
sim_pos=[]

k = 4

print(hetero_list)

for j in range(len(hetero_list)):
    for i in range(j,len(hetero_list)):
        if hetero_list[j] < hetero_list[i]:
            #print("true")
            #print("hetero_list[j]",hetero_list[j])
            #print("hetero_list[i]",hetero_list[i])
            temp = hetero_list[i]
            hetero_list[i] =  hetero_list[j]
            hetero_list[j] = temp
            #print("hetero_list_i", hetero_list)


print("printing kth largest elements")
for i in range(k):
    print(hetero_list[i])






# Calculating the sum of list elements
#print("Sum = ", sum(user_list))




# for j in range(len(hetero_list)):
#     print("hetero_list_j", hetero_list)
#     print("j loops", j)
#     for i in range(j,len(hetero_list)):
#         print("i loops", i)
#         print(hetero_list[j])
#         if hetero_list[j] < hetero_list[i]:
#             print("i loops inside", i)
#             #print("true")
#             #print("hetero_list[j]",hetero_list[j])
#             #print("hetero_list[i]",hetero_list[i])
#             temp = hetero_list[i]
#             hetero_list[i] =  hetero_list[j]
#             hetero_list[j] = temp
#             print("hetero_list_i", hetero_list)