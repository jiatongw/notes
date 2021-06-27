class Sol:
    def get_options(self, priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars) -> int:
        self.num_ways = 0

        options = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]

        self.backtrack(options, dollars, 0)

        return self.num_ways

    def backtrack(self, options, dollars, i):
        if dollars < 0:
            return

        if i >= len(options):
            self.num_ways += 1
            return

        for product in options[i]:
            self.backtrack(options, dollars - product, i + 1)

if __name__ == '__main__':
    solution = Sol()
    assert solution.get_options([2, 3], [4], [2, 3], [1, 2], 10) == 4
    assert solution.get_options([2, 3], [4], [2, 3], [1, 2], 9) == 1
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 12) == 4
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 13) == 8
    assert solution.get_options([6], [1, 1, 1, 1], [4, 5, 6], [1], 14) == 12
    assert solution.get_options([100], [1, 1, 1, 1], [4, 5, 6], [1], 99) == 0
    assert solution.get_options([1], [1], [1], [1], 4) == 1
    assert solution.get_options([1], [1], [1], [1], 3) == 0

from typing import List
class Solution:
    def maximumUnits(self, containers: List[int], peContainer: List[int], truckSize: int) -> int:
        if not truckSize:
            return 0
        
            
        import queue
        pq = queue.PriorityQueue()
        
        total = 0
        
        for u, v in zip(containers, peContainer):
            pq.put((-1 * v, u))
        
        while pq.qsize() > 0:
            m, n = pq.get()
            numUnits,  numBox= -1 * m, min(n, truckSize)
            
            total += numUnits * numBox
            truckSize -= numBox
            if truckSize == 0:
                break

        return total
# s = Solution()
# print(s.maximumUnits([5,2,4,3], [10,5,7, 9], 10))

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        move = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        ##      向北走    向左走    向南走    向右走
        
        ## 一开始朝向北。direction是 move的 index, 
        ## direction = 1 是向左走
        direction = 0
        x = y = 0
        
        for ins in instructions:
            if ins == "G":
                x += move[direction][0]
                y += move[direction][1]
                
            elif ins == "L":
                direction = (direction + 1) % 4
            
            elif ins == "R":
                direction = (direction + 3) % 4
                
        return (x == 0 and y == 0) or direction != 0

def options(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops, dollars):
    combine1 = [] 
    combine2 = []

    for m in priceOfJeans:
        for n in priceOfShoes:
            combination = m + n

            if combination < dollars:
                combine1.append(combination)

    for k in priceOfSkirts:
        for t in priceOfTops:
            combination = k + t

            if combination < dollars:
                combine2.append(combination)

    combine1.sort()
    combine2.sort()

    res = 0
    for pair in combine1:
        target = dollars - pair
        lastRight = findLastRight(combine2, target)

        if lastRight != -1:
            res += lastRight + 1

    return res

def findLastRight(l, target):
    start = 0
    end = len(l) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if l[mid] == target:
            start = mid
        elif l[mid] < target:
            start = mid
        else:
            end = mid
    if l[end] == target:
        return end
    elif l[start] == target :
        return start
    else:
        return -1

# print(options([1], [1], [1], [1], 4))


def fiveStarReviews(productRatings: List[List[int]], ratingsThreshold: int) -> int:
    import queue
    pq = queue.PriorityQueue()

    cursum = 0

    for i, product in enumerate(productRatings):
        gain = (product[0] + 1) / (product[1] + 1) - product[0]  / product[1] 
        pq.put((-1 * gain, i))

        cursum += product[0]  / product[1]
    cursum = cursum / len(productRatings) * 100

    res = 0
    
    while cursum < ratingsThreshold:
        gain, i = pq.get()
        gain = gain * -1

        cursum = cursum / 100 * len(productRatings) - productRatings[i][0] / productRatings[i][1]

        productRatings[i][0] += 1
        productRatings[i][1] += 1

        cursum = (cursum + productRatings[i][0] / productRatings[i][1]) / len(productRatings) * 100

        # curTotal = currentTotal(productRatings)

        if cursum > ratingsThreshold:
            res += 1
            break

        nextgain = (productRatings[i][0] + 1) / (productRatings[i][1] + 1) - productRatings[i][0]  / productRatings[i][1]
        pq.put((-1 * nextgain, i))
        # cursum = curTotal

        res += 1
    return res

def currentTotal(productRatings):
    total = 0
    for r in productRatings:
        total += r[0] / r[1] * 100
    total = total / len(productRatings)
    return total

# print(fiveStarReviews([[4,4], [1,2], [3, 6]], 77))

import math
def cloudFrontCache(n, edges):
    res = 0
    connectedNodes = getNodes(edges)
    for i in range(1, n+1):
        if i not in connectedNodes:
            res += 1
    
    q = []
    s = set()

    for node in connectedNodes:
        if node not in s:
            q.append(node)
            s.add(node)
            tmp = bfs(connectedNodes, q, s)
            res += tmp

    return res

