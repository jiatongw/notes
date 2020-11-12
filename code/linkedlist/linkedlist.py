### LC 206
### recursive 方法 reverse linkedlist

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

## method 1, 无helper function
def reverse(head):
    if head is None or head.next is None:
        return head
    cur = head
    tmp = head.next
    newHead = reverse(tmp)

    tmp.next = cur
    cur.next = None

    return newHead

## method 2， 有helper function
class Solution:

    ## 全局的newNode，用于最后return
    newNode = None

    def reverseList(self, head):
        if not head:
            return None
        
        prev = None
        cur = head
        self.helper(prev, cur)
        return self.newNode
        
    def helper(self, prev, cur):
        if cur.next is None:
            self.newNode = cur
            return
        if cur.next is not None:
            prev = cur
            cur = cur.next
            self.helper(prev, cur)
            
        cur.next = prev
        prev.next = None
        