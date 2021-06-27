'''
第一类问题:
    use recursion to return values in a bottom-up way in binary tree
'''

'''
第二类问题: path problem in binary tree
    Tree 相关问题，path类可以分为两大类
    case1: 人字形path, 这类题一般需要从下往上传integer value
    case2: 从root 往下看 (直上直下) path
        key point: carry a 直上直下 path prefix (非人字形)while traversing the tree:
            a. a complete path from leaf to root
            b. sub-section of complete path from leaf to root

            10
        -2     7
      8   -4 = cur
    prefix of path = [10, -2, -4]  
'''

'''
第三类问题: tree serialization problem
'''
'''
Q Given a Binary Tree, convert it to a Doubly linked list in in-order sequence
'''
def convert():
    pass

'''
第四类问题: convert a tree by xxx and in-order
''' 

'''
construct a Tree using inorder and level order

          20
      8       22
    4   12
       10 14

inorder [4,8,10,12,14,20,22]
level order [20, 8, 22, 4, 12, 10, 14]
'''
### level order 的第一个是每一层的 root, 然后 在Inorder中找出root index
### 方法1: 遍历level order，element 在Inorder中小于root index 的，是左子树，放进left_list，大于root index 的放进right_list
### 方法2: 每次maintain一个hashset, 在inorder中，index左边的放进set, 然后每次遍历level order，在set中的，放进left_list，不在的放进right_list


'''
N node LCA 问题
fond LCA in a n ary tree, k nodes
'''

def LCA(root, input):
    if not root:
        return None
    
    if root in input:
        return root

    count = 0
    tmp = None
    for child in root.children:
        lca = LCA(child, input)
        if lca is not None:
            count += 1
            tmp = lca
        if count >= 2:
            return root
        
    return tmp
