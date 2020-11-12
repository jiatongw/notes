
### stack 1 is used to store input elements
### stack 2 is used to store the min value on th top of the stack 2, which is reflecting
### the min element in stack 1
### stack 1 和 stack 2 同步加减


class MinStack:
    
    def __init__(self):

        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)
        if len(self.s2) == 0 or self.s2[-1] >= x:
            self.s2.append(x)

    def pop(self):
        num = self.s1.pop()
        if num == self.s2[-1]:
            self.s2.pop()

    def top(self):
        return self.s1[-1]

    def getMin(self):
        return self.s2[-1]

"""
follow up: how to optimize the space usage of stack 2 if there are a lot of duplicate?

e.g. 1111 2222222 111 -1 -1 -1 444

用 map 来 存进stack 2

stack 1 || 11111 2222 333 -1
stack 2 || {1: 1 = the size of stack 1, when the value is inserted into stack 2}, {-1: 13} 

"""