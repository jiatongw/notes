### LC 74 ###
### LC 240 也可用同样解法
### T(n) = log(m) + log(n) = log(m * n)
 
def searchMatrix(matrix, target):
    if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
        return False

    ##从最左下角开始找起
    x = len(matrix) - 1
    y = 0

    while x >= 0 and y < len(matrix[0]):
        if matrix[x][y] == target:
            return True
        elif matrix[x][y] > target:
            x -= 1
        else:
            y += 1

    return False



    