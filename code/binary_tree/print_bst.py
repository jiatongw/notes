
"""
Print BST keys in given range k1 - k2

"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def print_bst(self, root, k1, k2):
        if not root:
            return None
        self.helper(root, k1, k2)

    def helper(self, root, k1, k2):
        if root:
            ### 剪枝。 当val 小于 k1的时候，是不需要走左子树的
            if root.val > k1:
                self.helper(root.left, k1, k2)

            if root.val >= k1 and root.val <= k2:
                print(root.val)

            ### 剪枝。 当val 大于 k2的时候，是不需要走右子树的
            if root.val < k2:
                self.helper(root.right, k1, k2)
                
"""
Time complexity: O(n + |k2 - k1|) === max(O(n), O(|k2 - k1|))
"""


