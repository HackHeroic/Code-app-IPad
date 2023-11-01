n,h0,a,c,q = map(int,input().split())
my_height_list = []
for i in range(n):
    if i == 0 :
        my_height_list.append(h0)
    else:
        height_of_ith = (a*my_height_list[-1] + c)%q
        my_height_list.append(height_of_ith)
# print(my_height_list)
count = 0
for i in range(len(my_height_list)):
    if i == 0:
        count += 1
    elif my_height_list[i] > my_height_list[i-1]:
        count += 1
    elif i < i -1:
        my_sliced_list = my_height_list[i:0:-1]
        for j in range(len(my_sliced_list)):
            if my_sliced_list[j] <= my_sliced_list[j+1]:
                count += 1
            elif my_sliced_list[j] > my_sliced_list[j+1]:
                break
print(count) 










     

    

    



















# if person == 0 :
#         return h0
#     height_person = (a*(height_calc(a,person-1,c,q)) + c)%q