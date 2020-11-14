"""
Check two given binary trees are identical or not. 
Assuming any number of tweaks are allowed. A tweak is defined as a swap of the children of one node in the tree.

检查两棵二叉树是否在经过若干次扭转后可以等价。扭转的定义是，交换任意节点的左右子树。
等价的定义是，两棵二叉树必须为相同的结构，并且对应位置上的节点的值要相等。

LintCode 450. LC 无此题
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isIdentical(self, root):
        if not root:
            return True
        if root.left is None and root.right is None:
            return True
        flag = self.helper(root.left, root.right)
        
        return flag
        
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        
        if left.val != right.val:
            return False
        
        mirror_leftcheck = self.helper(left.left, right.right)
        mirror_rightcheck = self.helper(left.right, right.left)
        identical_leftcheck = self.helper(left.left, right.left)
        identical_rightcheck = self.helper(left.right, right.right)
        
        return (mirror_leftcheck and mirror_rightcheck) or (identical_leftcheck and identical_rightcheck)