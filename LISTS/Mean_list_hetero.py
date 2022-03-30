
#hetero_list = [8, 1, 3, 9, 'i', 10]
hetero_list = [8, 1, 3, 9, 5.6, 10]
sum = 0
sim_pos=[]

ct = 0;
for j in range(len(hetero_list)):
    if (type(hetero_list[j])==int or  type(hetero_list[j])==float):
        sum =sum + hetero_list[j]
        ct = ct + 1

mean = sum/ct

print("mean", round(mean, 3))

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
