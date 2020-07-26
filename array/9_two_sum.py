# Given an anrray and int. Find one and the only
# combination of array values, which in sum gives int

def twoSum(nums, target):
	diffs = {}
    for i in range(len(nums)):            
        if nums[i] in diffs:
        	return [diffs[nums[i]], i]
            
        diffs[target - nums[i]] = i
