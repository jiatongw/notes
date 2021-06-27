### 第二题

def find(array):
    '''
    Method: instead of doing multiple operation, we only count the number
    of negative item. If the number if even, then sign is 1, else -1.
    '''
    count = 0
    for num in array:

        if num < 0:
            count += 1
        elif num == 0:
            return 0
    ## means positove 
    if count % 2 == 0:
        return 1
    else:
        return -1

## count good node

class Solution:
    """
    This is a bottom-up solution.  
    1. Record the maximum value found while recurse down to the paths from root to leaves;
    2. If node value >= current maximum, count it in.
    3. return the total number after the completion of all recursions.
    """
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        return self.helper(root, float('-inf'))
        
    
    def helper(self, root, curmax):
        if not root:
            return 0
        
        ## record max value while recurse down
        curmax = max(curmax, root.val)
        
        left = self.helper(root.left, curmax)
        right = self.helper(root.right, curmax)
        
        cur = 0
        ## at current level, if current node val >= current max value, we count it in
        if root.val >= curmax:
            cur = 1
        
        ## return the number of from its left, right and itself
        return left + right + cur
'''
T(n) = 2T(n / 2) + O(n)
= 2(2T(n / 4) + O(n / 2)) + O(n)
= 4T(n / 4) + O(n) + O(n)
= 8T(n / 8) + 3O(n)
= nT(n / n) + lognO(n)
= n + O(nlongn)
= O(nlogn)
'''