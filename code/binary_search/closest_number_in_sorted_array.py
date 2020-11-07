'''
Given a target number and an integer array A sorted in ascending order, 
find the index in A such that A[i] is closest to the given target.

Return -1 if there is no element in the array.

Notice
There can be duplicate elements in the array, and we can return any of the indices with same value.

Example

Given[1, 2, 3]and target =2, return1.

Given[1, 4, 6]and target =3, return1.

Given[1, 4, 6]and target =5, return1or2.

Given[1, 3, 3, 4]and target =2, return0or1or2.
'''

### LC 无此题
### 找和target 最接近的数，返回index

def search(array, target):
    if not array:
        return -1

    start = 0 
    end = len(array) - 1

    while start + 1 < end:       ## start + 1 < end, 为了最后锁定只剩下2个元素
        mid = (start + end) // 2
        if array[mid] <= target: ## 此处小于等于，因为数组有重复情况
            start = mid
        else:
            end = mid

    if abs(array[start] - target) < abs(array[end] - target):
        return start
    else:
        return end

if __name__ == '__main__':
    array = [1,3,4,5,6,9,10]
    target = 0

    print(search(array, target))
