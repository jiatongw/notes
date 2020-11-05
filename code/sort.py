###### Merge Sort ######

def mergeSort(array, left, right):
    if not array or len(array) == 0:
        return array

    l = []
    if left == right:
        l.append(array[left])
        return l
    mid = (left + right) // 2

    half_left = mergeSort(array, left, mid)
    half_right = mergeSort(array, mid+1, right)

    result = merge(half_left, half_right)
    return result


def merge(left_array, right_array):
    tmp = []  # 将merge好的数组放进tmp中保存
    i = 0
    j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] <= right_array[j]:
            tmp.append(left_array[i])
            i += 1
        else:
            tmp.append(right_array[j])
            j += 1

    if i == len(left_array):
        for k in range(j, len(right_array)):
            tmp.append(right_array[k])
    if j == len(right_array):
        for k in range(i, len(left_array)):
            tmp.append(left_array[k])
    return tmp


if __name__ == '__main__':
    array = [1, 3, 2, 4, 3, 2, 5, 1, 6, 10]
    result = mergeSort(array, 0, len(array)-1)
    print(result)
