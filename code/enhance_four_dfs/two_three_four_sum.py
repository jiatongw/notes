'''
2 sum problem
'''

def twoSum(nums, target):
        
    m = {}
    
    for i in range(0, len(nums)):
        if nums[i] not in m:
            m[target - nums[i]] = i
        else:
            return [m[nums[i]], i]

'''
3 sum problem

LC 15
'''