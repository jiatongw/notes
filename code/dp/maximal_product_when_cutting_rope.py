'''
maximal product when cutting rope

given a rope with integer-length n, how to cut the rope into m integer-length parts with length
p[0], p[1]...p[m-1], in order to get the maximal product of p[0]*p[1]*...*p[m-1].
m is determined by you and must be greater than 0
'''

def getmax(n):
    if n <= 1:
        return 0

    max_product = 0
    for i in range(1, n): ## i = meters of rope to cut off
                          ## i is the 右小段
        best = max(n - i, getmax(n-i)) ## 由大到小，拆解成subproblem
        max_product = max(max_product, i * best)
    return max_product
'''
Time = O(n!)
'''

def dp_getmax(n):
    m = [0] * (n+1)
    m[0] = 0
    m[1] = 0

    for i in range(1, n+1):
        curmax = 0
        for j in range(1, i):
            curmax = max(curmax, max(j, m[j]) * max(i-j, m[i-j]))
        m[i] = curmax

    return m[n]
'''
Time: O(n^2)
'''

print(getmax(12))
print(dp_getmax(12))


