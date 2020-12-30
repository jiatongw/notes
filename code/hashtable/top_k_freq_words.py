def topKFrequent(words, k):
    if not words:
        return []
    maps = {}
    for w in words:
        if w not in maps:
            maps[w] = 1
        else:
            maps[w] += 1
    
    import queue
    pq = queue.PriorityQueue()
    
    for word, freq in maps.items():
        pq.put((-1*freq, word))

    res = []
    
    for i in range(0, k):
        res.append(pq.get()[1])
        
    return res

print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))