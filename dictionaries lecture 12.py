#methods of creating a list
# A =dict(a=1,b=2,c=3)
# B = dict([("a",1),("b",2),("c",3)])
# print(A)
# print(B)

# my_dict = {"a":1,
#            "b":2,
#            "c":3
#                 }
# print(my_dict)

# get manipulation
# anuj_number = my_dict.get("a",0)
# print(anuj_number)

# #deletingg a particluar value
# del my_dict["a"]
# print(my_dict)

# #ADD new value
# my_dict["new_value"] = 4

# print(my_dict)

#clear function -  will clear it fully
# final_result = my_dict.clear()
# print(final_result)

#item(),values(),keys() - View list
my_dict = {"a":1,
           "b":2,
           "c":3,
           "d":4,
           "e":5,
           "f":6
           }
d1 = my_dict.items()
d2 = my_dict.values()
d3 = my_dict.keys()
print(d1)
print(d2)
print(d3)

# #pop
# ans1 = my_dict.pop("a")
# print(ans1)
# #pop(key,[default value])
# ans2 = my_dict.pop("b",0)
# print(ans2)

# #update()
# e = {"h":8}
# my_dict.update(e)
# print(my_dict)

# #update(list of tuples)
# to_add = [("i",9),("j",10)]
# my_dict.update(to_add)
# print(my_dict)

 #sorting
# ans4 = sorted(my_dict,key = items()
# print(ans4)

#json
# import json
# json_string = '{"a":1,"b":2}'
# ans = json.loads(json_string)
# print(ans)



# #dict to json
# anu = json.dumps(ans)
# print(anu)
# #popitem()

# diction={"diary":1,"book":3,"novel":5}
# diction.update({"diary":1,"novel":5})
# print(diction)
