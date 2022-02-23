# class Solution:       
#     def twoSum(self,nums,target):
#         for i in range(len(nums)):
#             a = nums[i]
#             b = target - a
#             print(a,b)
#             if b in nums[i+1:]:
#                 print(b)
#                 bdict = dict(enumerate(nums[i+1:],i+1))
#                 new_bdict = dict([(value, key) for key, value in bdict.items()]) 
#                 print(bdict)
#                 print(new_bdict)
#                 h = new_bdict[b]
#                 return [i,h]
#                 break

# class Solution1(object):
    
#     def twoSum(self,nums, target):
#         self.nums = nums
#         self.target = target 
        
#         for i in range(len(self.nums)):
#             a = self.nums[i]
            
#             for j in range(i+1,len(self.nums)):
#                 b = self.nums[j]
#                 if a+b == self.target:
#                     return [i,j]
#                     break

# c = Solution1()

# r = c.twoSum([3,2,4],6)
# print(r)



# class Solution1:
#     def __init__(self, nums, target):
#         self.nums = nums
#         self.target = target
    
#     def twoSum(self):
#         # self.nums = nums
#         # self.target = target 
        
#         for i in range(len(self.nums)):
#             a = self.nums[i]
            
#             for j in range(i+1,len(self.nums)):
#                 b = self.nums[j]
#                 if a+b == self.target:
#                     return [i,j]
#                     break

# c = Solution1([3,2,4],6)

# r = c.twoSum()
# print(r)




# import math
# class Solution2(object):
#     def __init__(self, l1, l2):
#         self.l1 = l1
#         self.l2 = l2
    
#     def addTwoNumbers(self):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         # convert digit to numbers
#         self.l1_number = 0
#         self.l2_number = 0
#         for i in range(len(self.l1)):
#             self.l1_number = self.l1_number + self.l1[i]*(math.pow(10, i))
            
#         for i in range(len(self.l2)):
#             self.l2_number = self.l2_number + self.l2[i]*(math.pow(10, i))

#         # sum up 2 numbers
#         self.number_sum = self.l1_number+self.l2_number
#         # convert numbers to output list
#         self.number_list = []
#         # x = divmod(self.number_sum, 10)[0]
                
#         while divmod(self.number_sum, 10)[0]>0:
#             self.rem = divmod(self.number_sum, 10)[1]
#             self.number_list.append(int(self.rem))
#             self.number_sum = divmod(self.number_sum, 10)[0]
#         self.number_list.append(int(self.number_sum))

#         print(self.number_sum, self.number_list)



# class Solution2:

    
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         str_l1, str_l2 = '', ''
#         while l1:            
#             str_l1 += str(l1.val)
#             l1 = l1.next
#         while l2:            
#             str_l2 += str(l2.val)
#             l2 = l2.next
#         int_l1 = int(str_l1[::-1])
#         int_l2 = int(str_l2[::-1])       
#         return list(map(int, str(int_l1 + int_l2)[::-1]))


        # return self.l1_number, self.l2_number
# c = Solution2([2,4,3],[5,6,4])
# r = c.addTwoNumbers()



class Solution7(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        xlist = []        
        if x>=0:
            while x//10 > 0:
                xlist.append(x%10)
                x = x//10
            xlist.append(x)
            
            newn = 0
            for i in range(len(xlist)):                
                newn = newn+ xlist[-i-1]*(10**i)
        else:
            x= -1*x
            while x//10 > 0:
                xlist.append(x%10)
                x = x//10
            xlist.append(x)
            
            newn = 0
            for i in range(len(xlist)):             
                newn = newn+ xlist[-i-1]*(10**i)
            newn = -1*newn

        if newn<=-2**31 or newn>=2**31-1:
            newn = 0

        return int(newn)

c = Solution7()
print(c.reverse(-123))