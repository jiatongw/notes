# def isBipartite(graph):
#     if not graph:
#         return True
    
#     queue = [(0, graph[0])]
#     color = {0: 1}
#     print(queue)
#     while queue:
        
#         node, neighbors = queue.pop(0)
        
#         for neighbor in neighbors:
#             print(neighbor)
#             if neighbor not in color:
#                 print(neighbor)
#                 # queue.append((neighbor, graph[neighbor])
#     #             color[neighbor] = -1 * color[node]
                        
#     #         elif neighbor in color:
#     #             if color[neighbor] == -1 * color[node]:
#     #                 continue
#     #             else:
#     #                 return False
#     # return True
# isBipartite([[1,3],[0,2],[1,3],[0,2]])

import copy
def combination(nums, target):
    if not nums:
        return 0
    res = []
    visited = [0] * len(nums)
    helper(nums, target, [], res, visited)
    return res

def helper(nums, remain, tmp, res, visited):
    if remain == 0:
        res.append(copy.deepcopy(tmp))
        return

    for i, num in enumerate(nums):
        # if remain < 0:
        #     break

        if visited[i]:
            continue
            
        tmp.append(nums[i])
        visited[i] = 1
        helper(nums, remain - nums[i], tmp, res, visited)
        tmp.pop()
        visited[i] = 0

print(combination([1,1,2,2], 3))