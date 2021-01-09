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
