# #First example of recursion
# def print_i(n):
#     if n == 1:
#         print(1)
#         return 
#     print(n)
#     print_i(n-1)

# print(print_i(5))


#second example 
def sum_till_n(n):
    if n == 0:
        return 0
    return n + sum_till_n(n-1)

print(sum_till_n(5))


