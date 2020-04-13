#!/usr/bin/env python3

##### 1.Two Sum #####
"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
"""

class Solution:       
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            a = nums[i]
            b = target - a
            print(a,b)
            if b in nums[i+1:]:
                print(b)
                bdict = dict(enumerate(nums[i+1:],i+1))
                new_bdict = dict([(value, key) for key, value in bdict.items()]) 
                print(bdict)
                print(new_bdict)
                h = new_bdict[b]
                return [i,h]
                break


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]




##### 1119. Remove Vowels from a String #####
class Solution:
    def removeVowels(self, S):
        vowellist = ['a','e','i','o','u']
        outputstr=""
        for l in S:
            if l not in vowellist:
                outputstr=outputstr+l
        return(outputstr)



##### 1108. Defanging an IP Address #####
class Solution:
    def defangIPaddr(self,address):
        outputstr=""
        for l in address:
            if l==".":
                outputstr=outputstr+"[.]"
            else:
                outputstr=outputstr+l
        return outputstr


##### 1342. Number of Steps to Reduce a Number to Zero ##### 
class Solution:
    def numberOfSteps(self, num):
        i=0
        while num!=0:
            if num%2==0:
                num=num/2
            else:
                num = num-1
            i = i+1
        return i


class Solution:
    def numJewelsInStones(self, J, S):
        Jlist = [j for j in J]
        Slist = [s for s in S if s in Jlist]
        return len(Slist)

class Solution:
    def subtractProductAndSum(self, n):
        productdigit=1
        sumdigit=0
        while n>0

if __name__ == '__main__':
    n = Solution()
    print(n.numJewelsInStones("aA", "aAAbbb"))
