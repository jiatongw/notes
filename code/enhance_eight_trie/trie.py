'''
Trie

each node corresponds to a prefix of a word in the dictionary

'''

'''

how will you do to design a dictionary

先问: requirement/use case?
- search(word)
- delete
- add
- find all words with given prefix

options:
- hashmap O(m)
- linkedlist 
- sorted list O(m logn)
- Balanced BST O(m logn)
- Trie

    Trie: search, add, delete 时间复杂度都是O(m), m是单词长度
'''

'''
how to delete a word in Trie?

视频58分钟开始
'''

'''
Q DFS + Trie
Find all words with a given prefix
'''