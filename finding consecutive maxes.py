def find_max(given_list):
    max_element = given_list[0]
    for i in range(1,len(given_list)):
        if given_list[i] > max_element:
            max_element = given_list[i]
    return max_element

def find_second_max(given_list):
    max_element = find_max(given_list)
    given_list.remove(max_element)
    print(given_list)
    second_max_element = find_max(given_list)
    return second_max_element

def find_third_max(given_list):
    second_max_element = find_second_max(given_list)
    print(given_list)
    third_max_element = find_max(given_list)
    return third_max_element

A = list(map(int,input().split()))

print(find_max(A))
print(find_second_max(A))
print(find_third_max(A))




# T = int(input())

# while T >0:
#     N = int(input())
#     A = list(map(int,input().split()))
#     print(find_max(A),end = " ")
#     print(find_second_max(A),end = " ")
#     print(find_third_max(A))
#     T = T - 1
    

