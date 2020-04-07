'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3289/'''
class Solution:
    def countElements(self, arr: List[int]) -> int:
        count=0
        for i in arr:
            if i+1 in arr:
                count+=1
        return count
