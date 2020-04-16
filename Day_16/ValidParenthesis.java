/**
*   Problem Statement: https://leetcode.com/problems/valid-parenthesis-string
*/
class Solution {
    public boolean checkValidString(String s) {
        char[] arr = s.toCharArray();
        Stack<Character> stack = new Stack<>();
        for(int i=0;i<arr.length;i++) {
            if(arr[i]=='(' || arr[i]=='*')
                stack.push(arr[i]);
            else if(!stack.isEmpty()) {
                stack.pop();
            }
            else
                return false;
        }
        stack.clear();
        for(int i=arr.length-1;i>=0;i--) {
            if(arr[i]==')' || arr[i]=='*')
                stack.push(arr[i]);
            else if(!stack.isEmpty())
                stack.pop();
            else
                return false;
        }
        return true;
        
    }
}
