
hetero_dict = {'Student1': 99, 'Student2': 50, 'Student3': 74, 'Student4': 74, 'Student5': 96}


hetero_list=list()
for d in hetero_dict.values():
        hetero_list.append(d)

print(hetero_list)







for j in range(len(hetero_list)):
    for i in range(len(hetero_list)):
        if hetero_list[j] < hetero_list[i]:
            #print("true")
            #print("hetero_list[j]",hetero_list[j])
            #print("hetero_list[i]",hetero_list[i])
            temp = hetero_list[i]
            hetero_list[i] =  hetero_list[j]
            hetero_list[j] = temp
            #print("hetero_list_i", hetero_list)





print(hetero_list)
key_list=list(hetero_dict.keys())
for j in hetero_list:
    print(j)
    print(key_list[hetero_list.index(j)])
    #print("key", hetero_dict[hetero_list.index(j)], "values", j)

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
