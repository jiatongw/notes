'''

Find the common numbers between two sorted arrays 
'''

'''
sol 1: set()

sol 2:
可以用two pointers, 谁小移谁

a: 1, 3, 4
   i
b: 2, 3, 5
   j


sol 3: binary search
    for each element in b[m]:
        do binary search in a[n]
Time: O(mlogn)
Space: O(1)
'''
def common_number(nums1, nums2):
    pass