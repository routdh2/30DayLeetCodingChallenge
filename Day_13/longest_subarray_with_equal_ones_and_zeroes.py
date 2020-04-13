'''Problem Statement: https://leetcode.com/problems/contiguous-array'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        table={0:-1}
        zeroes,ones,max_len=0,0,0
        for index,value in enumerate(nums):
            if value==0:
                zeroes+=1
            else:
                ones+=1
            key=zeroes-ones
            if key in table:
                max_len=max(max_len,index-table[key])
            else:
                table[key]=index
        return max_len
