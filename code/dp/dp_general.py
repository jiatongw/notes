'''
DP 解题常用方法
1. 一维的dp, original data, such as a rope, a word, a piece of wood, 求max or min
    1.1 if the weight of each smallest element in the original data is identical/similar
        1.1.1 identical: 1 meter of rope
        1.1.2 similar: a letter, a number
then this kind of problem is usually simple:
Linear scan and look back to the previous element

for example:
    longest ascending subarray(when at i, look back ar i-1) LC 647
    longest ascending subsequence(when at i, look back at 1...i-1)
    cut rope
    cut palindrome
'''

'''
LC 343
Maximal product when cutting ropes

_ _ | _ _ _ product = 2 * 3 = 6

_ | _ | _ | _ | _  product = 1 * 1 * 1 * 1 * 1 = 1
'''

## sol 1: recursion
## TIME = O(n!)
def cutRope(n):
    if n <= 1:
        return 0

    maxProduct = 0

    for i in range(1, n):
        curBest = max(n - i, cutRope(n - i))
        ## 这里 curBest 是指 一刀都不切，和切一刀后的最大值
        maxProduct = max(maxProduct, curBest * i)
    
    return maxProduct
