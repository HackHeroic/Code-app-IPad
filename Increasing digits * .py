N = int(input())
def bob_likes_the_number(number):
    string_number = str(number)              # same idea of max nos is used
    current_max = int(string_number[0])
    for current_num in string_number[1:]:
        if int(current_num) <= current_max:
            return False
        else:
            current_max = current_num
    return True
counter = 0
for number in range(1,N+1,1):
    if bob_likes_the_number(number):
        counter += 1
print(counter)

#sir's method
# def get_list_of_digits(number):
#     my_digits = []
#     while number > 0:
#         digit = number % 10
#         number = number // 10
#         my_digits.append(digit)
#     return my_digits

    
#     my_digits = get_list_of_digits(number)
#     for index in range(len(my_digits)-1, 0, -1):
#         if not (my_digits[index] < my_digits[index-1]):
#             return False
#     return True
# print(does_bob_like(234))