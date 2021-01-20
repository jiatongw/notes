'''
common element problem

Q. Find common elements in two arrays
LC 349
'''

'''
变种: what if two arrays sorted but size of two arrays are very different? (m << n)

Sol: for each element from the array with smaller size, run binary search against the 
array of larger size.

Time = O(m * log n)
'''

'''
变种: what if unsorted?

Sol1: sort it first, then 谁小移谁
Time = O(mlogm + nlogn + m + n)

Sol2: Use a hash set. 把size小的array 放进set里，然后for each element in larger array, 判断

Time = O(m + n)
Space = O(m) (if m < n)
'''

'''
Q. Find common elements in 3 arrays

Sol1: 谁小移谁 
    how to move pointer? 
        - move the non-largest two pointers. 
'''

'''
Q. Find common elements in K arrays

'''

'''
Q2. 一个字典有一系列string, 要求找两个string, 使得他们没有共同字符，并且长度乘积最大.

s1: abcde size = 5
s2: adzz size = 4
s3: abd  size = 3
s4: fgz  size = 3

return: abcde * fgz = 5 * 3 = 15


Sol: BFS2 best first search
        - initial state 
        - expansion/generation rule
        - termination condition
'''

'''
Q2.2 how to find the k-th
'''
