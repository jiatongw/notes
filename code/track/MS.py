
'''
Figure Under Gravity
https://www.1point3acres.com/bbs/thread-744683-1-1.html
'''
import sys
def figureEnderGravity(matrix):
    if not matrix or not matrix[0]:
        return matrix
    m, n = len(matrix), len(matrix[0])
    minstep = sys.maxsize
    for j in range(n):
        i = 0
        while i < m:
            while i < m and matrix[i][j] != 'F':
                i += 1
            if i == m:
                continue
            while i < m and matrix[i][j] == 'F':
                i += 1
            if i < m:
                cnt = 0
                while i < m and matrix[i][j] != '#':
                    i += 1
                    cnt += 1
                minstep = min(minstep, cnt)
    if minstep == sys.maxsize or minstep == 0:
        return matrix

    for i in range(m-1, minstep-1, -1):
        for j in range(n):
            if matrix[i-minstep][j] == 'F':
                matrix[i][j] = 'F'
                matrix[i-minstep][j] = '.'

    return matrix


'''
Find all palidrome substring

abaaa

a, b, aa, aaa, aba
'''

def findAllPal(string):

    if not string:
        return []
    
    visited = set()

    for i in range(0, len(string)):
        helper(i, i, string, visited)
        helper(i, i + 1, string, visited)

    return list(visited)

def helper(l, r, string, visited):
    while l >= 0 and r < len(string) and string[l] == string[r]:
        if string[l:r+1] not in visited:
            visited.add(string[l:r+1])
        l -= 1
        r += 1
print(findAllPal("ab baeae"))