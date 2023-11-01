n = int(input())
def space_bef(n,i):
    space = n - i
    print(" "*space,end ="")
def Top_part_of_diamond(i):
    print("*"*((2*i)+1))
    print()
for i in range(n):
    space_bef(n,i)
    Top_part_of_diamond(i)
    
def bottom_part_of_diamond():
    print("*"*)
for i in range(n-1):
    space_aft()
    bottom_part_of_diamond()
