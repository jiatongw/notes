visited = [91, 44, 10, 836, 408, 527, 205,
            346, 560, 161, 157, 271, 12, 13, 277,
            388, 163, 56, 57,
            252, 253, 1429, 387, 438,
            288, 128, 538, 285,
            98, 173, 156, 366, 314,
            102, 785, 261, 5, 210, 207,
            133, 1197, 74, 48, 311, 415, 43, 67, 2, 50,
            17, 254, 282, 77, 39, 40, 46, 47, 394,
            2, 206, 21, 234, 92, 25, 23, 445, 203]

set(visited)

'''
In lintcode but not leetcode:
127. Topological Sorting
zombie in matrix
'''

'''
next: topology sort, course schedule, knight, zombie, 
'''
DFS = [17, 254, 282, 77, 39, 40, 46, 47]
LinkedList = []
Tree = []
prefixSum = []
UnionFind = []


lc = input("please enter LC number: ")

if int(lc) in visited:
    print("True")
else:
    print("False")

VIP = [5, 157, 91, 44, 10, 527, 56, 57, 252, 253, 438, 128,
        285, 173, 156, 366, 314, 102, 785, 261, 
        210, 207, 133, 415, 43, 2, 50, 394,
        2, 206, 234, 92, 25, 23, 445]