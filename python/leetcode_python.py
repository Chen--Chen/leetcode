#!/usr/bin/env python3

#####################
##### 1.Two Sum #####
#####################
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




class Solution1:       
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


class Solution2:
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


if __name__ == '__main__':
    n = Solution1()
    #n = Solution2()
    print(n.twoSum([3,2,4], 6))
    print(n.twoSum([2,7,11,15], 9))
    print(n.twoSum([-1,-2,-3,-4,-5],-8))
