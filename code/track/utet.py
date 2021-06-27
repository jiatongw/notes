
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
'''
test cases:
1. l1 = None, l2 = Non2
2. l1 = None, l2 = [1,2,3]
3. l1 = [1,2,3], l2 = None
4. l1 = [1,2,3], l2 = [6,7,8]
5. l1 = [1,2,3,4,5], l2 = [10]

'''

    
def mergeTwoSortedList(l1, l2):
    '''
    input type: two linked list
    return type: one linked list
    '''
    
    if not l1:
        return l2
    if not l2:
        return l1
    
    
    dummy = ListNode(-1)
    head = dummy 
    
#     ## merge
#   dummy ->  
# # head -> 1 -> 2
# #              h
    

# #     l2        4 -> 5
# #               j
    
    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
            head = head.next
        else:
            head.next = l2
            l2 = l2.next
            head = head.next
            
    if l1:
        head.next = l1
    else:
        head.next = l2
    
    return dummy.next

# expectNodeList = [1,2,3,4]
def assertEqual(expectNodeList, testNodeList):
    
    return expectNodeList == testNodeList
    
#     if len(expectNodeList) != len(testNodeList):
#         return False
    
#     i = 0
#     while i < len(expectNodeList):
#         if expectNodeList[i] != testNodeList[i]:
#             return False
#         i += 1
#     return True
    

def test_case1(expectNodeList, l1List, l2List):
    
    testNodeList = constructList(l1List, l2List)
    if not assertEqual(expectNodeList, testNodeList):
        return False
    
    return True
 
def test_case2(expectNodeList, l1, l2):
    pass

## [1,2,3], [4]

'''
constructList([1,2,3], [4])
constructList([], [4, 5, 6])
constructList([3,5], [4, 5, 6])
'''
def constructList(l1List, l2List):
    '''
    type: l1: List
          l2: List
    rtype: listNode
    '''
    if not l1List:
        l1 = None
    if not l2List:
        l2 = None
    

    cur1 = ListNode(l1List[0])
    head1 = cur1
    for l in l1List[1:]:
        cur1.next = ListNode(l)
        cur1 = cur1.next
    
    l1 = head1
    
    cur2 = ListNode(l2List[0])
    head2 = cur2
    for l in l2List[1:]:
        cur2.next = ListNode(l)
        cur2 = cur2.next
    
    l2 = head2
    
    testNode = mergeTwoSortedList(l1, l2)
    testNodeList = []
    
    while testNode != None:
        testNodeList.append(testNode.val)
        testNode = testNode.next
    
    print(testNodeList)
    return testNodeList


def run_test_cases():
    # run case 1
    case1_l1_List = [1,2,3]
    case1_l2_List = [4,5,6]
    case1_expectNodeList = [1,2,3,4,5,6]
    if test_case1(case1_expectNodeList, case1_l1_List, case1_l2_List):
        print("Test case 1 passed!")

    else:
        raise Exception("Test Case 1 not pass!")
    
    ## more test cases below..
    


if __name__ == '__main__':
    
    # [6,7,8]
    run_test_cases()
