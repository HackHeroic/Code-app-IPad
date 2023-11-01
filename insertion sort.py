def swap(given_list,item):
    temp = given_list[item]
    given_list[item] = given_list[item+1]
    given_list[item+1] = temp

def insert_sort(given_list):
    for item in range(len(given_list)-1):
        if given_list[item+1] < given_list[item]:
            swap(given_list,item)
    return given_list
print(insert_sort([78,59,62,89,90]))

    
