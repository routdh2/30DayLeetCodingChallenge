# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3290/'''
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        fast=slow=head
        while fast != None:
            fast=fast.next
            if fast != None:
                fast=fast.next
            elif fast==None:
                return slow
            slow=slow.next
        return slow
        
