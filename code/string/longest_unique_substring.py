'''
ABCDEFDEG -> longest ABCDEF len=6
'''

def uniqueChar(s):
    if not s:
        return 0, 0
    slow = 0
    fast = 0
    longest = 0
    hashset = set()
    index = 0

    while fast < len(s):
        if s[fast] not in hashset:
            hashset.add(s[fast])
            fast += 1
            if fast - slow > longest:
                longest = fast - slow
                index = slow
        else:
            hashset.remove(s[slow])
            slow += 1
    return longest, index

print(uniqueChar("AABBBCDKITBHHHHWIFLTGHSUDGLNQP"))
