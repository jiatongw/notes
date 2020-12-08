'''
实现方法: easy to use recursion
常见考题:
    1. print all subsets of a set
    2. print all valid permutations of () () ()
        ()()()  ((())) (())()
    3. 凑硬币的金额 99cents
        有1分，5分，10分，25分，凑99分，有几种方法， 打印所有可能组合
    4. given an input string = "12321234", output all valid ip address
    5. permutation of a string
    ....

'''

'''
DFS 基本方法:

1. what does it store on each level? 每层代表什么意义？一般来讲解题之前就要知道DFS要recurse多少层
2. how many different states should we try to put on this level 每层有多少个状态/case需要try
'''