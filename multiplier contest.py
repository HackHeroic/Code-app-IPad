N = int(input())

def sum_ofsingle_digit(product):
    required_sum = 0
    if product < 10 :
        required_sum += product
    else:
        while product > 9 :
            sum_of_digits = 0
            while product > 0:
                digit1 = product%10
                product = product//10
                sum_of_digits += digit1 
            product = sum_of_digits
    return product
        
ans = 0
for i in range(1,11):
    product = N*i
    ans = ans + sum_ofsingle_digit(product)
print(ans)

