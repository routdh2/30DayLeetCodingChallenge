'''Problem Statement: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3300/'''
#This runs in O(n) time and O(1) space
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size=len(nums)
        result=[0]*size
        result[0]=1
        for i in range(1,size):
            result[i]=result[i-1]*nums[i-1]
        R=1
        for i in reversed(range(size)):
            result[i]=result[i]*R
            R=R*nums[i]
        return result
