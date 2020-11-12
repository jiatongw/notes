""" How to use multiple stacks to implement a de-queue
De-queue
       Left xxxxxxxxxxxx Right
     left.add()         right.add()
     left.remove()      right.remove()

Method 1: use two stacks

         stack 1 || || stack 2

    <-- 8 7 6 5  || || 1 2 3 4 -->
left.add() == stack1.appnd()  O(1)
right.add() == stack2.appnd() O(1)
left.remove():
    case 1 : stack1.pop() if stack 1 is not empty
    case 2 : stack 1 == empty, then move all element from stack2 to stack 1, then call stack1.pop()
    O(n)
right.remove(): similiar to left.remove()

极端case: 如果一直循环往复调用left.remove()后在调用right.remove()， 那么每次都要先把element从一个stack移动到另一个stack
"""


"""
follow up: 优化
给一个stack 3 as buffer
    stack 1 || || stack 2
      empty || || 1 2 3 4 5 6 7 8

如果遇到一个stack 空了，需要用到stack3 为Buffer，把stack2 中 一半 的element 放到stack1, 

empty || || 1 2 3 4 5 6 7 8   -->   4 3 2 1 || || 5 6 7 8

先把 half element 放到stack3:
stack 1 || || stack 2
  empty || || 1 2 3 4 

stack3 || 8 7 6 5

然后把stack 2剩下的element放到 stack 1
stack 1 || || stack 2
4 3 2 1 || || empty
stack3 || 8 7 6 5

再把stack 3 element放回 stack 2
stack 1 || || stack 2
4 3 2 1 || || 5 6 7 8
stack3 || 

保证 左右stack 数据平均

这样的话 remove()操作平均时间复杂度 amortized time == O(1)

stack1: for left head
stack2: for right head
stack3: for buffer half element
"""
    