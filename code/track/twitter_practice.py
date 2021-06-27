import collections
def countFreq(freq):
    '''
    input:
[user1, 51]
[user2, 52]
[user1, 60]
[user1, 51]
[user2, 70]
[user1, 54]
[user3, 54]
[user3, 55]
    '''

    map1 = collections.defaultdict(set)

    for u, f in freq:
        map1[u].add(f)
    
    map2 = {}

    for k in map1:
        t = len(map1[k]) 
        if t not in map2:
            map2[t] = 1
        else:
            map2[t] += 1
    
    print(map1)
    print(map2)
    for k, v in map2.items():
        print(str(k) + '->' + str(v))

input = [["user1", 51], ["user2", 52],["user1", 60],["user1", 51],["user2", 70],["user1", 54],["user3", 54],["user3", 55]]
countFreq(input)

