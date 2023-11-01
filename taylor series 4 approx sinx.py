def factorial(n):
    answer =1
    while n > 1 :
        answer = answer *n

        n = n - 1
        return answer

def get_ith_coefficient_sin(i):
    n = i - 1
    mod = n%4
    ls1 = [0,1,0,-1]
    derrivative = ls1[mod]
    numerator = derrivative
    denominator = factorial(n)
    coef = numerator/denominator
    return coef

def get_approx_sin(x, max_degree):
    sum_of_series = 0
    for i in range(1,max_degree+1):
        sum_of_series = sum_of_series + get_ith_coefficient_sin(i)*(x**(i-1))
    return sum_of_series

#ask sir how to execute /call from here because in question so many inputs are giveni

