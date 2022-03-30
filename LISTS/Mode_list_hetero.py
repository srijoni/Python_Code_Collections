
#hetero_list = [8, 1, 3, 9, 'i', 10]


from Finding_highest_integer_static import *

hetero_list = [2.3, 2.3, 3, 4, 4, 4, 8,8, 9, 7, 8]


hetero_dict=dict()
visited=[]
for j in range(len(hetero_list)):
    if (type(hetero_list[j])==int or  type(hetero_list[j])==float):
        cnt=1
        for i in range(j+1, len(hetero_list)):
            if (type(hetero_list[i])==int or  type(hetero_list[i])==float):

                if (hetero_list[i] == hetero_list[j]):
                    print("inside loop")
                    print("hetero_list[i]", hetero_list[i])
                    print("hetero_list[j]", hetero_list[j])
                    cnt=cnt+1
        if(cnt>1):
            visit_cnt=0
            for w in visited:
                if (hetero_list[j]==w):
                    visit_cnt=visit_cnt+1
                    break
            if (visit_cnt==0):

                visited.append(hetero_list[j])

                hetero_dict[hetero_list[j]]=cnt

values=[]  
for d in hetero_dict.values():
    values.append(d)
print(values)
max, sim_pos=maximum_list(values)
print(hetero_dict)  
print(max) 


for key, value in hetero_dict.items():
    if value==max:
        print("Found Mode ->", key, " with frequency of operation=", value)









 