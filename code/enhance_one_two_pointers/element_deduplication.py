'''
挡板题, string removal. two pointers思想

基本思想: 用两个变量, 一个变量记录当前指针位置( = fast index), 一个变量记录挡板位置(= slow index)

性质1: slow 左边是处理好的元素，当前指针fast右边是未处理的元素，挡板和当前指针之间的区域是无用元素。每次只要分析
当前元素性质是否要加入或者移动 slow 挡板就可以了

性质2: 用快慢两个指针，同向而行，处理完毕后，return的结果中，每个integer/char的相对位置不变

prerequisite: the fast pointer is always ahead of the slow pointer.
关键点: 每个挡板的物理意义在整个程序运行过程中一直要保持 consistent
'''

'''
Q1 给一个 sorted array, remove duplicated elements

1122233 -> 123
'''
def remove(l):
    if not l:
        return []

    slow = fast = 1
    while fast < len(l):
        if l[fast] != l[slow -1]:
            l[slow] = l[fast]
            slow += 1

        fast += 1
    return l[:slow]
# print(remove([0,1,2,2,2,3,3,4,5,6,7,9,9,9,9,9]))

'''
Q2 给一个 sorted array, remove duplicated elements
最多保留两个重复的
1122233 -> 112233
'''
def remove2(l):
    if not l:
        return []

    slow = fast = 2

    while fast < len(l):
        if l[fast] != l[slow -2]: ## 必须 fast 和 slow - 2 来比较, 不能 fast和 fast - 2来比较
            l[slow] = l[fast] 
            slow += 1
        fast += 1

    return l[:slow]
# print(remove2([0,0,1,1,2,2,2,3,3,3,4,4]))

'''
延伸: 如果 说 remove duplicate, 至多保留 K 个， 那么slow fast 挡板 从 index = k 开始
然后 fast 和 slow - k 比较
'''

'''
Q2 给一个 sorted array, remove duplicated elements
重复的一个都不保留
1123344 -> 2

用slow, fast1, fast2 指针

1 2 2  3 3 4 4
  s
  f1
       f2
'''

def remove3Fail(l):
    if not l:
        return []

    slow = fast1 = fast2 = 0

    while fast2 < len(l):
        if l[fast2] == l[fast1]:
            fast2 += 1
            continue   ### 如果[0,0,1,1,4,4,5]， 不重复元素在最后一位，这个写法不会查到最后一个元素，
                       ### 而是直接退出了。 以上case返回[]. 因为当fast2在最后一位时，会先+1，然后等于len(l)
                       ### 进而直接退出循环
        else:
            if fast2 - fast1 == 1:
                l[slow] = l[fast1]
                slow += 1 

            fast1 = fast2
    return l[:slow]

def remove3Correct(l):
    if not l:
        return []

    slow = fast1 = fast2 = 0

    while fast2 < len(l):
        while fast2 < len(l) and l[fast2] == l[fast1]:
            fast2 += 1

        if fast2 - fast1 == 1:
            l[slow] = l[fast1]
            slow += 1 

        fast1 = fast2

    return l[:slow]
print(remove3Correct([0,1,1,2,2,2,3,3,3,4,4,5]))

'''
给一个随机数组，random numbers, 把所有 0 都放在数组的最后

[1,2,3,0,0,4,5,2,0,0] -> [1,2,3,4,5,2,0,0,0,0]

in place. other element 的位置可以改变
'''

def pushZero(l):
    if not l:
        return []

    left = 0
    right = len(l) - 1

    while left <= right:
        if l[left] != 0:
            left += 1
        elif l[right] == 0:
            right -= 1
        else:  ### left 是 0，right 不是 0 的情况
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
    return l

print(pushZero([0,1,1,2,2,0,3,3,0,4,4,5]))
