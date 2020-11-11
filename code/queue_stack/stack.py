### sort numbers with 2 stacks
### S1 || 1342
### S2 || 

### stack1: 用于放unsorted elements
### stack2: 分成左右两部分
### S2|| left part  ||| right part
### S2 || 1 2   ||| 4 3   temp_min = 3
#   左边部分用于存放之前的循环中sorted 的elements
#   右边的部分用于 buffer 作用

### stack1 = [1,3,2,4]
def sort_using_stack(stack1, stack2):
    
    length = len(stack1)
    left_size = 0 ## 记录左边sorted 的数量，剩下的部分就是右边的buffer size
    while left_size != length:
        tmp_min = float('inf')

        while len(stack1) != 0:
            num = stack1.pop()

            if num <= tmp_min:
                tmp_min = num
            stack2.append(num)
        
        ## 到左边sorted 数量就停止
        while len(stack2) != left_size:
            num = stack2.pop()
            if num > tmp_min:
                stack1.append(num)

        stack2.append(tmp_min)
        left_size += 1
    return stack2
    
if __name__ == '__main__':
    print(sort_using_stack([1,4,3,5,2], []))