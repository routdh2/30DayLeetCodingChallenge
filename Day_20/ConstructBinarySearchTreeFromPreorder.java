/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
//Problem Statement: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/530/week-3/3305/
class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        if(preorder==null || preorder.length==0)
            return null;
        TreeNode root = new TreeNode(preorder[0]);
        int index=findIndex(preorder, 1,preorder.length-1,root.val);
        root.left=makeTree(preorder,1,index);
        root.right=makeTree(preorder,index+1,preorder.length-1);
        return root;
        
    }
    public int findIndex(int[] arr,int start,int end, int target) {
        while(start<=end) {
            int mid=start+(end-start)/2;
            if(target>arr[mid])
                start=mid+1;
            else
                end=mid-1;
        }
        return end;
    }
    public TreeNode makeTree(int[] arr,int start, int end) {
        if(start<=end) {
            TreeNode root = new TreeNode(arr[start]);
            int index=findIndex(arr,start+1,end,root.val);
            root.left=makeTree(arr,start+1,index);
            root.right=makeTree(arr,index+1,end);
            return root;
        }
        return null;
    }
}
