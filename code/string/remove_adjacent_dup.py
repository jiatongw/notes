def removeDuplicates(S):
    if not S:
        return S
    
    stack = []
    i = 0
    while i < len(S):
        if not stack or i == 0:
            stack.append(S[i])
            i += 1
            continue
        if i != 0 and S[i] != stack[-1]:
            stack.append(S[i])
            i += 1
            continue
        while i < len(S) and S[i] == stack[-1]:
            i += 1
        stack.pop()
    print(''.join(stack))
removeDuplicates("aaaaaa")