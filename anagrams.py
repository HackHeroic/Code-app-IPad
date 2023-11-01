num1 = input()
num2 = input()
def are_anagrams(num1, num2):
    if sorted(num1) == sorted(num2):
        return True
    else:
        return False
print(are_anagrams(num1, num2))

