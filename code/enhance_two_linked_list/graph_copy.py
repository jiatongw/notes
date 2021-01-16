'''
copy linkedlist with random pointer

LC 138

唯一难点: 建立original node 和 copy node 的一一对应关系
防止一个 original node 被重复 copy 一次以上
'''

def copy_onepass():
    pass

'''
merge k sorted array into one big sorted array
'''


'''
General solutions for solving k-something problems:
1. iterative way:
    A1, A2 -> A12                       2N
              A3   ->  A13              3N
                       A4  -> A14       4N
                       ......           kN
    T(O) = (2+3+4+...+k) * n = O(k^2 * n)
2. binary reduction
3. K all together
k pointers, move the smallest one, use a priority queue. 
'''