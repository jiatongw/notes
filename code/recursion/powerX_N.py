#### LC 50 #####
## 还有其他方法，这里展示递归的方法
## 每次 x 的n次方，等于x的n/2 次方 乘以 x的n/2 次方
## 递归方法在LC上会超时

def power(x, n):

    if n == 0:
        return 1
    if n < 0:
        n = -1 * n
        return 1 / power(x, n)

    if n%2 == 0:
        return power(x, n//2) * power(x, n//2)
    else:
        return power(x, n//2) * power(x, n//2) * x

if __name__ == '__main__':
    print(power(3, -3))
