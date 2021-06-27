## input: [5, 10, 15] [[1,4], [3,3]]
## output: [5, 10]
import sys
def choosePipe(inventory, orders):
    ## [4, 6]
    ans = [0] * len(orders)
    totalNeed = [0] * len(orders)
    for i in range(0, len(orders)):
        totalNeed[i] = orders[i][0] * orders[i][1]

    for i in range(0, len(totalNeed)):
        minWaste = sys.maxsize
        for j in range(0, len(inventory)):
            
            curLength = inventory[j]
            while curLength < totalNeed[i]:
                curLength += curLength
            curWaste = curLength % totalNeed[i]
            if curWaste < minWaste:
                minWaste = curWaste
                candidate = inventory[j]
        ans[i] = candidate
    return ans
## for input [5, 10, 15],  [[1,4], [3,3]]
## it will return [5,5]. for [1,4], it watest 1 foot
## for [3,3], we use two 5 foot and waste 1 foot


