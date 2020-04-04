#Problem Statement:https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3286/
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==0:
            return
        start=0
        for index,value in enumerate(nums):
            if value!=0:
                nums[start]=value
                start+=1
        while start<len(nums):
            nums[start]=0
            start+=1
