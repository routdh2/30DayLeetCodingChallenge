'''Problem Statement: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        left=[0]*size
        right=[0]*size
        result=[0]*size
        left[0]=1
        right[size-1]=1
        for i in range(1,size):
            left[i]=left[i-1]*nums[i-1]
        for i in reversed(range(size-1)):
            right[i]=right[i+1]*nums[i+1]
        for i in range(size):
            result[i]=left[i]*right[i]
        return result
