#Selection sort
def selection_sort(given_list):
    for i in range(len(given_list)-1):
        min_element_index = i 
        for j in range(i+1,len(given_list)):
            if given_list[j] < given_list[min_element_index]:
                min_element_index = j
        given_list[i],given_list[min_element_index] = given_list[min_element_index],given_list[i]
    return given_list
print(selection_sort([5,4,3,2,1]))

#insertion sort
def swap(given_list,item):
    temp = given_list[item]
    given_list[item] = given_list[item+1]
    given_list[item+1] = temp

def insertion_sort(given_list):
    for item in range(len(given_list)-1):
        if given_list[item] > given_list[item+1]:
            swap(given_list,item)
    return given_list

print(insertion_sort([8,68,75,889,90]))


#bubble sort
def Bubble_sort(given_list):
    for i in range(len(given_list)-1):
        if given_list[i+1] < given_list[i]:
            given_list[i],given_list[i+1] = given_list[i+1],given_list[i]
    return given_list
print(Bubble_sort([67,5,69,7,70]))
