'''
Sliding window of size k, always return the max element in the window size.

index 0 1 2 3 4 5 6 7 8
      1 3 2 5 8 9 4 7 3

Sol1: 用 max heap size = k

    initial: insert all the first k elements into the max heap.
    Then: when the sliding window moves to the right side by 1 step..
        - 1 new element comes in max heap
        - 1 left-most element should be removed from the sliding window 
            (but we can temporarily keep it in the heap, until it becomes the
            top element in the heap)
        when we want to cal maxheap.top(), the only thing we should be careful about 
        is to check whether this top element's index is < left border of the sliding window.
        while (so), keep popping it out (lazy deletion)

        也可以用一个map 存每个元素的index, 用来比较

Sol2: use a deque. 
'''

'''
Design LRU cache
'''

'''
First unique number

LC 1429
'''