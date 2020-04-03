#Problem statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/
'''Submission Detail: 202 / 202 test cases passed.
Runtime: 60 ms
Memory Usage: 14.3 MB'''


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max=nums[0]
        max_so_far=nums[0]
        for i in range(1,len(nums)):
            max_so_far=max(max_so_far+nums[i],nums[i])
            if max_so_far>total_max:
                total_max=max_so_far
        return total_max
