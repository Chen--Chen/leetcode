# for loop
# while loop
# pythonic way to do fast loop creating list/array

# skip and continue and jump etc in loop


# if else
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
# else:
#   print("a is greater than b")



# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")


# a = 330
# b = 330 
# #print("A") if a > b else print("=") if a == b else print("B")


# x = 41

# if x > 10:
#     print("Above ten,")
#     if x > 20:
#         print("and also above 20!")
#     else: 
#         print("but not above 20.")



# a = 33 
# b = 200

# if b>a:
#     pass


# fruits = ["apple", "banana", "cherry", "mango"]

# for x in fruits:
#     if x =='banana':
#         continue
#     print(x)

# print(x)

# for x in "banana":
#     print(x)

# for x in range(6):
#     print(x)

# for x in range(2,6):
#     print(x)

# for x in range(2, 30, 3):
#     print(x)


# for x in range(6):
#     print(x)
# else:
#     print("Finally finished!")


# for x in range(6):
#     if x == 3: 
#         break
#     print(x)
# else:
#     print("Finally finished!")


# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#     for y in fruits:
#         print(x,y)

# for x in [0,1,2]:
#     pass

# i = 1
# while i < 6 : 
#     print(i)
#     if i ==3:
#         break
#     i +=1


# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)


# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print(i, "i is no longer less than 6")




# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# result_1 = tri_recursion(6)

# print(result_1)


x = lambda a: a+10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

x = lambda a, b, c: a+b+c 
print(x(5,6,2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)


print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


############## break, continue, pass ##############


