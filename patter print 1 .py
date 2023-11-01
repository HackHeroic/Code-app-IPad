# n = int(input())
# while n > 0 :
#     for i in range(n):
#          print(i,end = '')
#     n = n -1
#     print()
n = int(input())
x = n 
while True:
    for i in range(x,n+1):
        print(i,end ='')
    print()
    x = x-1
    if x == 0:
        break
    