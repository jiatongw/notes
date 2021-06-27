# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


'''
LC 124 的变种，记录最大值的同时，记录下path
'''
class Solution:
    ans = float('-Inf')
    candidate = ""
    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        
        _ , curpath = self.helper(root, "")
        print(self.candidate)
        return self.ans
        
    
    def helper(self, root, curpath):
        if not root:
            return 0, ""
        
        left, curpathleft= self.helper(root.left, curpath)
        right, curpathright = self.helper(root.right, curpath)
        
        if left < 0:
            left = 0
            curpathleft = ""
        if right < 0:
            right = 0
            curpathright = ""
            
        curSum = left + right + root.val
        if self.ans < curSum:
            self.ans = curSum
            self.candidate = curpathleft + " "+str(root.val) + " "+curpathright

        
        ### 这里，不能return left + right + root.val,
        ### 要 return max(left, right) + root.Value
        ### 要return 单支的情况！！
        if left > right:
            curpath = curpathleft + " "+ str(root.val)
            maxvalue = left + root.val
        else:
            curpath = curpathright + " "+ str(root.val)
            maxvalue = right + root.val
        return maxvalue, curpath