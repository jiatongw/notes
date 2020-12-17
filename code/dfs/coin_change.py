'''
1. what does it store on each level? 4 levels, each level represents how many coins of this value
can be selected to form the final results
2. how maany different states should we try to put on each level? it depends on the input

                        99 cents
                    /        |         |         | 

level0 (25)     0*25(rem=99)  1*25     2*25     3*25 (rem=24)
                 |||||
level1 (10)     0*10 1*10...
level2 (5)
level3 (1)

时间T(O) = 99 ^ 4
空间T(O) = O(4)
'''
import copy
## coin = [25, 10, 5]
def coin_change(total, coin):
    result = []
    sol = [0 for i in range(len(coin))]
    helper(total, coin, total, 0, sol, result)

    return result

def helper(total, coin, remain, level, sol, result):
    if level == len(coin) - 1:
        if remain % coin[level] == 0:
            sol[level] = remain // coin[level]
            result.append(copy.deepcopy(sol))
        return

    for i in range(0, remain // coin[level] + 1): ## 向上取整
        sol[level] = i
        helper(total, coin, remain - i * coin[level], level+1, sol, result)

print(coin_change(10, [5,2,1]))
