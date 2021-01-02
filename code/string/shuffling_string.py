'''
A1B2C3D4 -> ABCD1234 
'''

def shuffling(s):
    array = list(s)
    res = mergeSort(array, 0, len(array)-1)
    return ''.join(res)

def mergeSort(array, left, right):
    if not array or len(array) == 0:
        return array

    l = []

    if left == right:
        l.append(array[left])
        return l
    mid = (left + right) // 2

    left_half = mergeSort(array, left, mid)
    right_half = mergeSort(array, mid + 1, right)

    result = merge(left_half, right_half)
    return result

def merge(left, right):
    i = 0
    j = 0
    tmp = []

    while i < len(left) and j < len(right):
        if left[i].isdigit() and right[j].isdigit():
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        elif (not left[i].isdigit()) and (not right[j].isdigit()):
            if left[i] <= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        else:
            if left[i] >= right[j]:
                tmp.append(left[i])
                i += 1
            else:
                tmp.append(right[j])
                j += 1
        
    if i == len(left):
        for k in range(j, len(right)):
            tmp.append(right[k])
    if j == len(right):
        for k in range(i, len(left)):
            tmp.append(left[k])

    return tmp


print(shuffling("A1B2C3D4EFGH567IJ89"))