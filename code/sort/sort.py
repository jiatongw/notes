###### Merge Sort ######
#### 每一步，找中点

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

###### Merge Sort ######
### LinkedList 版本  LC 148 ###




#### Quick sort #####
#### https://chinese.freecodecamp.org/news/sorting-in-python/ ###
#### 和上面的merge sort 不同，merge sort 用的是分治法
#### quick sort 下面的实现，用的是遍历法
#### quick sort 也有分治法实现的例子，但是空间复杂度太高，效率低

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        ## 左右指针往中间扫，发现左边比Pivot值大的，或者右边比pivot小的，就停
        while low <= high and array[low] <= array[start]:
            low += 1
        while low <= high and array[high] > array[start]:
            high -= 1
        
        ## 交换左右指针的值， 保证左边的值都比pivot小，右边的都比pivot大
        ## 继续循环
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    ## 交换pivot和high指针的值，这样就完成了第一轮：左边的值都比pivot小，右边的都比pivot大
    array[start], array[high] = array[high], array[start]

    return high ## return 下一个pivot

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = partition(array, start, end)
    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)



if __name__ == '__main__':
    array = [1, 3, 2, 4, 3, 2, 5, 1, 6, 10]
    # result = mergeSort(array, 0, len(array)-1)
    quick_sort(array, 0, len(array)-1)
    print(array)
