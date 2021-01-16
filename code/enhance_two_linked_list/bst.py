'''
BST: find, insert, remove a node
'''

'''
Find a node whose value is closest to the target value (the target may not exsit)

如果当前 node 比 target 大，往左走，当前 node 比 target 小，往右走，
'''


'''
Find the largest element in the tree that is smaller than a target number x

        10
    5       15 = cur    target = 13
  2  7     12  20

case 1: if cur.value >= target:
        DO NOT update, 
        go left
case 2: if cur.value < target:
        update global result node, update min_diff
        go right
'''

'''
How to remove a target node from BST

传进一个node, 传出一个node
'''


'''
How to insert a target node from BST

LC 701
'''