def bfs(connectedNodes, q, s):
    curSum = 0
    while len(q) != 0:
        item = q.pop(0)
        curSum += 1
        for neighbor in connectedNodes[item]:
            if neighbor not in s:
                q.append(neighbor)
                s.add(neighbor)
    curSum = math.sqrt(curSum)
    curSum = math.ceil(curSum)
    return curSum


def getNodes(edges):
    m = {}
    for u, v in edges:
        if u not in m:
            m[u] = [v]
        else:
            m[u].append(v)
        if v not in m:
            m[v] = [u]
        else:
            m[v].append(u)
    return m

# print(cloudFrontCache(10, [[1, 2], [1, 3], [2, 4], [3, 5], [7, 8]]))
class Merge:
    count = 0
    def printCount(self, array):
        res = self.mergeSort(array, 0, len(array) - 1)
        return self.count

    def mergeSort(self, array, left, right):
        if not array or len(array) == 0:
            return array

        l = []
        if left == right:
            l.append(array[left])
            return l
        mid = (left + right) // 2

        half_left = self.mergeSort(array, left, mid)
        half_right = self.mergeSort(array, mid+1, right)

        result = self.merge(half_left, half_right)
        return result


    def merge(self, left_array, right_array):
        tmp = []  # 将merge好的数组放进tmp中保存
        rightIndex = 0
        for leftIndex in range(0, len(left_array)):
            while rightIndex < len(right_array) and left_array[leftIndex] > right_array[rightIndex]:
                rightIndex += 1
            self.count += rightIndex

        i = 0
        j = 0

        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                tmp.append(left_array[i])
                i += 1
            else:
                tmp.append(right_array[j])
                j += 1            

        if i == len(left_array):
            for k in range(j, len(right_array)):
                tmp.append(right_array[k])
        if j == len(right_array):
            for k in range(i, len(left_array)):
                tmp.append(left_array[k])

        return tmp

# ll = []
# for i in range(50000, -1, -1):
#     ll.append(i)

# for i in range(1, 50000):
#     ll.append(i)

import time
# m=Merge()
# start1 = time.time()
# print(m.printCount(ll))
# end1 = time.time()
# print("time1: ", end1-start1)

import bisect
class Solutions:
    def countSmaller(self, nums: List[int]) -> int:
        
        sl, counts = [], [0] * len(nums)
        
        for i in reversed(range(len(nums))):
            counts[i] = bisect.bisect_left(sl, nums[i])
            bisect.insort(sl, nums[i])
            
        return sum(counts)
# m=Solutions()
# start2 = time.time()
# print(m.countSmaller(ll))
# end2 = time.time()
# print("time2: ", end2-start2)

def storageOpt(n, m, h, v):
    h.sort()
    v.sort()
    
    maxLenH = 0
    countH = 0
    prev = 0
    for i in range(0, len(h)):
        if h[i] - prev == 1:
            countH += 1
        else:
            countH = 1
        prev = h[i]
        maxLenH = max(maxLenH, countH)

    maxLenV = 0
    countV = 0  
    prev = 0
    for i in range(0, len(v)):
        if v[i] - prev == 1:
            countV += 1
        else:
            countV = 1
        prev = v[i]
        maxLenV = max(maxLenV, countV)
    
    return (maxLenV + 1) * (maxLenH + 1)

# print(storageOpt(3, 2, [1,2,3], [1,2]))
import collections
def optimizeBox(nums):
    maps = {}
    for num in nums:
        if num in maps:
            maps[num] += 1
        else:
            maps[num] = 1
    
    tmp = []
    for weight, freq in maps.items():
        tmp.append((weight, freq))

    tmp.sort(key=lambda x:(-x[0],-x[0]*x[1]))
    
    A=[]

    total_sum=sum(nums)
    curSum=0
    for weight, freq in tmp:
        if curSum+(weight * freq)<total_sum-curSum:
            curSum+=weight * freq
            A += ([weight] * freq)
    if curSum>=total_sum-curSum:
        return sorted(A)
    else:
        return sorted([x for x in nums if x not in A])
print(optimizeBox([2,3,6,7,5]))

    # /**
    #  * Solves 0/1 knapsack in bottom up dynamic programming
    #  */
    # public int bottomUpDP(int val[], int wt[], int W){
    #     int K[][] = new int[val.length+1][W+1];
    #     for(int i=0; i <= val.length; i++){
    #         for(int j=0; j <= W; j++){
    #             if(i == 0 || j == 0){
    #                 K[i][j] = 0;
    #                 continue;
    #             }
    #             if(j - wt[i-1] >= 0){
    #                 K[i][j] = Math.max(K[i-1][j], K[i-1][j-wt[i-1]] + val[i-1]);
    #             }else{
    #                 K[i][j] = K[i-1][j];
    #             }
    #         }
    #     }
    #     return K[val.length][W];