class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.total_left = 0

'''
        root (6)
       /   |
      3     5
     / |    /
    1  2   4
'''

def store(root):
    if not root:
        return 0
    total = helper(root)
    print(total)

    
def helper(root):
    if not root:
        return 0
    left = helper(root.left)
    right = helper(root.right)
    root.total_left = left

    return left + right +1


def print_eachnode_left(root):
    if not root:
        return
    help(root)

def help(root):
    if root:
        print("root is: ", root.val)
        print("root left node is: ", root.total_left)
        help(root.left)
        help(root.right)


root = Node(6)
left1 = Node(3)
right1 = Node(5)
left2  = Node(1)
right2 = Node(2)
left3 = Node(4)
root.left = left1
root.right = right1
left1.left = left2
left1.right = right2
right1.left = left3

store(root)
print_eachnode_left(root)