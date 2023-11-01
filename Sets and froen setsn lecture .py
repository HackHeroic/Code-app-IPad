# # set1 = {1,2,3,4}
# # print(type(set1),set1)
# # my_dict =dict(a=1,b=2,c=3)
# # print(my_dict)
# # my_set = {5,6,7}
# # set2 = {1,2,3,4,my_set}
# # print(set2)
# # my_set2 = {(1,2),(4,3)}
# # print(my_set2)
# # print(set((1,2,4,3)))

# #method in sets 
# s1 = {1,2,3}
# s2 = [3,4,5]
# ans = s1.union(s2)
# print(ans)

# #operator
# ans1 = s1|set(s2)
# print(ans1)

# #s2 is not a set and "|" is called pi
# ans2 = s1|set(s2)
# print(ans2)

#updating sets
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {4,5,6}
# # ans10 = set1.update(set2) #this is wrong coz returns none
# set1.update(set2,#can also give multiple sets into this.)
# print(set1)
#using intersection_update()
# set1 &= set2
# print(set1)
# ans = set1.intersection_update(set2)
# print(ans)
# set1.intersection_update(set2,set3)
# print(set1)

#using differnce_update()
set1.difference_update(set2)
print(set1)
set2 -= set3
print(set2)m

#Important sorting functions
#add() syntax = set1.add(hashable)
#remove() syntax = set1.remove() but it will give error when the lement specified is not in the set
#discard() syn - set1.discard() but it is a better cousin of remove they wil not give the error when the sopecified char is not mentioned in the set
#pop()- same syn but again it will remove some random element from set






