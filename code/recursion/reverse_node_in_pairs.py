class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(head):
    if not head or head.next is None:
        return head
    cur = head.next.next
    tmphead = reverse(cur)
    newhead = head.next
    newhead.next = head
    head.next = tmphead
    return newhead

def reverse2(head):
    if not head or head.next is None:
        return head
    
    dummy = Node(-1)
    dummy.next = head
    prev = dummy
    cur = head
    Next = cur.next

    while cur and cur.next:
        tmp = Next.next
        Next.next = cur
        cur.next = tmp
        prev.next = Next
        if tmp:
            Next = tmp.next
            prev = cur
            cur = tmp
        else:
            return dummy.next
    return dummy.next
        
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node1.next = node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

new = reverse2 (node1)

while new is not None:
    print(new.val)
    new = new.next




    