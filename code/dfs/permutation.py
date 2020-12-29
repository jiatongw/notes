'''
Given a string with no duplicated letters, print all permutations of the string

a b c
a c b
b a c
b c a
c a b
c b a

'''

'''
1. what does it store on each level? 3 levels, each levep represents one position
2. how many states should we try to put in each level? It is equal to the number of letters remaining

                    a b c
                /       |          | 
level0        a(bc)    b(ac)     c(ab)
               / |      / |       /    |
level 1    b(c)  c(b)  a(c) c(a)  a(b) b(a)
            |       |   |    |     |     |
level2      c      b   c     a     b     b

T(O) = O(n!) 最后一层一共有n的阶乘个node
T(O) = O(n)
'''

import copy
def permutation(string):
    result = []
    helper(string, [], result)
    return result

def helper(string, tmp, result):
    if len(tmp) == len(string):
        result.append(copy.deepcopy(tmp))
        return

    for i in range(0, len(string)):
        if string[i] in tmp:
            continue

        tmp.append(string[i])
        helper(string, tmp, result)
        tmp.pop()

print(permutation("1234"))