X = int(input())
D = int(input())
staff = input()


if staff == "false" and D <= 7 :
    total_fine = X
    print(total_fine)
elif staff == "false" and D>7:
    total_fine = (D//7)*X + (D%7)*2
    print(total_fine)
elif staff == "True":
    total_fine = (D//7)*X
    print(total_fine)