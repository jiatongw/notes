## LC 876

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
这种方法，如果是偶数个node，

1 -> 2 -> 3 -> 4 -> 5 -> 6

return 的是 node 4. 

这样的话，如果要把Linkedlist分成两部分，还需要一个prev指针，指向slow的前一个node

这样，第一个list, prev = None
第二个list， slow就是new head。这样就把linkedlist分半了
"""
def find_middle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow