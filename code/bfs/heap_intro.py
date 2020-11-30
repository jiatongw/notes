'''
heap (binary heap) 又被称为 优先队列 priority queue

性质：
1. 任意节点小于它的所有后裔，最小元素在堆的根上
2. 堆总是一颗完全树 complete tree
3. 根节点最大的堆叫做max heap, 根节点最小的堆叫做min heap
4. index of left child = index of parent * 2 + 1
5. index of right child = index of parent * 2 + 2
6. unsorted but follow rules above

'''

'''
支持的基本操作：
1. insert O(log(n))
2. update O(log(n))
3. get/top O(1)
4. pop O(log(n))
5. heapify: 使一个unsorted array变成一个堆 O(n)
'''