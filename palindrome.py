n = int(input())
def spaces(n,i):
    print(" "*(n-i),end = "")

def left_part_palindrome(i):
    for item in range(1,i+1):
        print(item,end = "")

def right_part_palindrome(i):
    for item in range(i-1,0,-1):
        print(item,end = "")


def ith_row(n,i):
    spaces(n,i)
    left_part_palindrome(i)
    right_part_palindrome(i)
    print()

for i in range(1,n+1):
    ith_row(n,i)



