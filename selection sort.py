def selectiion_sort(given_list):
    for i in range(len(given_list)-1):
        min_element_index = i
        for j in range(i+1,len(given_list)):
            if given_list[j] < given_list[min_element_index]:
                min_element_index = j
        given_list[i],given_list[min_element_index] = given_list[min_element_index],given_list[i]
    return given_list
print(selectiion_sort([5,4,1,3,2,]))
