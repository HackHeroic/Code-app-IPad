def find_max(given_list):
    max_element = given_list[0]
    for i in range(1,len(given_list)):
        if given_list[i] > max_element:
            max_element = given_list[i]
    return max_element

print(find_max([1,2,3,4,5]))

def find_second_max(given_list):
    max_element = find_max(given_list)
    given_list.remove(max_element)
    second_max_element = find_max(given_list)
    return second_max_element

print(find_second_max([1,2,3,4,5]))

def find_third_max(given_list):
    second_max_element = find_second_max(given_list)
    given_list.remove(second_max_element)
    third_max_element = find_max(given_list)
    return third_max_element

print(find_third_max([6,7,89,1,67,85]))


