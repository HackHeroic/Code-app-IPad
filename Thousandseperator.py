S = input()
s_reverse = S[-1::-1]
print(s_reverse)
for i in range(0,len(S)-2,3):
    s_reverse = s_reverse[i] + s_reverse[i+1] + s_reverse[i+2] + "."
    print(s_reverse)
s_req = s_reverse[-1::-1]