"""
Find smallest k elements from an unsorted array of size n. 

"""

"""
Time complexity: O(nlog(k))

此题也可以用 quick sort 来做: pivot如果是第k个，那么只需要看Pivot之前的部分就行了
"""

from queue import PriorityQueue

def smallestK(array, k):
    if not array:
        return -1

    pq = PriorityQueue()

    for num in array:
        pq.put(-1 * num)

        if pq.qsize() > k:
            pq.get()
    res = []
    for i in range(0, k):
        res.append( -1 * pq.get())
    return res

if __name__ == '__main__':
    print(smallestK([1,9,4,10,5,6,3,-2,-1,4], 3))

