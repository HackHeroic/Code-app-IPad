n = int(input())
def toppart_ith_row(n,i):
    print("*"*i," "*2*(n-i),"*"*i,sep = '')
def bottom_ith_row(n,i):
    print("*"*i," "*(n-i)*2,"*"*i,sep = '')

for i in range(1,n+1):
    toppart_ith_row(n,i)
for i in range(n,0,-1):
    bottom_ith_row(n,i)

