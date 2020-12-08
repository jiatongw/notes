'''
Print all subsets of a set S = ["a", "b", "c"]
'''

from copy import deepcopy

def subsets(s):
    if not s:
        return [[]]
    res = []
    helper(s, [], 0, res)
    return res

def helper(s, tmp, start, res):

    res.append(deepcopy(tmp))

    for i in range(start, len(s)):
        tmp.append(s[i])
        helper(s, tmp, i + 1, res)
        tmp.pop()

if __name__ == '__main__':
    s = ["a", "b", "c"]
    print(subsets(s))


'''
Time complexity: O(2**n), 一共有3层，每一层分叉，最后一共有2**n个 node

space complexity: O(n)

所有的 permutation 的题，时间复杂度 一定是 指数级，x ^ n, 或者 n 的阶层
'''
    