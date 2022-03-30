
hetero_dict = {'Student1': 45, 'Student2': 50, 'Student3': 74, 'Student4': 74, 'Student5': 96}


hetero_list=list()
for d in hetero_dict.values():
    if (type(d)== float or type(d) == int):
        hetero_list.append(d)

print(hetero_list)

def get_key(val):
    key1=[]
    for key, value in hetero_dict.items():
         if (type(value)== float or type(value) == int):
        #if (type(d)== float or type(d) == int):

            if val == value:
                key1.append(key)
    return key1




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

visited=[]
print("printing kth largest elements")
max_cnt=0
for i in range(k):
    cnt=0
    for j in visited:
        if hetero_list[i]==j:
            cnt=cnt+1
    if cnt==0:
        max_cnt=max_cnt+1
        visited.append(hetero_list[i])
        print(max_cnt,"th max value", hetero_list[i]," keys", get_key(hetero_list[i]))







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
