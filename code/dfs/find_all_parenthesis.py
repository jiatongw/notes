'''
LC 22

()()(), ((())), (())()

Valid principle: whenever you see/add a right parenthesis into the sequence, 
we must guarantee that the left parenthesis added so far > right parenthesis added so far


DFS 基本方法:

1. what does it store on each level? 每层代表什么意义？一般来讲解题之前就要知道DFS要recurse多少层
    6 层
2. how many different states should we try to put on this level 每层有多少个状态/case需要try
    2 个 (either add left OR add right)
'''

def generateParenthesis(n):
        if n == 0:
            return []
        result = []
        helper(0, 0, "", result, n)
        return result
        
def helper(l, r, tmp, result, n):
    # 如果右括号用的比左括号多，那么久是invalid
    if l == n and r == n:
        result.append(tmp)
        return
    
    if l < n:
        tmp = tmp + "("
        helper(l + 1, r, tmp, result, n)
        tmp = tmp[:-1]
        
    if r < l:
        tmp = tmp + ")"
        helper(l, r + 1, tmp, result, n)
        tmp = tmp[:-1]

print(generateParenthesis(3))