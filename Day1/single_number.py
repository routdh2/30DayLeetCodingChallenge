#Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3283/
'''Submission Detail:16 / 16 test cases passed.
Runtime: 88 ms
Memory Usage: 16.4 MB'''


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num=0
        for item in nums:
            num=num^item
        return num
