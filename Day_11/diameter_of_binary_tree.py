# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''Problem Statement: https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3293/'''

class Solution:
    diameter=0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.find_height(root)
        return self.diameter
    
    def find_height(self,root):
        if root==None:
            return 0
        if root.left==None and root.right==None:
            return 1
        l_height=self.find_height(root.left)
        r_height=self.find_height(root.right)
        total=l_height+r_height
        if total>self.diameter:
            self.diameter=total
        return 1+max(l_height,r_height)
        
        
