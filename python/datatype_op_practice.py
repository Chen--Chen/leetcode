# x = 'Cake'
# y = "Cookie"

# z2 = y[0:]+y[1]

# # print(str.upper('cookie'))

# str1 = "Cake 4 U"
# str2 = "404"

# # print(len(str1), len(str2), str1.replace('4 U', str2))

# list1 = ["fdsf", 2,"fds","fdsf"]
# tuple1 = ("fdsf", 2,"fds","fdsf")
# list2 = ["list2", 'list22']
# list1[0] = "change"
# del list1[0]

# list3 = list1+list2
# # print(list3)

# list3.insert(0, 'insert to 0')
# list3.append('mom')
# # print(list(tuple(list3)))


# myset = set([1,2,3,2])
# myset = {1.0, "Hello", (1, 2, 3)}
# # print(myset)


# myDict = {}
# myDict["k"] = 1
# myDict["k"] = 222
# print(myDict, myDict.keys())



fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)


#newlist = [x for x in fruits if "b" in x]

#newlist = [x for x in range(10)]

#newlist = [len(x) for x in fruits]

#newlist = ['hello' for x in fruits]

newlist = [x if x!='banana' else 'orange' for x in fruits  ]

print(newlist)

